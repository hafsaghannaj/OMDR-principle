---
layout: default
title: Experimental Setup
---

# Building an ODMR Setup

## Required Components

### Optical

| Component | Specification | Purpose |
|-----------|--------------|---------|
| Laser | 532 nm, >50 mW | NV excitation |
| Dichroic mirror | 560 nm longpass | Separate excitation/emission |
| Emission filter | 650-800 nm bandpass | Isolate NV fluorescence |
| Objective | 40x-100x, NA > 0.7 | Focus/collect light |
| Photodetector | APD or PMT | Single-photon counting |

### Microwave

| Component | Specification | Purpose |
|-----------|--------------|---------|
| MW source | 2.5-3.5 GHz, >10 dBm | Drive spin transitions |
| Amplifier | 30-40 dB gain | Sufficient MW power |
| Antenna | 20 um wire loop or CPW | Deliver MW to NV |

### Sample

| Component | Specification | Purpose |
|-----------|--------------|---------|
| Diamond | Type Ib or CVD with NV | Sensing element |
| Typical [NV] | 1-100 ppm (ensemble) | Trade-off: signal vs linewidth |

## Basic ODMR Measurement Protocol

1. **Align** the laser onto the diamond sample (or single NV)
2. **Optimize** the collection path for maximum fluorescence
3. **Sweep** the microwave frequency from ~2.7 to ~3.1 GHz
4. **Record** fluorescence intensity at each frequency
5. **Identify** the dip(s) in the fluorescence spectrum
6. **Apply** a known magnetic field to verify Zeeman splitting

## Tips for Good ODMR Contrast

- Use sufficient laser power for full optical polarization (~1 mW at focus)
- Ensure MW delivery is efficient (loop antenna close to NV, impedance matched)
- Average over many sweeps to improve SNR
- Use lock-in detection for best sensitivity
- Shield from stray magnetic fields for narrow linewidths
