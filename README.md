# ODMR Principle Visualized

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Publication-ready diagrams explaining Optically Detected Magnetic Resonance (ODMR) in Nitrogen-Vacancy centers.**

Used in quantum sensing courses, instrument manuals, and research publications.

## Included Visualizations

| Diagram | Description |
|---------|-------------|
| `fig1_energy_levels` | NV- electronic structure with optical transitions |
| `fig2_odmr_workflow` | The 4-step measurement cycle (Initialization -> Control -> Sensing -> Readout) |
| `fig3_zeeman_splitting` | Magnetic field dependence, peak splitting |
| `fig4_fluorescence_contrast` | Time-trace showing bright/dark states |
| `fig5_nv_crystal_orientations` | 3D vector magnetometry explanation |
| `fig6_temperature_shift` | Thermometry via resonance shift |

## Quick Start

### Generate all figures

```bash
cd scripts/
pip install -r requirements.txt
python generate_figures.py
```

### Compile TikZ diagrams

```bash
python tikz2png.py
```

## Formats

All diagrams are provided in:

- **PNG** (300 DPI, publication ready)
- **SVG** (vector, editable in Inkscape/Illustrator)
- **PDF** (vector, embeddable in LaTeX)
- **TikZ** (LaTeX source, fully customizable)

## Theory

The NV center in diamond is a point defect consisting of a substitutional nitrogen atom adjacent to a carbon vacancy. Its ground state is a spin triplet (S=1) with a zero-field splitting of **D = 2.87 GHz** between the |0> and |+/-1> sublevels.

### The ODMR Cycle

1. **Initialization**: A 532 nm laser pulse optically pumps the NV center into the |0> spin state via spin-selective intersystem crossing through the singlet manifold.

2. **Microwave Control**: A resonant microwave pulse can coherently rotate the spin state. At f = D +/- gamma*B, the spin transfers to |+/-1>.

3. **Sensing**: The spin evolves under external perturbations (magnetic field, electric field, temperature, strain), accumulating phase proportional to the field strength.

4. **Readout**: A second laser pulse produces spin-state-dependent fluorescence. The |0> state fluoresces brightly (637 nm), while |+/-1> states are darker due to non-radiative decay through the singlet.

### Key Equations

- Zero-field splitting: D = 2.87 GHz (at 300 K)
- Zeeman splitting: df = 2 * gamma * B, where gamma = 28.025 GHz/T
- Temperature shift: dD/dT = -74.2 kHz/K
- Magnetic sensitivity (DC): eta ~ (h / g*mu_B) * 1/(C * sqrt(R * T2*))

## Cite This Work

```bibtex
@software{odmr_visualized_2026,
  author = {Hafsa Ghannaj},
  title = {ODMR Principle Visualized},
  year = {2026},
  url = {https://github.com/hafsaghannaj/ODMR-Principle-Visualized}
}
```

## Contributing

Pull requests welcome! Suggested additions:

- Quantum coherence protocols (T1, T2*, Ramsey fringes)
- Pulsed ODMR sequences (Rabi oscillations, Hahn echo, CPMG)
- DC vs AC magnetometry comparison
- Widefield ODMR imaging

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
