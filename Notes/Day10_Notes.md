# Day 10 Notes - Functions in Python
# Topics Covered
Functions
Creating Functions
Calling Functions
Parameters
Return Statement
Functions with Multiple Parameters
Benefits of Functions

# 1. What is a Function?
## Definition
A function is a reusable block of code that performs a specific task.
Instead of writing the same code multiple times, we write it once inside a function and call it whenever needed.
Functions make programs:
Easier to read
Easier to maintain
Reusable
Organized

# 2. Creating a Function
Functions are created using the `def` keyword.
## Syntax
python
def function_name():
    # code
Example:
python
def greet():
    print("Welcome to Python!")


# 3. Calling a Function
A function runs only when it is called.
Example:
python
def greet():
    print("Hello!")
greet()
Output:
Hello!

# 4. Functions with Parameters
Parameters allow us to pass information into a function.
Example:
python
def greet(name):
    print("Hello", name)
greet("Mukti")
Output:
Hello Mukti
A function can have one or more parameters.

# 5. Functions with Multiple Parameters
Example:
python
def student(name, age, branch):
    print(name)
    print(age)
    print(branch)
student("Mukti", 19, "AI & ML")

Parameters make functions flexible and reusable.

# 6. Return Statement
The `return` statement sends a value back from the function.
Example:
python
def square(number):
    return number * number
result = square(8)
print(result)
Output:
64
Unlike `print()`, `return` allows the result to be stored in a variable and used later.

# 7. Difference Between print() and return
| print()                                | return                                                |
| -------------------------------------- | ----------------------------------------------------- |
| Displays output on the screen          | Sends a value back to the caller                      |
| Cannot be reused later                 | Can be stored in a variable                           |
| Mainly used for displaying information | Used when a result is needed for further calculations |

# 8. Programs Built Today
Introduction Function
Greeting Function
Square Calculator Function
Student Report Function

# 9 Functions Learned Today
User-defined functions
Functions with parameters
Functions with multiple parameters
Functions using `return`