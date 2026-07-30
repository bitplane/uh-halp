#!/bin/sh

set -e

# Variables
PROJECT_NAME=$(basename "$(pwd)")
MODULE_NAME=$(echo "$PROJECT_NAME" | tr '-' '_')
REPO_URL="ssh://git@github.com/bitplane/bitplane.net.git"
SRC_PATH="docs"
DEST_PATH="dev/python/$PROJECT_NAME"
COMMIT_MSG="Update $PROJECT_NAME docs"

# Build the pydocs
. .venv/bin/activate

mkdir -p docs/pydoc
cd src
pydoc-markdown -p "$MODULE_NAME" > ../docs/pydoc/index.md
cd ..

# Check out the main website repo
TMP_DIR=$(mktemp -d)

# Cleanup on exit
cleanup() {
    echo "Cleaning up..."
    rm -rf "$TMP_DIR"
}
trap cleanup EXIT

# Clone the repository
echo "Cloning $REPO_URL into $TMP_DIR..."
git clone --depth=1 "$REPO_URL" "$TMP_DIR"

# Set up the destination path
FULL_DEST_PATH="$TMP_DIR/$DEST_PATH"

# Copy files from source to destination
echo "Copying files from $SRC_PATH to $FULL_DEST_PATH..."
mkdir -p "$FULL_DEST_PATH"
cp -r "$SRC_PATH/." "$FULL_DEST_PATH/"

# Remove symlinks in the destination
echo "Removing symlinks in $FULL_DEST_PATH..."
find "$FULL_DEST_PATH" -type l -exec rm {} +

# Replace symlinks with file contents
echo "Replacing symlinks with file contents..."
cd "$SRC_PATH"
find . -type l -exec sh -c 'cat "$1" > "$2/$1"' _ {} "$FULL_DEST_PATH" \;

# Commit and push
echo "Committing and pushing changes..."
cd "$TMP_DIR"
git add "$DEST_PATH"
git commit -m "$COMMIT_MSG"
git push

echo "Docs published!"
