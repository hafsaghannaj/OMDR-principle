# ODMR Principle Visualized

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![LaTeX](https://img.shields.io/badge/LaTeX-TikZ-orange.svg)](https://www.ctan.org/pkg/pgf)

Publication-ready diagrams and reproducible figure-generation workflows for Optically Detected Magnetic Resonance (ODMR) in nitrogen-vacancy (NV) centers in diamond.

Repository URL: https://github.com/hafsaghannaj/OMDR-principle

## What This Repository Contains

This project generates six ODMR/NV figures directly from source code. The figures are intended for papers, theses, lab onboarding docs, and teaching material.

Programmatically generated figures:

- `fig1_energy_levels`: NV- energy-level structure and optical/spin transitions
- `fig2_odmr_workflow`: four-step ODMR measurement cycle
- `fig3_zeeman_splitting`: ODMR dip splitting under applied magnetic field
- `fig4_fluorescence_contrast`: simulated bright/dark fluorescence readout trace
- `fig5_nv_crystal_orientations`: NV axis geometry and 8-dip spectrum context
- `fig6_temperature_shift`: resonance shift versus temperature

## Repository Layout

```text
.
├── diagrams/
│   ├── png/            # Generated PNG outputs
│   ├── svg/            # Generated SVG outputs
│   ├── pdf/            # Generated PDF outputs
│   └── source/
│       ├── tikz/       # TikZ source files
│       └── drawio/     # Draw.io source files
├── docs/               # Theory and experimental notes
├── scripts/
│   ├── generate_figures.py
│   ├── tikz2png.py
│   └── requirements.txt
├── CITATION.cff
└── README.md
```

## Quick Start

### 1) Install dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/requirements.txt
```

### 2) Generate Python-based figures

```bash
python scripts/generate_figures.py
```

Outputs are written to:

- `diagrams/png/`
- `diagrams/svg/`
- `diagrams/pdf/`

### 3) Compile TikZ figures (optional)

```bash
python scripts/tikz2png.py
```

Requirements for this optional step:

- `pdflatex` (required)
- `magick` or `convert` (optional PNG conversion)
- `pdf2svg` (optional SVG conversion)

## Reproducibility Statement

In this repository, reproducible means:

- Figures are generated from version-controlled source code (no manual post-editing required).
- The same scripts, parameters, and dependency versions should reproduce the same scientific content and visual structure.
- Stochastic elements in Python plots use fixed seeds where implemented.

Important scope note:

- File bytes are not guaranteed to be identical across all systems/toolchains. Rendering backends, fonts, library versions, and embedded metadata can change binary output while preserving the same figure content.

## Documentation

- `docs/theory.md`: ODMR theory and NV electronic structure
- `docs/experimental.md`: baseline setup and measurement protocol notes

## Citation

If you use these figures, cite the project using `CITATION.cff` or the BibTeX snippet below:

```bibtex
@software{odmr_visualized_2026,
  author       = {Hafsa Ghannaj},
  title        = {{ODMR Principle Visualized}},
  year         = {2026},
  url          = {https://github.com/hafsaghannaj/OMDR-principle},
  license      = {CC-BY-4.0}
}
```

## Contributing

See `CONTRIBUTING.md` for contribution guidelines.

## License

This project is licensed under CC BY 4.0. See `LICENSE`.
