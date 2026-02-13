# ODMR Principle Visualized

[![Reproducible Build](https://github.com/hafsaghannaj/ODMR-principle/actions/workflows/reproducibility.yml/badge.svg)](https://github.com/hafsaghannaj/ODMR-principle/actions/workflows/reproducibility.yml)

Publication-ready diagrams and reproducible figure generation for **Optically Detected Magnetic Resonance (ODMR)**
in Nitrogen-Vacancy (NV) centers in diamond.

**Repository:** <https://github.com/hafsaghannaj/ODMR-principle>

---

## What this repository is (and is not)

- **Is:** a figure/diagram artifact repository intended for papers, theses, lecture slides, and lab docs.
- **Is not:** a full ODMR analysis package or experimental control stack.

---

## Figure Gallery (generated programmatically)

| Figure | Filename | Generator | Description |
|:--:|--|--|--|
| 3 | `fig3_zeeman_splitting` | Python | Illustrative ODMR dips under B = 0, 3, 5 mT (Lorentzian dip model) |
| 6 | `fig6_temperature_shift` | Python | Illustrative linear shift of ZFS parameter D with temperature (dD/dT) |

### Output formats

Each figure is produced as:
- **PNG** (300 DPI)
- **SVG**
- **PDF**

Outputs are written to `diagrams/png/`, `diagrams/svg/`, `diagrams/pdf/`.

---

## Quick Start

### Option 1: Docker (recommended — fully reproducible)

```bash
docker build -t odmr-viz .
docker run --rm -v $(pwd):/workspace odmr-viz
```

This generates all figures (Python + TikZ) in an identical environment every time.

### Option 2: Local Python (figures 3 and 6 only)

Prerequisites: Python **3.9+**

```bash
pip install -r scripts/requirements.txt
python scripts/generate_figures.py
```

If anything fails, open an issue with your OS, Python version, and full traceback.

---

## TikZ workflow

Compile TikZ `.tex` sources from `diagrams/source/tikz/` into PDF, PNG, and SVG:

```bash
python scripts/tikz2png.py
```

Requires `pdflatex` (TeX distribution) and `pdftocairo` (Poppler) for PNG/SVG conversion.

**macOS setup:**

```bash
brew install --cask basictex
export PATH="/Library/TeX/texbin:$PATH"
brew install poppler
```

---

## Reproducibility

This repository provides a **Dockerfile** that pins the entire toolchain (Ubuntu 22.04, TeX Live, Python 3.11,
and all dependencies) to ensure byte-for-byte identical figure output across any machine.

For local (non-Docker) runs, outputs are deterministic within a pinned dependency environment but may
vary across different OS/font stacks.

---

## CI

GitHub Actions workflow (`.github/workflows/reproducibility.yml`) runs on every push and PR:

1. Builds the Docker image (pins entire toolchain)
2. Generates all figures (Python + TikZ) inside the container
3. Uploads `diagrams/` as a build artifact

---

## Theory & Documentation

See `docs/`:
- `docs/theory.md`
- `docs/experimental.md`

---

## References

1. Doherty, M.W. et al. *Physics Reports* **528**, 1–45 (2013). doi:10.1016/j.physrep.2013.02.001
2. Rondin, L. et al. *Rep. Prog. Phys.* **77**, 056503 (2014). doi:10.1088/0034-4885/77/5/056503
3. Barry, J.F. et al. *Rev. Mod. Phys.* **92**, 015004 (2020). doi:10.1103/RevModPhys.92.015004
4. Gruber, A. et al. *Science* **276**, 2012–2014 (1997). doi:10.1126/science.276.5321.2012

---

## Citing this work

Machine-readable metadata: [`CITATION.cff`](CITATION.cff)

```bibtex
@software{ghannaj_odmr_principle_visualized_2026,
  author  = {Ghannaj, Hafsa},
  title   = {ODMR Principle Visualized},
  year    = {2026},
  url     = {https://github.com/hafsaghannaj/ODMR-principle}
}
```

---

## License

- **Code** (scripts, workflows): MIT — see [`LICENSE_CODE`](LICENSE_CODE)
- **Figures & diagrams**: CC-BY-4.0 — see [`LICENSE`](LICENSE)
