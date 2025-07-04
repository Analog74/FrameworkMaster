#!/bin/sh
# Regenerate DIRECTORY_STRUCTURE.md with the current project tree

tree -a -I ".git" > DIRECTORY_STRUCTURE.md

echo "DIRECTORY_STRUCTURE.md updated. Don't forget to commit and push!"
