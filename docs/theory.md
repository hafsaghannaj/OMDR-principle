---
layout: default
title: ODMR Theory
---

# ODMR Theory

## The Nitrogen-Vacancy Center

The NV center in diamond is a point defect consisting of a substitutional nitrogen atom adjacent to a lattice vacancy. In its negatively charged state (NV-), it has 6 electrons forming a spin-1 (S=1) ground state.

## Electronic Structure

### Ground State (3A2)

The ground state is a spin triplet with:
- **|0>** sublevel (ms = 0)
- **|+/-1>** sublevels (ms = +/-1)
- Zero-field splitting **D = 2.87 GHz** separating |0> from |+/-1>

### Excited State (3E)

The excited state is also a spin triplet, reached by 532 nm optical excitation. The excited state has a smaller zero-field splitting of ~1.42 GHz.

### Singlet States

Two singlet states (1A1 and 1E) provide a non-radiative decay pathway:
- Connected by 1042 nm infrared emission
- The intersystem crossing (ISC) rate is **spin-selective**: |+/-1> states decay through the singlet ~10x more than |0>
- The singlet preferentially decays back to |0> in the ground state

## The ODMR Mechanism

### Why ODMR Works

1. **Spin-dependent fluorescence**: |0> emits more red photons (637 nm) than |+/-1>, because |+/-1> has a higher probability of non-radiative decay through the singlet pathway.

2. **Optical spin polarization**: After a few optical cycles, the preferential singlet-to-|0> decay accumulates population in |0>, creating >80% spin polarization without cryogenics.

3. **Microwave-induced contrast**: When microwaves drive the |0> -> |+/-1> transition at resonance (f = D), fluorescence decreases because population moves to the darker |+/-1> state.

## Magnetic Field Sensing

An external magnetic field B along the NV axis causes Zeeman splitting:

**f+/- = D +/- gamma * B**

where gamma = 28.025 GHz/T is the gyromagnetic ratio.

By measuring the resonance frequency shift, the magnetic field can be determined with sensitivities reaching:
- **~1 nT/sqrt(Hz)** for single NV centers
- **~1 pT/sqrt(Hz)** for optimized ensembles

## Temperature Sensing

The zero-field splitting D has a temperature dependence:

**dD/dT = -74.2 kHz/K** (near room temperature)

This enables nanoscale thermometry with ~mK sensitivity by tracking the ODMR resonance frequency shift.

## References

1. Doherty, M.W. et al. "The nitrogen-vacancy colour centre in diamond." Physics Reports 528, 1-45 (2013).
2. Rondin, L. et al. "Magnetometry with nitrogen-vacancy defects in diamond." Reports on Progress in Physics 77, 056503 (2014).
3. Barry, J.F. et al. "Sensitivity optimization for NV-diamond magnetometry." Reviews of Modern Physics 92, 015004 (2020).
