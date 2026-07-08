# Day 12 Notes - Exception Handling in Python
# Topics Covered
Exceptions
try Block
except Block
else Block
finally Block
Handling Multiple Exceptions
Common Python Exceptions

# 1. What is Exception Handling?
## Definition
Exception handling is the process of detecting and handling errors that occur while a program is running.
Without exception handling, a program stops immediately when an error occurs.
With exception handling, the program can continue running and display meaningful error messages.

# 2. What is an Exception?
An exception is an error that occurs during the execution of a program.
Example:
python
number = int(input("Enter a number: "))
If the user enters:
text
abc
Python raises:
text
ValueError

# 3. The `try` Block
The `try` block contains the code that may produce an error.
Example:
python
try:
    number = int(input("Enter a number: "))
    print(number)
Python first executes the code inside the `try` block.

# 4. The `except` Block
The `except` block runs only if an exception occurs.
Example:
python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number.")
Instead of crashing, the program displays a friendly message.

# 5. Handling Multiple Exceptions
A program can handle different types of errors separately.
Example:
python
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except ValueError:
    print("Invalid number entered.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")

# 6. The `else` Block
The `else` block executes only if no exception occurs.
Example:
python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", number)

# 7. The `finally` Block
The `finally` block always executes, whether an exception occurs or not.
Example:
python
try:
    print("Program started")
finally:
    print("Program ended")
The `finally` block is commonly used to close files or release resources.

# 8. Common Exceptions
| Exception           | Cause                                                   |
| ------------------- | ------------------------------------------------------- |
| `ValueError`        | Invalid value (e.g., entering text instead of a number) |
| `ZeroDivisionError` | Division by zero                                        |
| `FileNotFoundError` | File does not exist                                     |
| `TypeError`         | Invalid operation between incompatible data types       |
| `IndexError`        | Accessing an invalid list index                         |
| `KeyError`          | Accessing a dictionary key that does not exist          |

# 9. Programs Built Today
Integer Input Validator
Safe Division Program
try-except-else Practice
Safe Student Age Checker

# 10. Keywords Learned Today
`try`
`except`
`else`
`finally`