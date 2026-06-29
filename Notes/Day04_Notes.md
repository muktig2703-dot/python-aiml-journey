# Day 04 Notes - Conditional Statements (if, elif, else)

## Topics Covered

if statement
if-else statement
if-elif-else ladder
Comparison operators in conditions
Real-life decision making in Python

# 1. Conditional Statements
## Definition
Conditional statements are used to make decisions in Python based on conditions that return True or False.

# 2. if Statement
## Syntax:
python
if condition:
    # block of code

## Example:
python
age = 20
if age >= 18:
    print("You are an adult")

# 3. if-else Statement
## Syntax:
python
if condition:
    # block 1
else:
    # block 2
## Example:
python
age = 16
if age >= 18:
    print("Allowed")
else:
    print("Not allowed")

# 4. if-elif-else Ladder
Used when multiple conditions exist.
## Syntax:
python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
## Example:
python
marks = 85
if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Fail")

# Important Rule
Python checks conditions **top to bottom**.
 First True condition is executed.

# 5. Comparison Operators in Conditions
| Operator | Meaning          |
| -------- | ---------------- |
| ==       | equal            |
| !=       | not equal        |
| >        | greater than     |
| <        | less than        |
| >=       | greater or equal |
| <=       | less or equal    |


# 6. Real-Life Examples
Voting eligibility check
Even or odd number check
Grade system
Login validation (future use)
Age-based decisions

# 7. Programs Built Today

Voting Eligibility Checker
Even/Odd Checker
Positive / Negative / Zero Checker
Student Result System