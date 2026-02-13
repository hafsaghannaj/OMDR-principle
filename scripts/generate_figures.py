#!/usr/bin/env python3
"""Generate deterministic ODMR figures for a minimal reproducible pipeline."""

from __future__ import annotations

import sys
import traceback
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


BASE_DIR = Path(__file__).resolve().parent.parent
DIAGRAMS_DIR = BASE_DIR / "diagrams"
PNG_DIR = DIAGRAMS_DIR / "png"
SVG_DIR = DIAGRAMS_DIR / "svg"
PDF_DIR = DIAGRAMS_DIR / "pdf"
OUTPUT_DIRS = (PNG_DIR, SVG_DIR, PDF_DIR)

ZERO_FIELD_SPLITTING_GHZ = 2.87
GYROMAGNETIC_RATIO_GHZ_PER_T = 28.025
TEMP_COEFF_GHZ_PER_K = -74.2e-6


def configure_style() -> None:
    """Set a publication-friendly plotting style."""
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 11,
            "axes.linewidth": 1.1,
            "xtick.major.width": 1.0,
            "ytick.major.width": 1.0,
            "figure.dpi": 300,
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.08,
        }
    )


def ensure_output_dirs() -> None:
    """Create output directories for PNG/SVG/PDF artifacts."""
    for directory in OUTPUT_DIRS:
        directory.mkdir(parents=True, exist_ok=True)


def lorentzian_dip(freq_ghz: np.ndarray, center_ghz: float, fwhm_ghz: float, depth: float) -> np.ndarray:
    """Return a normalized Lorentzian dip line shape."""
    gamma = fwhm_ghz / 2.0
    return 1.0 - depth * (gamma**2 / ((freq_ghz - center_ghz) ** 2 + gamma**2))


def save_figure(fig: plt.Figure, stem: str) -> list[Path]:
    """Save one figure in PNG, SVG, and PDF formats."""
    outputs: list[Path] = []
    targets = ((PNG_DIR, "png"), (SVG_DIR, "svg"), (PDF_DIR, "pdf"))

    for directory, extension in targets:
        output_path = directory / f"{stem}.{extension}"
        fig.savefig(output_path)
        outputs.append(output_path)

    plt.close(fig)
    return outputs


def fig3_zeeman_splitting() -> list[Path]:
    """Generate Zeeman splitting ODMR spectra for three magnetic fields."""
    freq_ghz = np.linspace(2.70, 3.04, 2400)
    fields_mT = (0.0, 3.0, 5.0)
    colors = ("#1f77b4", "#ff7f0e", "#d62728")

    fig, ax = plt.subplots(figsize=(9.0, 5.3))

    for field_mT, color in zip(fields_mT, colors):
        if field_mT == 0.0:
            spectrum = lorentzian_dip(
                freq_ghz,
                center_ghz=ZERO_FIELD_SPLITTING_GHZ,
                fwhm_ghz=0.010,
                depth=0.16,
            )
        else:
            shift_ghz = GYROMAGNETIC_RATIO_GHZ_PER_T * (field_mT * 1e-3)
            left = lorentzian_dip(
                freq_ghz,
                center_ghz=ZERO_FIELD_SPLITTING_GHZ - shift_ghz,
                fwhm_ghz=0.008,
                depth=0.12,
            )
            right = lorentzian_dip(
                freq_ghz,
                center_ghz=ZERO_FIELD_SPLITTING_GHZ + shift_ghz,
                fwhm_ghz=0.008,
                depth=0.12,
            )
            spectrum = left * right

        ax.plot(freq_ghz, spectrum, color=color, lw=2.0, label=f"B = {field_mT:g} mT")

    ax.axvline(ZERO_FIELD_SPLITTING_GHZ, color="0.45", ls=":", lw=1.0)
    ax.text(ZERO_FIELD_SPLITTING_GHZ + 0.0015, 1.003, "D = 2.87 GHz", color="0.35", fontsize=9)

    ax.set_title("Zeeman Splitting in ODMR Spectra", fontweight="bold")
    ax.set_xlabel("Microwave Frequency (GHz)")
    ax.set_ylabel("Normalized Fluorescence")
    ax.set_ylim(0.82, 1.02)
    ax.grid(alpha=0.25)
    ax.legend(framealpha=0.9)

    formula_box = "$\\Delta f = 2\\gamma B$\n$\\gamma = 28.025$ GHz/T"
    ax.text(
        0.02,
        0.03,
        formula_box,
        transform=ax.transAxes,
        fontsize=10,
        va="bottom",
        bbox={"boxstyle": "round", "facecolor": "#f9fafb", "edgecolor": "0.5"},
    )

    return save_figure(fig, "fig3_zeeman_splitting")


def fig6_temperature_shift() -> list[Path]:
    """Generate ODMR temperature shift spectra with dD/dT labeling."""
    freq_ghz = np.linspace(2.84, 2.89, 2400)
    temperatures_k = (300, 325, 350, 400)
    colors = ("#1f77b4", "#2ca02c", "#ff7f0e", "#d62728")

    fig, ax = plt.subplots(figsize=(9.0, 5.3))

    centers: list[float] = []
    for temp_k, color in zip(temperatures_k, colors):
        delta_temp = temp_k - 300
        center = ZERO_FIELD_SPLITTING_GHZ + TEMP_COEFF_GHZ_PER_K * delta_temp
        centers.append(center)

        signal = lorentzian_dip(
            freq_ghz,
            center_ghz=center,
            fwhm_ghz=0.006,
            depth=0.16,
        )

        ax.plot(freq_ghz, signal, color=color, lw=2.0, label=f"T = {temp_k} K")
        ax.axvline(center, color=color, ls=":", lw=1.0, alpha=0.45)

    center_300 = centers[0]
    center_400 = centers[-1]
    shift_mhz = (center_400 - center_300) * 1e3

    ax.annotate(
        "",
        xy=(center_400, 0.885),
        xytext=(center_300, 0.885),
        arrowprops={"arrowstyle": "<->", "lw": 1.8, "color": "#7e22ce"},
    )
    ax.text(
        (center_300 + center_400) / 2,
        0.892,
        f"{shift_mhz:.2f} MHz over 100 K",
        ha="center",
        fontsize=9,
        color="#7e22ce",
        fontweight="bold",
    )

    ax.set_title("ODMR Temperature Dependence", fontweight="bold")
    ax.set_xlabel("Microwave Frequency (GHz)")
    ax.set_ylabel("Normalized Fluorescence")
    ax.set_ylim(0.82, 1.02)
    ax.grid(alpha=0.25)
    ax.legend(framealpha=0.9)

    ax.text(
        0.02,
        0.03,
        "$dD/dT \\approx -74.2$ kHz/K",
        transform=ax.transAxes,
        fontsize=10,
        va="bottom",
        bbox={"boxstyle": "round", "facecolor": "#f9fafb", "edgecolor": "0.5"},
    )

    return save_figure(fig, "fig6_temperature_shift")


def main() -> int:
    """Run the minimal deterministic figure generation pipeline."""
    try:
        ensure_output_dirs()
        configure_style()

        generators = (
            ("fig3_zeeman_splitting", fig3_zeeman_splitting),
            ("fig6_temperature_shift", fig6_temperature_shift),
        )

        print("Generating deterministic ODMR figures (v0.1)...")
        produced_files: list[Path] = []

        for name, generator in generators:
            print(f"  - {name}")
            produced_files.extend(generator())

        print("\nGenerated files:")
        for output_file in produced_files:
            print(f"  {output_file.relative_to(BASE_DIR)}")

        print("\nOutputs written to:")
        for directory in OUTPUT_DIRS:
            print(f"  {directory.resolve()}")

        return 0
    except Exception as exc:  # pragma: no cover - runtime guard
        print(f"ERROR: figure generation failed: {exc}", file=sys.stderr)
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
