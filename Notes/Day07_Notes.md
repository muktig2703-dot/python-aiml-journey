# Day 07 Notes - Lists in Python
# Topics Covered
Lists
Creating Lists
List Indexing
Negative Indexing
List Slicing
List Methods
Built-in Functions for Lists

# 1. What is a List?
## Definition
A list is a collection of multiple values stored in a single variable.
Lists are enclosed within square brackets `[]`.
Example:
python
subjects = ["Physics", "Maths", "Python", "AI", "ML"]
Instead of creating many variables, we can store related values in a single list.

# 2. Creating Lists
Examples:
python
numbers = [10, 20, 30, 40]
fruits = ["Apple", "Banana", "Mango"]
mixed_data = ["Mukti", 19, True, 95.5]
A list can contain different data types.

# 3. List Indexing
Just like strings, lists use indexing.
Example:
text
Physics  Maths  Python  AI  ML
0         1      2      3   4
Example:
python
subjects = ["Physics", "Maths", "Python", "AI", "ML"]
print(subjects[0])
Output:
text
Physics
Indexing starts from **0**.

# 4. Negative Indexing
Lists can also be accessed from the end.
Example:
text
Physics  Maths  Python  AI  ML
-5       -4     -3     -2  -1
Example:
python
print(subjects[-1])
Output:
text
ML
Negative indexing is useful when we want the last element without knowing the list length.

# 5. List Slicing
Slicing extracts a portion of a list.
## Syntax
python
list_name[start:end]
Example:
python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
Output:
text
[20, 30, 40]
The start index is included and the end index is excluded.

# 6. Modifying Lists
Lists are mutable, which means they can be changed after creation.
Example:
python
fruits = ["Apple", "Banana", "Mango"]
fruits[1] = "Orange"
print(fruits)
Output:
text
['Apple', 'Orange', 'Mango']

# 7. Common List Methods
## append()
Adds an element to the end of a list.
python
fruits.append("Grapes")
## insert()
Adds an element at a specific position.
python
fruits.insert(1, "Pineapple")
## remove()
Removes an element by value.
python
fruits.remove("Apple")

## pop()
Removes an element by index.
python
fruits.pop()

By default, removes the last element.
## sort()
Sorts the list in ascending order.
python
numbers.sort()

## reverse()
Reverses the list.
python
numbers.reverse()

# 8. Built-in Functions Used with Lists
## len()
Returns the number of items.
python
print(len(subjects))

## max()
Returns the largest value.
python
marks = [85, 92, 78, 88, 95]
print(max(marks))
Output:
text
95
## min()
Returns the smallest value.
python
print(min(marks))
Output:
text
78
## sum()
Returns the sum of all values.
python
print(sum(marks))
Output:
text
438

# 9. Programs Built Today
Subjects List Program
Marks List Program
Language List Modifier
Student Marks Manager

# 10. Functions Learned
`append()`
`insert()`
`remove()`
`pop()`
`sort()`
`reverse()`
`len()`
`max()`
`min()`
`sum()`