#!/usr/bin/env bash
source .venv/bin/activate
set -e

if command -v uv >/dev/null 2>&1; then
    PIP="uv pip"
else
    PIP="python3 -m pip"
fi

$PIP install -e .[dev]

echo "Installed in dev mode"
touch .venv/.installed-dev
rm .venv/.installed 2>/dev/null || true
