# Day 11 Notes - File Handling in Python
# Topics Covered
File Handling
Opening Files
File Modes
Writing to Files
Reading Files
Appending Data
Closing Files
`with open()` Statement

# 1. What is File Handling?
## Definition
File handling allows a Python program to create, read, write, update, and manage files stored on a computer.

Unlike variables, data stored in a file remains available even after the program ends.
File handling is widely used for storing records, reading datasets, writing logs, and saving program outputs.

# 2. Opening a File
Files are opened using the `open()` function.
## Syntax
python
file = open("filename.txt", "mode")
Example:
python
file = open("student.txt", "w")
`"student.txt"` is the file name.
`"w"` is the file mode.

# 3. File Modes
| Mode  | Description                                                        |
| ----- | ------------------------------------------------------------------ |
| `"r"` | Read a file                                                        |
| `"w"` | Write to a file (creates a new file or overwrites an existing one) |
| `"a"` | Append data to an existing file                                    |
| `"x"` | Create a new file (fails if the file already exists)               |

# 4. Writing to a File
The `write()` method writes text into a file.
Example:
python
file = open("hello.txt", "w")
file.write("Hello Python!")
file.close()
If the file does not exist, Python creates it automatically.

# 5. Reading a File
The `read()` method reads the complete contents of a file.
Example:
python
file = open("hello.txt", "r")
content = file.read()
print(content)
file.close()
Output:
text
Hello Python!

# 6. Appending Data
Append mode (`"a"`) adds new content without deleting the existing content.
Example:
python
file = open("hello.txt", "a")
file.write("\nI am learning Python.")
file.close()
The previous content remains unchanged.

# 7. Closing a File
Files should always be closed after use.
Example:
python
file.close()
Closing a file releases system resources and ensures that all data is properly saved.

# 8. Using `with open()` (Best Practice)
Instead of manually opening and closing a file, Python provides the `with` statement.
Example:
python
with open("hello.txt", "r") as file:
    print(file.read())
Advantages:
Automatically closes the file.
Cleaner and shorter code.
Prevents resource leaks if an error occurs.

# 9. Programs Built Today
Hello File Writer
Hello File Reader
File Append Program
Student Record System

# 10. Functions and Methods Learned
`open()`
`read()`
`write()`
`close()`