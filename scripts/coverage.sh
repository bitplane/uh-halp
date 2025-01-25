#!/usr/bin/env bash

source .venv/bin/activate

pytest --cov=uh-halp/src --cov-report=html .
