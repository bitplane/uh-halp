#!/usr/bin/env bash

# Pull Makefile, scripts/ and .github/ from the template repo into the
# current repo, so it can be reviewed with `git diff` and committed by hand.
#
# The repo's PROJECT_NAME line in the Makefile is preserved. Files that only
# exist in this repo (extra scripts, extra workflows) are left alone.
#
# Override the source with TEMPLATE_REPO=<url-or-path> (default: github master).

set -e

TEMPLATE_REPO="${TEMPLATE_REPO:-https://github.com/bitplane/example-python-project.git}"

if [ ! -f Makefile ] || [ ! -d .git ]; then
    echo "Run this from the root of a git repo with a Makefile" >&2
    exit 1
fi

if ! git diff --quiet Makefile scripts .github 2>/dev/null; then
    echo "warning: Makefile/scripts/.github have uncommitted changes; the diff will mix them" >&2
fi

# Remember this repo's identity
project_name=$(sed -n 's/^PROJECT_NAME := //p' Makefile)

# Fetch the template
TMP_DIR=$(mktemp -d)
cleanup() {
    rm -rf "$TMP_DIR"
}
trap cleanup EXIT

echo "Fetching template from $TEMPLATE_REPO..."
git clone --quiet --depth=1 "$TEMPLATE_REPO" "$TMP_DIR"

# Copy template-owned files over ours, leaving repo-specific extras in place
cp "$TMP_DIR/Makefile" Makefile
mkdir -p scripts .github
cp -r "$TMP_DIR/scripts/." scripts/
cp -r "$TMP_DIR/.github/." .github/

# Restore this repo's identity
if [ -n "$project_name" ]; then
    sed -i "s/^PROJECT_NAME := .*/PROJECT_NAME := $project_name/" Makefile
fi

echo "Template applied. Review with: git diff Makefile scripts .github"
