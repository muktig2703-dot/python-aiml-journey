# Day 09 Notes - Dictionaries in Python
# Topics Covered
Dictionaries
Creating Dictionaries
Key-Value Pairs
Accessing Dictionary Values
Updating Dictionary Values
Adding New Key-Value Pairs
Dictionary Methods

# 1. What is a Dictionary?
## Definition
A dictionary is a collection of data stored as **key-value pairs**.
Each key is unique and is used to access its corresponding value.
Dictionaries are enclosed within curly braces `{}`.
Example:
python
student = {
    "name": "Mukti",
    "age": 19,
    "branch": "AI & ML"
}
Here:
`"name"` is the key and `"Mukti"` is the value.
`"age"` is the key and `19` is the value.

# 2. Creating Dictionaries
Example:
python
student = {
    "name": "Mukti",
    "age": 19,
    "college": "MITS"
}
A dictionary can store different data types such as strings, integers, floats, booleans, lists, and even other dictionaries.

# 3. Accessing Values
Dictionary values are accessed using their keys.
Example:
python
print(student["name"])
print(student["age"])
Output:
Mukti
19

# 4. Updating Values
Existing values can be updated by assigning a new value to the key.
Example:
python
student["age"] = 20
print(student)
Output:
{'name': 'Mukti', 'age': 20, 'college': 'MITS'}

# 5. Adding New Key-Value Pairs
New information can be added simply by creating a new key.
Example:
python
student["branch"] = "AI & ML"

Now the dictionary contains an additional key-value pair.

# 6. Common Dictionary Methods
## keys()
Returns all keys in the dictionary.
Example:
python
print(student.keys())
## values()
Returns all values.
Example:
python
print(student.values())
## items()
Returns both keys and values as tuples.
Example:
python
print(student.items())
Output:
dict_items([
('name', 'Mukti'),
('age', 19),
('college', 'MITS')
])
## get()
Safely returns the value of a key.
Example:
python
print(student.get("name"))
Unlike `student["name"]`, `get()` does not produce an error if the key does not exist.

# 7. Programs Built Today
Student Dictionary
Dictionary Update Program
Dictionary Methods Practice
Student Information System

# 8. Functions and Methods Learned
`keys()`
`values()`
`items()`
`get()`
Previously learned functions like `len()` also work with dictionaries.
Example:
python
print(len(student))
This returns the number of key-value pairs.