# Day 05 Notes - Loops in Python (for & while)

# Topics Covered

Loops
for Loop
range() Function
while Loop
Infinite Loops

# 1. What is a Loop?
## Definition
A loop is used to execute the same block of code multiple times without writing it repeatedly.
Instead of writing:
python
print("Hello")
print("Hello")
print("Hello")
We can write:
python
for i in range(3):
    print("Hello")
Loops make programs shorter, cleaner, and more efficient.

# 2. for Loop
## Definition
A `for` loop is used when the number of repetitions is known.
## Syntax
python
for variable in range(number):
    # code
## Example
python
for i in range(5):
    print(i)
Output:

0
1
2
3
4

# 3. range() Function
The `range()` function generates a sequence of numbers.
## a) range(stop)
python
range(5)
Output:
0 1 2 3 4

## b) range(start, stop)
python
range(2, 6)
Output:
2 3 4 5

## c) range(start, stop, step)
python
range(2, 11, 2)
Output:
2 4 6 8 10

# 4. while Loop
## Definition
A `while` loop executes as long as its condition remains `True`.
## Syntax
python
while condition:
    # code
## Example
python
count = 1

while count <= 5:
    print(count)
    count += 1
Output:

1
2
3
4
5

# 5. Infinite Loop
An infinite loop keeps running forever because its condition never becomes `False`.
Wrong:
python
count = 1

while count <= 5:
    print(count)
Correct:
python
count = 1
while count <= 5:
    print(count)
    count += 1
Always update the loop variable inside a `while` loop.

# 6. Programs Built Today
Print numbers from 1 to 10
Print "Python" 5 times
Countdown from 10 to 1
Multiplication Table Generator
Print Even Numbers

# 7. Functions Learned
## range()
Generates a sequence of numbers.
Example:
python
for i in range(1, 6):
    print(i)