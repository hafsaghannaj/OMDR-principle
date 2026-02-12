#!/usr/bin/env python3
"""
Generate all ODMR principle diagrams as publication-ready PNGs and SVGs.

Usage:
    python generate_figures.py

Output:
    ../diagrams/png/fig1_energy_levels.png
    ../diagrams/png/fig2_odmr_workflow.png
    ../diagrams/png/fig3_zeeman_splitting.png
    ../diagrams/png/fig4_fluorescence_contrast.png
    ../diagrams/png/fig5_nv_crystal_orientations.png
    ../diagrams/png/fig6_temperature_shift.png
    (+ corresponding SVGs)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from mpl_toolkits.mplot3d import Axes3D
from pathlib import Path

# Output directories
BASE = Path(__file__).parent.parent / "diagrams"
PNG_DIR = BASE / "png"
SVG_DIR = BASE / "svg"
PDF_DIR = BASE / "pdf"

for d in [PNG_DIR, SVG_DIR, PDF_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# Publication style
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.linewidth": 1.2,
    "xtick.major.width": 1.0,
    "ytick.major.width": 1.0,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.15,
})


def lorentzian(f, f0, gamma, contrast):
    """Lorentzian dip profile for ODMR resonance."""
    return 1 - contrast * (gamma**2 / ((f - f0)**2 + gamma**2))


def save_fig(fig, name):
    """Save figure in PNG, SVG, and PDF formats."""
    fig.savefig(PNG_DIR / f"{name}.png")
    fig.savefig(SVG_DIR / f"{name}.svg")
    fig.savefig(PDF_DIR / f"{name}.pdf")
    plt.close(fig)
    print(f"  Saved {name}")


# =========================================================================
# Figure 1: Energy Level Diagram
# =========================================================================
def fig1_energy_levels():
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(-1, 10)
    ax.axis("off")

    lw = 3

    # Ground state triplet (3A2)
    ax.plot([1, 4], [0, 0], color="#2563eb", lw=lw)
    ax.text(4.2, 0, r"$|0\rangle$", fontsize=14, va="center", color="#2563eb")
    ax.plot([1, 4], [1.5, 1.5], color="#dc2626", lw=lw)
    ax.text(4.2, 1.5, r"$|\pm1\rangle$", fontsize=14, va="center", color="#dc2626")

    # ZFS bracket
    ax.annotate("", xy=(5, 1.5), xytext=(5, 0),
                arrowprops=dict(arrowstyle="<->", lw=1.5, color="gray"))
    ax.text(5.3, 0.75, "D = 2.87 GHz", fontsize=11, fontweight="bold",
            va="center", color="gray")

    ax.text(0.3, 0.75, r"${}^3A_2$", fontsize=16, fontweight="bold",
            va="center", ha="center")

    # Excited state triplet (3E)
    ax.plot([1, 4], [6, 6], color="#2563eb", lw=lw)
    ax.text(4.2, 6, r"$|0\rangle$", fontsize=14, va="center", color="#2563eb")
    ax.plot([1, 4], [7.2, 7.2], color="#dc2626", lw=lw)
    ax.text(4.2, 7.2, r"$|\pm1\rangle$", fontsize=14, va="center", color="#dc2626")

    ax.text(0.3, 6.6, r"${}^3E$", fontsize=16, fontweight="bold",
            va="center", ha="center")

    # Singlet states
    ax.plot([8, 11], [5.5, 5.5], color="gray", lw=lw, ls="--")
    ax.text(11.2, 5.5, r"${}^1A_1$", fontsize=13, va="center", color="gray")
    ax.plot([8, 11], [2.5, 2.5], color="gray", lw=lw, ls="--")
    ax.text(11.2, 2.5, r"${}^1E$", fontsize=13, va="center", color="gray")

    ax.text(9.5, 8.5, "Singlet", fontsize=13, fontweight="bold",
            ha="center", color="gray")

    # Green excitation arrows
    for x_pos in [1.8, 2.8]:
        ax.annotate("", xy=(x_pos, 5.8), xytext=(x_pos, 1.7 if x_pos > 2 else 0.2),
                    arrowprops=dict(arrowstyle="->,head_width=0.3",
                                    lw=2.5, color="#16a34a"))
    ax.text(1.0, 3.5, "532 nm", fontsize=11, color="#16a34a", fontweight="bold",
            rotation=90, va="center")

    # Red fluorescence (wavy would need custom - use dashed)
    ax.annotate("", xy=(3.5, 0.2), xytext=(3.5, 5.8),
                arrowprops=dict(arrowstyle="->,head_width=0.4",
                                lw=3, color="#ef4444", linestyle="--"))
    ax.text(3.8, 3.5, "637 nm\n(bright)", fontsize=10, color="#ef4444",
            fontweight="bold", va="center")

    # ISC arrows
    # |+/-1> excited -> singlet (strong)
    ax.annotate("", xy=(8, 5.5), xytext=(4, 7.0),
                arrowprops=dict(arrowstyle="->,head_width=0.25",
                                lw=2, color="#94a3b8", linestyle=":"))
    ax.text(6, 6.8, "ISC\n(strong)", fontsize=9, color="#64748b",
            ha="center", va="center")

    # Singlet 1A1 -> 1E
    ax.annotate("", xy=(9.5, 2.7), xytext=(9.5, 5.3),
                arrowprops=dict(arrowstyle="->,head_width=0.25",
                                lw=2, color="#7c3aed"))
    ax.text(10, 4, "1042 nm", fontsize=10, color="#7c3aed", rotation=90,
            va="center")

    # Singlet 1E -> |0> ground (preferential)
    ax.annotate("", xy=(4, 0.2), xytext=(8, 2.3),
                arrowprops=dict(arrowstyle="->,head_width=0.25",
                                lw=2, color="#3b82f6", linestyle=":"))
    ax.text(6, 0.8, r"to $|0\rangle$ (preferential)", fontsize=9,
            color="#3b82f6", ha="center")

    ax.set_title(r"NV$^-$ Center Energy Level Structure", fontsize=18,
                 fontweight="bold", pad=20)

    save_fig(fig, "fig1_energy_levels")


# =========================================================================
# Figure 2: ODMR Measurement Cycle Workflow
# =========================================================================
def fig2_odmr_workflow():
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle("The ODMR Measurement Cycle", fontsize=20, fontweight="bold", y=0.98)
    fig.text(0.5, 0.93, r"Optically Detected Magnetic Resonance in NV$^-$ Centers",
             fontsize=13, ha="center", color="gray")

    steps = [
        {
            "num": "1", "title": "Initialization",
            "color": "#16a34a",
            "lines": [
                "Green laser pulse (532 nm)",
                r"Spin polarized to $|0\rangle$",
                "via intersystem crossing",
                "Bright fluorescence",
            ]
        },
        {
            "num": "2", "title": "MW Control",
            "color": "#ea580c",
            "lines": [
                "Microwave pulse applied",
                r"Frequency $\approx$ 2.87 GHz",
                r"If resonant: $|0\rangle \to |\pm1\rangle$",
                "Coherent spin rotation",
            ]
        },
        {
            "num": "3", "title": "Sensing",
            "color": "#2563eb",
            "lines": [
                "Spin evolves freely",
                "Accumulates phase from:",
                "B-field, temperature,",
                "strain, electric field",
            ]
        },
        {
            "num": "4", "title": "Readout",
            "color": "#dc2626",
            "lines": [
                "Second green laser pulse",
                r"$|0\rangle \to$ Bright (more photons)",
                r"$|\pm1\rangle \to$ Dim (fewer photons)",
                "Fluorescence = spin state",
            ]
        },
    ]

    for ax, step in zip(axes.flat, steps):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")

        # Background box
        bg = FancyBboxPatch((0.3, 0.3), 9.4, 9.4, boxstyle="round,pad=0.3",
                            facecolor=step["color"] + "08",
                            edgecolor=step["color"], linewidth=3)
        ax.add_patch(bg)

        # Step number circle
        circle = plt.Circle((1.5, 8.5), 0.7, color=step["color"],
                            zorder=5)
        ax.add_patch(circle)
        ax.text(1.5, 8.5, step["num"], fontsize=18, fontweight="bold",
                color="white", ha="center", va="center", zorder=6)

        # Title
        ax.text(3, 8.5, step["title"], fontsize=16, fontweight="bold",
                color=step["color"], va="center")

        # Description lines
        for i, line in enumerate(step["lines"]):
            weight = "bold" if i == len(step["lines"]) - 1 else "normal"
            ax.text(1.5, 6 - i * 1.3, line, fontsize=12, va="center",
                    fontweight=weight)

    # Arrows between panels
    fig.patches.extend([
        FancyArrowPatch((0.52, 0.52), (0.53, 0.52),
                        transform=fig.transFigure,
                        arrowstyle="->,head_width=6,head_length=4",
                        color="#16a34a", lw=3, mutation_scale=1),
    ])

    plt.tight_layout(rect=[0, 0, 1, 0.91])
    save_fig(fig, "fig2_odmr_workflow")


# =========================================================================
# Figure 3: Zeeman Splitting
# =========================================================================
def fig3_zeeman_splitting():
    fig, ax = plt.subplots(figsize=(10, 6))

    f = np.linspace(2.70, 3.04, 2000)

    configs = [
        (0, "#2563eb", 2.5, "B = 0 mT"),
        (3, "#ea580c", 2.0, "B = 3 mT"),
        (5, "#dc2626", 1.5, "B = 5 mT"),
    ]

    for B_mT, color, lw, label in configs:
        gamma_B = 28.025e-3 * B_mT  # GHz
        if B_mT == 0:
            signal = lorentzian(f, 2.87, 0.006, 0.15)
        else:
            signal = (lorentzian(f, 2.87 - gamma_B, 0.005, 0.12) *
                      lorentzian(f, 2.87 + gamma_B, 0.005, 0.12))
        ax.plot(f, signal, color=color, lw=lw, label=label)

    # Annotations
    ax.axvline(2.87, color="gray", ls=":", alpha=0.5)
    ax.text(2.872, 1.005, "D = 2.87 GHz", fontsize=9, color="gray")

    ax.annotate(r"$\Delta f = 2\gamma B$", xy=(2.87, 0.9),
                fontsize=12, color="#dc2626", ha="center",
                fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                          edgecolor="#dc2626", alpha=0.9))

    ax.set_xlabel("Microwave Frequency (GHz)", fontsize=13)
    ax.set_ylabel("Normalized Fluorescence", fontsize=13)
    ax.set_title("Zeeman Splitting in ODMR Spectra", fontsize=16,
                 fontweight="bold")
    ax.legend(fontsize=11, framealpha=0.9)
    ax.set_ylim(0.82, 1.02)
    ax.grid(True, alpha=0.2)

    # Equation box
    textstr = r"$\gamma = 28.025$ GHz/T" + "\n" + r"$\Delta f = 2\gamma B$"
    props = dict(boxstyle="round", facecolor="#f8fafc", edgecolor="gray",
                 alpha=0.9)
    ax.text(0.02, 0.02, textstr, transform=ax.transAxes, fontsize=10,
            va="bottom", bbox=props)

    save_fig(fig, "fig3_zeeman_splitting")


# =========================================================================
# Figure 4: Fluorescence Contrast
# =========================================================================
def fig4_fluorescence_contrast():
    fig, ax = plt.subplots(figsize=(10, 5))

    np.random.seed(42)
    t = np.linspace(0, 10, 2000)

    # Simulate time trace
    mw_on = (t > 3) & (t < 7)
    base_rate = 50000  # counts/s
    contrast = 0.20
    signal = np.where(mw_on, base_rate * (1 - contrast), base_rate)
    noise = np.random.normal(0, 1500, len(t))
    signal = signal + noise

    ax.plot(t, signal / 1000, color="#2563eb", lw=0.8, alpha=0.7)

    # Smoothed overlay
    kernel = np.ones(50) / 50
    smooth = np.convolve(signal, kernel, mode="same") / 1000
    ax.plot(t, smooth, color="#1e40af", lw=2, label="Smoothed signal")

    # Shaded regions
    ax.axvspan(0, 3, alpha=0.05, color="green", label="MW OFF (bright)")
    ax.axvspan(3, 7, alpha=0.08, color="red", label="MW ON (dark)")
    ax.axvspan(7, 10, alpha=0.05, color="green")

    # Level lines
    ax.axhline(base_rate / 1000, color="#16a34a", ls="--", lw=1.5, alpha=0.7)
    ax.text(0.1, base_rate / 1000 + 0.5, r"$I_{\mathrm{bright}}$",
            fontsize=12, color="#16a34a", fontweight="bold")
    ax.axhline(base_rate * (1 - contrast) / 1000, color="#dc2626",
               ls="--", lw=1.5, alpha=0.7)
    ax.text(0.1, base_rate * (1 - contrast) / 1000 - 1,
            r"$I_{\mathrm{dark}}$", fontsize=12, color="#dc2626",
            fontweight="bold")

    # Contrast annotation
    ax.annotate("", xy=(9.5, base_rate / 1000),
                xytext=(9.5, base_rate * (1 - contrast) / 1000),
                arrowprops=dict(arrowstyle="<->", lw=2, color="purple"))
    ax.text(9.0, (base_rate * (1 - contrast / 2)) / 1000,
            f"C = {contrast:.0%}", fontsize=12, color="purple",
            fontweight="bold", ha="right")

    ax.set_xlabel("Time (s)", fontsize=13)
    ax.set_ylabel("Fluorescence (kcounts/s)", fontsize=13)
    ax.set_title("Fluorescence Contrast in ODMR", fontsize=16,
                 fontweight="bold")
    ax.legend(loc="lower right", fontsize=10)
    ax.set_xlim(0, 10)
    ax.grid(True, alpha=0.2)

    # Equation box
    eq = r"$C = \frac{I_{\mathrm{bright}} - I_{\mathrm{dark}}}{I_{\mathrm{bright}}}$"
    props = dict(boxstyle="round", facecolor="white", edgecolor="purple", alpha=0.9)
    ax.text(0.5, 0.05, eq, transform=ax.transAxes, fontsize=14,
            ha="center", va="bottom", bbox=props)

    save_fig(fig, "fig4_fluorescence_contrast")


# =========================================================================
# Figure 5: NV Crystal Orientations
# =========================================================================
def fig5_nv_crystal_orientations():
    fig = plt.figure(figsize=(12, 6))

    # 3D crystal
    ax1 = fig.add_subplot(121, projection="3d")

    # Diamond unit cell (simplified cube)
    r = 1
    for s1 in [-r, r]:
        for s2 in [-r, r]:
            ax1.plot([s1, s1], [s2, s2], [-r, r], "k-", lw=0.5, alpha=0.3)
            ax1.plot([s1, s1], [-r, r], [s2, s2], "k-", lw=0.5, alpha=0.3)
            ax1.plot([-r, r], [s1, s1], [s2, s2], "k-", lw=0.5, alpha=0.3)

    # Four NV orientations (body diagonals)
    orientations = [
        ([1, 1, 1], "#dc2626", "[111]"),
        ([1, -1, -1], "#2563eb", r"[1$\bar{1}\bar{1}$]"),
        ([-1, 1, -1], "#16a34a", r"[$\bar{1}$1$\bar{1}$]"),
        ([-1, -1, 1], "#ea580c", r"[$\bar{1}\bar{1}$1]"),
    ]

    for vec, color, label in orientations:
        v = np.array(vec) / np.sqrt(3) * r
        ax1.quiver(0, 0, 0, v[0], v[1], v[2], color=color,
                   arrow_length_ratio=0.15, lw=3, label=label)
        ax1.quiver(0, 0, 0, -v[0], -v[1], -v[2], color=color,
                   arrow_length_ratio=0, lw=2, alpha=0.3)

    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_zlabel("z")
    ax1.set_title("NV Orientations\nin Diamond Lattice", fontsize=13,
                  fontweight="bold")
    ax1.legend(fontsize=9, loc="upper left")
    ax1.set_xlim(-1.2, 1.2)
    ax1.set_ylim(-1.2, 1.2)
    ax1.set_zlim(-1.2, 1.2)

    # ODMR spectrum with 8 peaks
    ax2 = fig.add_subplot(122)
    f = np.linspace(2.5, 3.25, 3000)
    B = 3  # mT
    angles = [0, 54.7, 54.7, 54.7]  # Degrees from B-field direction

    total_signal = np.ones_like(f)
    for angle, (_, color, label) in zip(angles, orientations):
        B_proj = B * np.cos(np.radians(angle))
        splitting = 2 * 28.025e-3 * B_proj
        f_minus = 2.87 - splitting / 2
        f_plus = 2.87 + splitting / 2
        dip1 = lorentzian(f, f_minus, 0.008, 0.04)
        dip2 = lorentzian(f, f_plus, 0.008, 0.04)
        total_signal *= dip1 * dip2
        ax2.axvline(f_minus, color=color, ls=":", alpha=0.4, lw=0.8)
        ax2.axvline(f_plus, color=color, ls=":", alpha=0.4, lw=0.8)

    ax2.plot(f, total_signal, "k-", lw=1.5)
    ax2.set_xlabel("Microwave Frequency (GHz)", fontsize=12)
    ax2.set_ylabel("Fluorescence (norm.)", fontsize=12)
    ax2.set_title("Vector Magnetometry\n(8 dips from 4 orientations)",
                  fontsize=13, fontweight="bold")
    ax2.grid(True, alpha=0.2)
    ax2.set_ylim(0.82, 1.02)

    # Color patches for legend
    patches = [mpatches.Patch(color=c, label=l) for _, c, l in orientations]
    ax2.legend(handles=patches, fontsize=9)

    plt.tight_layout()
    save_fig(fig, "fig5_nv_crystal_orientations")


# =========================================================================
# Figure 6: Temperature Shift
# =========================================================================
def fig6_temperature_shift():
    fig, ax = plt.subplots(figsize=(10, 6))

    f = np.linspace(2.82, 2.92, 2000)
    temps = [
        (300, "#2563eb", "300 K"),
        (350, "#ea580c", "350 K"),
        (400, "#dc2626", "400 K"),
    ]

    shift_rate = -74.2e-6  # GHz/K

    for T, color, label in temps:
        dT = T - 300
        D_shifted = 2.87 + shift_rate * dT
        signal = lorentzian(f, D_shifted, 0.005, 0.15)
        ax.plot(f, signal, color=color, lw=2, label=label)
        ax.axvline(D_shifted, color=color, ls=":", alpha=0.4)

    # Shift arrow
    D_300 = 2.87
    D_400 = 2.87 + shift_rate * 100
    ax.annotate("", xy=(D_400, 0.88), xytext=(D_300, 0.88),
                arrowprops=dict(arrowstyle="<->", lw=2, color="purple"))
    ax.text((D_300 + D_400) / 2, 0.89,
            f"{shift_rate * 100 * 1e3:.1f} MHz\n(100 K shift)",
            fontsize=10, ha="center", color="purple", fontweight="bold")

    ax.set_xlabel("Microwave Frequency (GHz)", fontsize=13)
    ax.set_ylabel("Normalized Fluorescence", fontsize=13)
    ax.set_title("ODMR Temperature Dependence", fontsize=16,
                 fontweight="bold")
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.2)
    ax.set_ylim(0.82, 1.02)

    # Rate box
    props = dict(boxstyle="round", facecolor="#f8fafc", edgecolor="gray")
    ax.text(0.02, 0.02, r"$dD/dT \approx -74.2$ kHz/K",
            transform=ax.transAxes, fontsize=11, va="bottom", bbox=props)

    save_fig(fig, "fig6_temperature_shift")


# =========================================================================
# Main
# =========================================================================
if __name__ == "__main__":
    print("Generating ODMR diagrams...")
    print()

    fig1_energy_levels()
    fig2_odmr_workflow()
    fig3_zeeman_splitting()
    fig4_fluorescence_contrast()
    fig5_nv_crystal_orientations()
    fig6_temperature_shift()

    print()
    print(f"All figures saved to:")
    print(f"  PNG: {PNG_DIR}")
    print(f"  SVG: {SVG_DIR}")
    print(f"  PDF: {PDF_DIR}")
