#!/usr/bin/env bash
source .venv/bin/activate
set -e

if command -v uv >/dev/null 2>&1; then
    PIP="uv pip"
else
    PIP="python3 -m pip"
fi

$PIP install .

echo Installed normally
touch .venv/.installed
rm .venv/.installed-dev 2>/dev/null || true
