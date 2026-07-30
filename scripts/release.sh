#!/bin/bash

source .venv/bin/activate

# dirty
VERSION=$(grep -E '^version[[:space:]]*=' pyproject.toml | sed -E 's/.*=[[:space:]]*"([^"]+)".*/\1/')
TAG_NAME=$(git describe --exact-match --tags HEAD)

if [[ "$VERSION" != "$TAG_NAME" ]]; then
    echo "Tag and version do not match!"
    echo "Tag: $TAG_NAME, Version: $VERSION"
    exit 1
fi

if [ -z "$PYPI_TOKEN" ]; then
  echo "PYPI_TOKEN is not set. Can't authenticate to upload"
  exit 1
fi

python3 -m twine upload dist/* --user=__token__ --password="$PYPI_TOKEN"
