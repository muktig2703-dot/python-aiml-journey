# Day 26 Notes - Virtual Environments (venv) in Python
# Topics Covered
Virtual Environment
`venv` Module
Creating a Virtual Environment
Activating and Deactivating
Installing Packages
`pip list`
`.gitignore`
Python Environment Checker Project

# 1. What is a Virtual Environment?
## Definition
A virtual environment is an isolated Python environment that allows each project to have its own Python interpreter and installed packages.
It prevents dependency conflicts between different Python projects and keeps project environments organized.
For example:
Project A may require `requests` version 2.28.
Project B may require `requests` version 2.31.
Using separate virtual environments allows both projects to work without interfering with each other.

# 2. Why Use a Virtual Environment?
Virtual environments provide several benefits:
Isolate project dependencies.
Prevent package version conflicts.
Keep the global Python installation clean.
Make projects easier to share with others.
Improve reproducibility across different systems.
Almost every professional Python project uses a virtual environment.

# 3. Creating a Virtual Environment
To create a virtual environment, open a terminal in your project folder and run:
bash
python -m venv venv
This creates a folder named:
text
venv/
The folder contains:
Python executable
Installed packages
Scripts
Configuration files

# 4. Activating the Virtual Environment
### Windows
bash
venv\Scripts\activate
### Linux / macOS
bash
source venv/bin/activate
After activation, the terminal usually displays:
text
(venv)
This indicates that the virtual environment is currently active.

# 5. Installing Packages
Once the virtual environment is active, packages can be installed using `pip`.
Example:
bash
pip install requests
The package is installed only inside the current virtual environment.

# 6. Viewing Installed Packages
Use the following command:
bash
pip list
Example Output:
text
Package      Version
------------ -------
pip          25.x
requests     2.x
urllib3      ...
This command displays all packages installed in the active virtual environment.

# 7. Deactivating the Virtual Environment
To exit the virtual environment, run:
bash
deactivate
The `(venv)` prefix disappears, indicating that the global Python environment is active again.

# 8. `.gitignore`
The `venv` folder should **not** be uploaded to GitHub because:
It is automatically generated.
It contains many unnecessary files.
It increases repository size.
Other developers can recreate it easily.
Create a `.gitignore` file:
text
venv/
Git will ignore the entire virtual environment folder.

# 9. Python Environment Checker Project
Today's mini project displayed useful information about the Python environment.
Example:
python
import sys
print("Python Version :", sys.version)
print("Python Executable :", sys.executable)
It helped verify whether the program was running inside the virtual environment.

# 10. Advantages of Virtual Environments
Separate dependencies for each project.
Avoid package conflicts.
Easy to recreate project environments.
Cleaner project management.
Standard practice in professional Python development.
Improves collaboration in teams.

# 11. Keywords Learned Today
Virtual Environment
`venv`
`pip`
Package
Dependency
Activate
Deactivate
`.gitignore`
`sys`
Python Executable