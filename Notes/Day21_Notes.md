# Day 21 Notes - Working with JSON in Python
# Topics Covered
JSON (JavaScript Object Notation)
Python `json` Module
`json.dumps()`
`json.loads()`
`json.dump()`
`json.load()`
Student JSON Saver Project

# 1. What is JSON?
## Definition
JSON (JavaScript Object Notation) is a lightweight data-interchange format used to store and exchange data between applications.
It is easy for humans to read and write and easy for computers to parse and generate.
JSON is widely used in:
Web APIs
AI applications
Mobile apps
Databases
Configuration files
Cloud services
Example:
json
{
    "name": "Mukti",
    "age": 19,
    "branch": "AI & ML"
}
Although JSON looks similar to a Python dictionary, they are different data types.

# 2. Python `json` Module
Python provides a built-in `json` module for working with JSON data.
Import statement:
python
import json
No additional installation is required.

# 3. `json.dumps()`
The `json.dumps()` function converts a Python object into a JSON string.
Example:
python
import json
student = {
    "name": "Mukti",
    "age": 19
}
json_data = json.dumps(student, indent=4)
print(json_data)

The `indent` parameter formats the JSON output to make it more readable.

# 4. `json.loads()`
The `json.loads()` function converts a JSON string back into a Python object.
Example:
python
import json
json_string = '''
{
    "name": "Mukti",
    "age": 19
}
'''
student = json.loads(json_string)
After conversion, the data behaves like a normal Python dictionary.

# 5. `json.dump()`
The `json.dump()` function writes a Python object directly to a JSON file.
Example:
python
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
This creates or overwrites the JSON file with the provided data.

# 6. `json.load()`
The `json.load()` function reads data from a JSON file and converts it into a Python object.
Example:
python
with open("student.json", "r") as file:
    student = json.load(file)
The returned object can then be accessed like a Python dictionary.

# 7. Student JSON Saver Project
Today's mini project allowed users to:
Enter student details
Store the information in a dictionary
Save the dictionary to a JSON file
Read the same file
Display the stored information
This project demonstrated the complete workflow of reading and writing JSON data.

# 8. Difference Between `dump()` and `dumps()`
| Function       | Purpose                                        |
| -------------- | ---------------------------------------------- |
| `json.dump()`  | Writes a Python object directly to a JSON file |
| `json.dumps()` | Converts a Python object into a JSON string    |

# 9. Difference Between `load()` and `loads()`
| Function       | Purpose                                                          |
| -------------- | ---------------------------------------------------------------- |
| `json.load()`  | Reads JSON data from a file and converts it into a Python object |
| `json.loads()` | Converts a JSON string into a Python object                      |

# 10. Advantages of JSON
Easy to read and write
Lightweight data format
Platform-independent
Supported by almost every programming language
Commonly used for APIs and web applications
Simple way to store structured data

# 11. Keywords Learned Today
JSON
`json`
`dump()`
`dumps()`
`load()`
`loads()`
Dictionary
JSON File
Serialization
Deserialization