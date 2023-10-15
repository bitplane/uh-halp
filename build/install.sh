#!/usr/bin/env bash

# activate venv
source .venv/bin/activate

set -e

# install our package
python3 -m pip install ./uh-halp

# let make know that we are installed in user mode
echo Installed normally

touch .venv/.installed
rm .venv/.installed-dev || true

