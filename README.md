# ODMR Principle Visualized

Publication-ready diagrams and reproducible figure generation for **Optically Detected Magnetic Resonance (ODMR)**
in Nitrogen-Vacancy (NV) centers in diamond.

**Repository:** <https://github.com/hafsaghannaj/OMDR-principle>

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

### Prerequisites

- Python **3.9+**
- For TikZ figures: a TeX distribution (`pdflatex`), plus optionally ImageMagick and `pdf2svg`

### Generate Python figures (fig 3, fig 6)

```bash
pip install -r scripts/requirements.txt
python scripts/generate_figures.py
```

### Compile TikZ figures (fig 1, 2, 4, 5)

```bash
python scripts/tikz2png.py
```

Requires `pdflatex`. See the script for optional PNG/SVG conversion dependencies.

If anything fails, open an issue with your OS, Python version, and full traceback.

---

## Reproducibility

This repository aims for deterministic figure generation **within a pinned dependency environment**.
Exact byte-for-byte identical outputs across different OS/font stacks are **not guaranteed** unless the rendering
toolchain (including fonts) is containerized and pinned.

---

## CI

GitHub Actions workflow (`.github/workflows/reproducibility.yml`) runs on every push and PR:
1. Installs Python 3.11 + pinned dependencies
2. Runs `generate_figures.py`
3. Uploads `diagrams/` as a build artifact

TikZ compilation is not yet in CI (requires a TeX distribution in the runner).

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
  url     = {https://github.com/hafsaghannaj/OMDR-principle}
}
```

---

## License

- **Code** (scripts, workflows): MIT — see [`LICENSE_CODE`](LICENSE_CODE)
- **Figures & diagrams**: CC-BY-4.0 — see [`LICENSE`](LICENSE)
