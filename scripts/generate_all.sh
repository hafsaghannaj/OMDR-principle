#!/bin/bash
set -euo pipefail
echo "=== Generating Python figures ==="
python scripts/generate_figures.py
echo "=== Generating TikZ figures ==="
python scripts/tikz2png.py
echo "=== All figures generated successfully ==="
