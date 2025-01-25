#!/usr/bin/env bash

rm -r .venv                                         2>/dev/null
rm .coverage                                        2>/dev/null
rm -r htmlcov                                       2>/dev/null
rm .git/hooks/pre-commit                            2>/dev/null
find . -name '__pycache__' -exec rm -rv {} \;       2>/dev/null
find . -name '*.egg-info' -exec rm -rv {} \;        2>/dev/null
find . -name '.pytest_cache' -exec rm -rv {} \;     2>/dev/null
rm ./*/dist -r                                      2>/dev/null

echo Cleaned project
