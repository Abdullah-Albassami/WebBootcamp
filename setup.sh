#!/bin/zsh

# Make sure we're in the WebBootcamp directory

# Create folders
mkdir project

# Create Files
touch project/ main.py project/README.md

# Filling README.md file
echo "1- created the setup.sh shell script file
2- Accessed the script file using nano
3- Created the commands in order to firstr create the project folder, create two files (main.py, README.md), documented the steps in the README.md file, initialized git, added Created Files, Commited changes, pushed the project on github, displayed a success message, fianlly added excute mode to the script file using chmod +x setup.sh" 

# Initialize Git
git init

# Adding Created Files
git add .

# Commiting changes
git commit -m "Initial Commit"

# Pushing commited changes
git push

# Display completion message
echo "Project setup completed successfully!"
