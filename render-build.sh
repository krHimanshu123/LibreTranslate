#!/usr/bin/env bash
set -euo pipefail
echo "Python version:" $(python -V 2>&1)
python -m pip install --upgrade pip
pip install .
