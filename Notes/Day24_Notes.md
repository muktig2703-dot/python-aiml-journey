# Day 24 Notes - Working with the OS Module in Python
# Topics Covered
OS Module
`os.getcwd()`
`os.listdir()`
`os.mkdir()`
`os.path.exists()`
File & Folder Inspector Project

# 1. Introduction to the OS Module
## Definition
The `os` module is a built-in Python module that allows programs to interact with the operating system.
It provides functions to:
Work with files and folders
Create directories
Check whether files or folders exist
Get the current working directory
List files and folders
Perform various operating system tasks
The `os` module is widely used in automation, backend development, scripting, data science, and artificial intelligence projects.

# 2. Importing the Module
To use the `os` module:
python
import os
Since it is a built-in module, no installation is required.

# 3. `os.getcwd()`
The `os.getcwd()` function returns the current working directory.
Example:
python
import os
print(os.getcwd())
Example Output:
text
C:\Users\Mukti\Desktop\python-ai-ml-journey\Day24_OS
This is useful when you want to know where your Python program is currently running.

# 4. `os.listdir()`
The `os.listdir()` function returns a list of all files and folders in the current directory.
Example:
python
import os
items = os.listdir()
for item in items:
    print(item)
Example Output:
text
main.py
README.md
students.csv
MyFolder

# 5. `os.mkdir()`
The `os.mkdir()` function creates a new folder.
Example:
python
import os
os.mkdir("Projects")
If the folder already exists, Python raises a `FileExistsError`.
To avoid this:
python
if not os.path.exists("Projects"):
    os.mkdir("Projects")

# 6. `os.path.exists()`
The `os.path.exists()` function checks whether a file or folder exists.
Example:
python
import os
if os.path.exists("student.json"):
    print("File Exists")
else:
    print("File Not Found")
It returns:
`True` if the path exists
`False` if it does not exist

# 7. File & Folder Inspector Project
Today's mini project allowed users to:
Display the current working directory
List all files and folders
Create a new folder if it did not already exist
Check whether a file exists
This project combined several useful `os` module functions into one practical application.

# 8. Advantages of the OS Module
Built into Python
Easy to use
Helps automate file management
Works across different operating systems
Useful for organizing project files
Essential for scripting and backend development

# 9. Keywords Learned Today
`os`
`os.getcwd()`
`os.listdir()`
`os.mkdir()`
`os.path.exists()`
Directory
File
Folder
Path
Working Directory