# Day 13 Notes - Modules and Packages in Python
# Topics Covered
Modules
Importing Modules
Creating Your Own Module
Built-in Modules
Packages
Module Aliases

# 1. What is a Module?
## Definition
A module is a Python file (`.py`) that contains reusable code such as functions, variables, or classes.
Modules help organize code into separate files, making programs easier to read, maintain, and reuse.
Example:
python
# calculator.py
def add(a, b):
    return a + b

# 2. Importing a Module
Modules are imported using the `import` keyword.
## Syntax
python
import module_name
Example:
python
import calculator
print(calculator.add(10, 20))
Output:
text
30

# 3. Importing Specific Functions
Instead of importing the entire module, you can import only the functions you need.
Example:
python
from calculator import add
print(add(5, 3))
Output:
text
8
This makes the code shorter when only a few functions are required.

# 4. Module Aliases
Modules can be imported using an alias with the `as` keyword.
Example:
python
import math as m
print(m.sqrt(25))
Output:
text
5.0
Aliases are useful for long module names.

# 5. Built-in Modules
Python provides many built-in modules that can be used without creating them yourself.
### Math Module
python
import math
print(math.sqrt(81))
print(math.pi)
Useful functions:
`math.sqrt()`
`math.pi`
`math.ceil()`
`math.floor()`
### Random Module
python
import random
print(random.randint(1, 100))
Useful functions:
`random.randint()`
`random.choice()`
`random.shuffle()`

# 6. What is a Package?
A package is a folder that contains one or more Python modules.
Packages help organize larger applications into logical sections.
Example:
text
utilities/
│
├── calculator.py
├── student_utils.py
└── __init__.py

# 7. Programs Built Today
Calculator Module
Math Module Practice
Random Number Generator
Student Utility Module

# 8. Keywords Learned Today
`import`
`from`
`as`