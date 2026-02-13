#!/usr/bin/env python3
"""
Compile TikZ .tex files to PDF, PNG, and SVG.

Input directory:
  diagrams/source/tikz/*.tex

Outputs:
  diagrams/pdf/<stem>.pdf
  diagrams/png/<stem>.png   (300 DPI)
  diagrams/svg/<stem>.svg

Required:
  - pdflatex

Preferred converters (in priority order):
  - pdftocairo (Poppler)  [recommended on macOS via: brew install poppler]
  - ImageMagick (magick/convert)
  - pdf2svg (SVG only)
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TIKZ_DIR = ROOT / "diagrams" / "source" / "tikz"
PNG_DIR = ROOT / "diagrams" / "png"
SVG_DIR = ROOT / "diagrams" / "svg"
PDF_DIR = ROOT / "diagrams" / "pdf"


def tool_exists(name: str) -> bool:
    return shutil.which(name) is not None


def run(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd, cwd=str(cwd) if cwd else None, capture_output=True, text=True
    )


def ensure_dirs() -> None:
    for d in (PNG_DIR, SVG_DIR, PDF_DIR):
        d.mkdir(parents=True, exist_ok=True)


def compile_pdf(tex_file: Path, tmpdir: Path) -> Path | None:
    shutil.copy(tex_file, tmpdir / tex_file.name)
    res = run(["pdflatex", "-interaction=nonstopmode", tex_file.name], cwd=tmpdir)

    pdf_path = tmpdir / f"{tex_file.stem}.pdf"
    if not pdf_path.exists():
        print(f"ERROR: pdflatex failed for {tex_file.name}")
        if res.stdout:
            print(res.stdout[-800:])
        if res.stderr:
            print(res.stderr[-800:])
        return None
    return pdf_path


def pdf_to_png(pdf_path: Path, png_out: Path, dpi: int = 300) -> bool:
    if tool_exists("pdftocairo"):
        prefix = png_out.with_suffix("")
        run(["pdftocairo", "-png", "-r", str(dpi), str(pdf_path), str(prefix)])
        # pdftocairo appends -1 for single-page PDFs
        candidate = prefix.parent / f"{prefix.name}-1.png"
        if candidate.exists():
            candidate.replace(png_out)
            return True
        if png_out.exists():
            return True
        return False

    if tool_exists("magick"):
        res = run(["magick", "-density", str(dpi), str(pdf_path), "-quality", "100", str(png_out)])
        return png_out.exists() and res.returncode == 0

    if tool_exists("convert"):
        res = run(["convert", "-density", str(dpi), str(pdf_path), "-quality", "100", str(png_out)])
        return png_out.exists() and res.returncode == 0

    print("  (skipping PNG - no converter found: install poppler or ImageMagick)")
    return False


def pdf_to_svg(pdf_path: Path, svg_out: Path) -> bool:
    if tool_exists("pdftocairo"):
        res = run(["pdftocairo", "-svg", str(pdf_path), str(svg_out)])
        return svg_out.exists() and res.returncode == 0

    if tool_exists("pdf2svg"):
        res = run(["pdf2svg", str(pdf_path), str(svg_out)])
        return svg_out.exists() and res.returncode == 0

    print("  (skipping SVG - no converter found: install poppler or pdf2svg)")
    return False


def compile_one(tex_file: Path) -> bool:
    stem = tex_file.stem
    print(f"Compiling {tex_file.name} ...")
    with tempfile.TemporaryDirectory() as td:
        tmpdir = Path(td)
        pdf_path = compile_pdf(tex_file, tmpdir)
        if pdf_path is None:
            return False

        shutil.copy(pdf_path, PDF_DIR / f"{stem}.pdf")
        print("  -> PDF")

        if pdf_to_png(pdf_path, PNG_DIR / f"{stem}.png", dpi=300):
            print("  -> PNG")

        if pdf_to_svg(pdf_path, SVG_DIR / f"{stem}.svg"):
            print("  -> SVG")

    return True


def main() -> None:
    ensure_dirs()

    if not tool_exists("pdflatex"):
        print("ERROR: pdflatex not found.")
        print("Install TeX:")
        print('  macOS: brew install --cask basictex  (then: export PATH="/Library/TeX/texbin:$PATH")')
        print("  Ubuntu: apt-get install texlive-latex-base texlive-latex-extra texlive-pictures")
        sys.exit(1)

    tex_files = sorted(TIKZ_DIR.glob("*.tex"))
    if not tex_files:
        print(f"No .tex files found in {TIKZ_DIR}")
        print("Create one under diagrams/source/tikz/ and re-run.")
        return

    ok = True
    print(f"Found {len(tex_files)} TikZ source files in {TIKZ_DIR}:")
    for f in tex_files:
        ok = compile_one(f) and ok

    if not ok:
        sys.exit(2)

    print("Done.")


if __name__ == "__main__":
    main()
