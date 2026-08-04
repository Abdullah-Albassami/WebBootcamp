#!/bin/zsh

# Make sure we're in the WebBootcamp directory

# Create folders
mkdir project

# Create Files
touch project/main.py project/README.md

# Filling README.md file
echo "
1. Created the setup.sh shell script file
2. Accessed the script file using nano
3. Created the project folder
4. Created main.py and README.md
5. Documented the steps in README.md
6. Initialized Git
7. Added the created files
8. Committed the changes
9. Pushed the project to GitHub
10. Made setup.sh executable using chmod +x setup.sh" >> project/README.md 

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
