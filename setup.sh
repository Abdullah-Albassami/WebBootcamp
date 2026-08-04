#!/bin/zsh

# Make sure we're in the WebBootcamp directory

# Create folders
mkdir project

# Create Files
touch project/main.py project/README.md

# Filling README.md file
echo "
1- created the setup.sh shell script file
2- Accessed the script file using nano
3- Created the commands in order to firstr create the project folder
4- Create two files (main.py, README.md)
5- Documented the steps in the README.md file
6- Initialized git
7- Added Created Files 
7- Commited changes
8- Pushed the project on github 
9- Displayed a success message 
10- Made the script executable using chmod +x setup.sh." >> README.md 

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
