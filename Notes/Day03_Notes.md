# Day 03 Notes - Operators in Python

## Topics Covered
Arithmetic Operators
Comparison Operators
Logical Operators
Assignment Operators
Operator Precedence

# 1. Operators
## Definition
Operators are special symbols used to perform operations on variables and values.
Example:
python
a = 10
b = 5
print(a + b)
Output:
15

# 2. Arithmetic Operators
Arithmetic operators perform mathematical calculations.

| Operator | Meaning             | Example      |
| -------- | ------------------- | ------------ |
| +        | Addition            | 5 + 3 = 8    |
| -        | Subtraction         | 5 - 3 = 2    |
| *        | Multiplication      | 5 * 3 = 15   |
| /        | Division            | 10 / 2 = 5.0 |
| //       | Floor Division      | 10 // 3 = 3  |
| %        | Modulus (Remainder) | 10 % 3 = 1   |
| **       | Exponent (Power)    | 2 ** 3 = 8   |
Example:
python
a = 15
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# 3. Comparison Operators
Comparison operators compare two values and always return either `True` or `False`.
| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not Equal to             |
| >        | Greater than             |
| <        | Less than                |
| >=       | Greater than or Equal to |
| <=       | Less than or Equal to    |
Example:
python
print(10 > 5)
print(10 == 5)
Output:
True
False

# 4. Logical Operators
Logical operators combine multiple conditions.
### and
Returns True only if both conditions are true.
python
age = 20
print(age > 18 and age < 30)
Output:
True

### or
Returns True if at least one condition is true.
python
print(5 > 10 or 5 < 10)
Output:
True

### not
Reverses the result.
python
print(not True)
Output:
False

# 5. Assignment Operators
Assignment operators update variable values.
Example:
python
x = 10
x += 5
print(x)
Output:
15

Other assignment operators:
python
x -= 2
x *= 3
x /= 2

# 6. Operator Precedence
Python follows the order of operations (similar to BODMAS).
Example:
python
print(2 + 3 * 4)
Output:
14
Because multiplication happens before addition.
Using parentheses:
python
print((2 + 3) * 4)
Output:
20

# 7. Programs Created Today
Arithmetic Calculator
Comparison Checker
Age & Salary Checker
Student Marks Calculator