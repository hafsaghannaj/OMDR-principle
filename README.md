# ODMR Principle Visualized

Publication-ready diagrams and reproducible figure generation for **Optically Detected Magnetic Resonance (ODMR)**
in Nitrogen-Vacancy (NV) centers in diamond.

**Repository:** https://github.com/hafsaghannaj/OMDR-principle

---

## What this repository is (and is not)

- **Is:** a figure/diagram artifact repository intended for papers, theses, lecture slides, and lab docs.
- **Is not:** a full ODMR analysis package or experimental control stack.

---

## Figure Gallery (generated programmatically)

| Figure | Filename | Description |
|:------:|----------|-------------|
| 3 | `fig3_zeeman_splitting` | ODMR spectra under applied magnetic fields (0, 3, 5 mT), showing Zeeman-split resonance dips |
| 6 | `fig6_temperature_shift` | Temperature dependence of the ODMR zero-field splitting parameter D (illustrative linear model) |

### Output formats
Each figure is produced as:
- **PNG** (300 DPI)
- **SVG**
- **PDF**

Outputs are written to:
- `diagrams/png/`
- `diagrams/svg/`
- `diagrams/pdf/`

---

## Quick Start

### Prerequisites
- Python **3.9+**

### Generate figures
```bash
cd scripts
python -m pip install -r requirements.txt
python generate_figures.py
```

If this fails, open an issue with:
- OS + Python version
- full traceback

---

## Reproducibility policy (what we guarantee)

- Deterministic figure generation **given pinned dependencies**.
- Any stochastic elements (if added later) must use fixed seeds.

> Exact byte-for-byte identity across OS/font stacks is **not guaranteed** unless fonts and rendering toolchain
> are pinned (e.g., containers + font bundles). CI will enforce “script runs and produces outputs” first.

---

## Theory & documentation
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
Machine-readable metadata: `CITATION.cff`

```bibtex
@software{ghannaj_odmr_principle_visualized_2026,
  author  = {Ghannaj, Hafsa},
  title   = {ODMR Principle Visualized},
  year    = {2026},
  url     = {https://github.com/hafsaghannaj/OMDR-principle}
}
```
