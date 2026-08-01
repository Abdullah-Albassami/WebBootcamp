#!/bin/zsh

# Make sure we're in the WebBootcamp directory

# Create folders
mkdir -p src tests

# Create Files
touch main.py README.md

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requests
python -m pip install requests

# Initialize Git
git init

# Display completion message
echo "Project setup completed successfully!"
