#!/usr/bin/env bash
(
  rm -r .venv
  rm .coverage
  rm -r htmlcov
  rm .git/hooks/pre-commit
  find . -name '__pycache__' -exec rm -rv {} \;
  find . -name '*.egg-info' -exec rm -rv {} \;
  find . -name '.pytest_cache' -exec rm -rv {} \;
  rm ./dist -r
) 2>/dev/null

echo Cleaned project
