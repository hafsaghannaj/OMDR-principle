#!/usr/bin/env python3
"""
Compile TikZ .tex files to PNG, SVG, and PDF.

Requires: pdflatex, pdf2svg (optional), ImageMagick convert (optional)

Usage:
    python tikz2png.py
"""

import subprocess
import shutil
from pathlib import Path
import sys
import tempfile

TIKZ_DIR = Path(__file__).parent.parent / "diagrams" / "source" / "tikz"
PNG_DIR = Path(__file__).parent.parent / "diagrams" / "png"
SVG_DIR = Path(__file__).parent.parent / "diagrams" / "svg"
PDF_DIR = Path(__file__).parent.parent / "diagrams" / "pdf"


def check_tool(name):
    """Check if a command-line tool is available."""
    return shutil.which(name) is not None


def compile_tex(tex_file):
    """Compile a .tex file to PDF, then optionally to PNG and SVG."""
    stem = tex_file.stem
    print(f"  Compiling {tex_file.name}...")

    with tempfile.TemporaryDirectory() as tmpdir:
        # Copy tex file to temp dir
        shutil.copy(tex_file, Path(tmpdir) / tex_file.name)

        # pdflatex
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", tex_file.name],
            cwd=tmpdir, capture_output=True, text=True
        )

        pdf_path = Path(tmpdir) / f"{stem}.pdf"
        if not pdf_path.exists():
            print(f"    ERROR: pdflatex failed for {tex_file.name}")
            if result.stderr:
                print(f"    {result.stderr[:200]}")
            return

        # Copy PDF
        shutil.copy(pdf_path, PDF_DIR / f"{stem}.pdf")
        print(f"    -> PDF saved")

        # Convert to PNG (if ImageMagick available)
        if check_tool("magick"):
            png_out = PNG_DIR / f"{stem}.png"
            subprocess.run([
                "magick", "-density", "300", str(pdf_path),
                "-quality", "100", str(png_out)
            ], capture_output=True)
            print(f"    -> PNG saved")
        elif check_tool("convert"):
            png_out = PNG_DIR / f"{stem}.png"
            subprocess.run([
                "convert", "-density", "300", str(pdf_path),
                "-quality", "100", str(png_out)
            ], capture_output=True)
            print(f"    -> PNG saved")
        else:
            print("    (skipping PNG - ImageMagick not found)")

        # Convert to SVG (if pdf2svg available)
        if check_tool("pdf2svg"):
            svg_out = SVG_DIR / f"{stem}.svg"
            subprocess.run([
                "pdf2svg", str(pdf_path), str(svg_out)
            ], capture_output=True)
            print(f"    -> SVG saved")
        else:
            print("    (skipping SVG - pdf2svg not found)")


def main():
    if not check_tool("pdflatex"):
        print("ERROR: pdflatex not found. Install a TeX distribution:")
        print("  macOS: brew install --cask mactex-no-gui")
        print("  Ubuntu: sudo apt install texlive-full")
        sys.exit(1)

    tex_files = sorted(TIKZ_DIR.glob("*.tex"))
    if not tex_files:
        print("No .tex files found in", TIKZ_DIR)
        return

    print(f"Found {len(tex_files)} TikZ source files:")
    for f in tex_files:
        compile_tex(f)

    print("\nDone.")


if __name__ == "__main__":
    main()
