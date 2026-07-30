#!/usr/bin/env bash

# create the python virtual environment
if [[ ! -d .venv ]]; then
    if command -v uv >/dev/null 2>&1; then
        uv venv
    else
        python3 -m venv .venv
    fi
fi

# activate it
source .venv/bin/activate
