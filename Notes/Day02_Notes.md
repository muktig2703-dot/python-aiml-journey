# Day 02 Notes - User Input & Type Conversion

## Topics Covered
input()
Type Conversion
int()
float()
str()
User Interaction

# 1. input()
## Definition
The input() function is used to take input from the user through the keyboard.
### Syntax
python
variable = input("Message")
### Example
python
name = input("Enter your name: ")
print(name)

# 2. How input() Works
1. Program displays a message.
2. User enters a value.
3. Python stores the value.
4. Program continues execution.
Example:
python
city = input("Enter your city: ")
print(city)

# 3. Important Point
input() always returns a string (`str`).
Example:
python
age = input("Enter your age: ")
print(type(age))
Output:
<class 'str'>
Even if the user enters:
19
Python stores it as:
python
"19"

# 4. Type Conversion
Type conversion changes one data type into another.
### int()
Converts a string into an integer.
python
age = int(input("Enter your age: "))
### float()
Converts a string into a decimal number.
python
height = float(input("Enter your height: "))
### str()
Converts a value into a string.
python
number = 25
text = str(number)

# 5. Why Type Conversion is Needed
Without conversion:
python
age = input("Age: ")
age is a string.
This causes problems during calculations.
Wrong:
python
age = input("Age: ")
print(age + 5)
Correct:
python
age = int(input("Age: "))
print(age + 5)

# 6. Programs Created Today
User Introduction
Next Year Age Calculator
Student Registration Form

# 7. Common Mistakes
Forgetting to use `int()` before calculations.
Using `input()` and expecting numbers automatically.
Giving variables the same names as Python built-in functions.
Example:
python
sum = 10
Better:
python
total = 10

# 8. Best Practices
Use meaningful variable names.
Use `snake_case` for variables.
Use `f-strings` for printing whenever possible.
Convert user input to the correct data type before performing calculations.

# 9. New Functions Learned
## input()
Purpose:
Takes input from the user.
Example:
python
name = input("Enter your name: ")
## int()
Purpose:
Converts a value to an integer.
Example:
python
age = int(input("Enter age: "))
## float()
Purpose:
Converts a value to a decimal number.
Example:
python
salary = float(input("Enter salary: "))