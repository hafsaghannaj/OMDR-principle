# ODMR Principle Visualized

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![LaTeX](https://img.shields.io/badge/LaTeX-TikZ-orange.svg)](https://www.ctan.org/pkg/pgf)

Publication-ready diagrams and reproducible figure generation for **Optically Detected Magnetic Resonance (ODMR)** in Nitrogen-Vacancy (NV) centers in diamond.

This repository provides deterministic, scriptable workflows for producing vector and raster figures suitable for journal articles, theses, course materials, and instrument documentation.

---

## Figure Gallery

All figures are generated programmatically. No manual editing is required to reproduce them.

| Figure | Filename | Description |
|:------:|----------|-------------|
| 1 | `fig1_energy_levels` | NV⁻ electronic structure: ground-state triplet (³A₂), excited-state triplet (³E), singlet manifold, optical transitions, and intersystem crossing pathways |
| 2 | `fig2_odmr_workflow` | Four-step ODMR measurement cycle: Initialization → Microwave Control → Sensing → Readout |
| 3 | `fig3_zeeman_splitting` | ODMR spectra under applied magnetic fields (0, 3, 5 mT), showing Zeeman-split resonance dips |
| 4 | `fig4_fluorescence_contrast` | Simulated time-domain fluorescence trace with bright/dark state contrast under resonant microwave drive |
| 5 | `fig5_nv_crystal_orientations` | Diamond lattice NV axis orientations and corresponding 8-dip vector magnetometry spectrum |
| 6 | `fig6_temperature_shift` | Temperature dependence of ODMR resonance frequency (dD/dT ≈ −74.2 kHz/K) |

### Output Formats

Each figure is provided in three formats:

- **PNG** — 300 DPI raster, suitable for manuscripts and presentations
- **SVG** — Scalable vector, editable in Inkscape or Illustrator
- **PDF** — Vector, embeddable directly in LaTeX documents

TikZ source files (`.tex`) are also included for three core diagrams, allowing full customization within LaTeX workflows.

---

## Quick Start

### Prerequisites

- Python 3.9 or later
- (Optional) A TeX distribution with `pdflatex` for compiling TikZ sources
- (Optional) ImageMagick and `pdf2svg` for TikZ-to-raster conversion

### Generate all Python-based figures

```bash
cd scripts/
pip install -r requirements.txt
python generate_figures.py
```

Output is written to `diagrams/png/`, `diagrams/svg/`, and `diagrams/pdf/`.

### Compile TikZ diagrams (optional)

```bash
python scripts/tikz2png.py
```

Requires `pdflatex`. See script output for details on optional converters.

---

## Pipeline

The figure generation follows a deterministic pipeline:

```
Theory & Parameters
    │
    ├── Python (matplotlib/numpy)
    │       └── generate_figures.py → PNG / SVG / PDF
    │
    └── LaTeX (TikZ/PGFPlots)
            └── tikz2png.py → PDF → PNG / SVG
```

All physical parameters (D = 2.87 GHz, γ = 28.025 GHz/T, dD/dT = −74.2 kHz/K) are defined as constants at the top of each script or within individual figure functions. Changing a parameter and re-running the script regenerates all dependent figures.

Random processes (e.g., fluorescence noise in Fig. 4) use fixed seeds (`np.random.seed(42)`) for bitwise reproducibility.

---

## Theory

The NV center in diamond is a point defect consisting of a substitutional nitrogen atom adjacent to a carbon vacancy. Its negatively charged state (NV⁻) has a spin-triplet ground state (S = 1) with a zero-field splitting of **D = 2.87 GHz** between the |0⟩ and |±1⟩ sublevels.

### The ODMR Cycle

1. **Initialization** — A 532 nm laser pulse optically pumps the NV center into the |0⟩ spin state via spin-selective intersystem crossing through the singlet manifold.

2. **Microwave Control** — A resonant microwave pulse coherently rotates the spin state. At f = D ± γB, the spin transfers to |±1⟩.

3. **Sensing** — The spin evolves under external perturbations (magnetic field, electric field, temperature, strain), accumulating phase proportional to the field strength.

4. **Readout** — A second laser pulse produces spin-state-dependent fluorescence. The |0⟩ state fluoresces brightly (637 nm), while |±1⟩ states are darker due to non-radiative decay through the singlet.

### Key Equations

| Quantity | Expression | Value |
|----------|-----------|-------|
| Zero-field splitting | D | 2.87 GHz (at 300 K) |
| Zeeman splitting | Δf = 2γB | γ = 28.025 GHz/T |
| Temperature shift | dD/dT | −74.2 kHz/K |
| DC magnetic sensitivity | η ~ (ℏ / gμ_B) · 1/(C √(R · T₂*)) | — |

---

## Reproducibility

- All figures are generated from source code with no manual post-processing.
- Python scripts use fixed random seeds where stochastic elements appear.
- The `requirements.txt` pins minimum package versions for compatibility.
- Running `generate_figures.py` on any system with the specified dependencies produces identical output.

### Environment

```
Python     >= 3.9
numpy      >= 1.24
matplotlib >= 3.7
scipy      >= 1.10
```

For TikZ compilation: any modern TeX distribution (TeX Live 2022+, MiKTeX, or MacTeX).

---

## Use Cases

- **Journal articles** — Embed PNG/PDF figures directly; cite this repository.
- **Theses and dissertations** — Use TikZ sources for consistent styling with your document.
- **Course materials** — The ODMR cycle diagram and energy level figure are designed for lecture slides and problem sets.
- **Lab onboarding** — The experimental setup documentation and parameter tables serve as quick-reference guides.
- **Instrument manuals** — Figures are licensed CC BY 4.0 for inclusion in technical documentation.

---

## Documentation

Additional documentation is available in the `docs/` directory and served via GitHub Pages:

- [Theory](docs/theory.md) — Detailed ODMR theory and electronic structure
- [Experimental Setup](docs/experimental.md) — Component specifications and measurement protocols

---

## References

1. Doherty, M.W. et al. "The nitrogen-vacancy colour centre in diamond." *Physics Reports* **528**, 1–45 (2013). [doi:10.1016/j.physrep.2013.02.001](https://doi.org/10.1016/j.physrep.2013.02.001)

2. Rondin, L. et al. "Magnetometry with nitrogen-vacancy defects in diamond." *Reports on Progress in Physics* **77**, 056503 (2014). [doi:10.1088/0034-4885/77/5/056503](https://doi.org/10.1088/0034-4885/77/5/056503)

3. Barry, J.F. et al. "Sensitivity optimization for NV-diamond magnetometry." *Reviews of Modern Physics* **92**, 015004 (2020). [doi:10.1103/RevModPhys.92.015004](https://doi.org/10.1103/RevModPhys.92.015004)

4. Gruber, A. et al. "Scanning confocal optical microscopy and magnetic resonance on single defect centers." *Science* **276**, 2012–2014 (1997). [doi:10.1126/science.276.5321.2012](https://doi.org/10.1126/science.276.5321.2012)

---

## Citing This Work

If you use these diagrams in a publication, please cite:

```bibtex
@software{odmr_visualized_2026,
  author       = {Hafsa Ghannaj},
  title        = {{ODMR Principle Visualized}},
  year         = {2026},
  url          = {https://github.com/hafsaghannaj/OMDR-principle},
  license      = {CC-BY-4.0}
}
```

A machine-readable citation is also available in [`CITATION.cff`](CITATION.cff).

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Suggested additions:

- Quantum coherence protocols (T₁, T₂*, Ramsey fringes)
- Pulsed ODMR sequences (Rabi oscillations, Hahn echo, CPMG)
- DC vs. AC magnetometry comparison
- Widefield ODMR imaging

---

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
