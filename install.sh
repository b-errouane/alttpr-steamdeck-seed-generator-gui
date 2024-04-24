#!/bin/bash
set -e

repo_name="alttpr-steamdeck-seed-generator-gui"

# Check if Git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install Git first."
    exit 1
fi

# Clone or update the Git repository
if [ -d "$repo_name" ]; then
    cd "$repo_name"
    
    if ! git diff-index --quiet HEAD --; then
        echo "Local changes detected. Stashing changes..."
        git stash save "Local changes stashed by installer"
    fi

    git pull origin main --ff-only

    if [ -n "$(git stash list)" ]; then
        echo "Applying stashed changes..."
        git stash pop
    fi
else
    git clone https://github.com/b-errouane/$repo_name.git
    echo "Repository cloned."
    cd "$repo_name"
fi

echo "Installation/Update complete."
