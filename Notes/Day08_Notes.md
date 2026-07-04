# Day 08 Notes - Tuples and Sets in Python
# Topics Covered
Tuples
Creating Tuples
Tuple Indexing
Tuple Slicing
Immutable Nature of Tuples
Sets
Creating Sets
Set Methods
Difference Between List, Tuple, and Set

# 1. What is a Tuple?
## Definition
A tuple is an ordered collection of items that **cannot be modified** after creation.
Tuples are enclosed within parentheses `()`.
Example:
python
subjects = ("Physics", "Maths", "Python", "AI", "ML")
Tuples are useful when the data should remain constant.
Examples:
Days of the week
Months of the year
GPS coordinates
Fixed configuration values

# 2. Creating Tuples
Examples:
python
numbers = (10, 20, 30, 40)
fruits = ("Apple", "Banana", "Mango")
mixed_data = ("Mukti", 19, True, 95.5)
A tuple can store different data types.

# 3. Tuple Indexing
Tuples use indexing just like lists and strings.
Example:
text
Physics  Maths  Python  AI  ML
0         1      2      3   4
Example:
python
subjects = ("Physics", "Maths", "Python")
print(subjects[0])
print(subjects[-1])
Output:
Physics
Python

# 4. Negative Indexing
Negative indexing accesses elements from the end.
Example:
text
Physics  Maths  Python
-3       -2     -1
Example:
python
subjects = ("Physics", "Maths", "Python")
print(subjects[-1])
Output:
Python

# 5. Tuple Slicing
Slicing extracts a portion of a tuple.
## Syntax
python
tuple_name[start:end]
Example:
python
numbers = (5, 10, 15, 20, 25)
print(numbers[0:3])
Output:
(5, 10, 15)
Example:
python
print(numbers[-2:])
Output:
(20, 25)
The starting index is included, while the ending index is excluded.

# 6. Immutable Nature of Tuples
Tuples cannot be modified after creation.
Incorrect:
python
subjects = ("Physics", "Maths")
subjects[0] = "Chemistry"
This produces a `TypeError`.
Use tuples when values should remain unchanged.

# 7. What is a Set?
## Definition
A set is an unordered collection of **unique** values.
Sets are enclosed within curly braces `{}`.
Example:
python
fruits = {"Apple", "Banana", "Mango"}
Sets automatically remove duplicate values.

# 8. Creating Sets
Example:
python
numbers = {10, 20, 30, 40}
Example with duplicates:
python
numbers = {10, 20, 20, 30, 30, 40}
print(numbers)
Output:
{10, 20, 30, 40}

# 9. Empty Set
An empty set is created using:
python
student_subjects = set()
Do **not** use:
python
{}
because {} creates an empty dictionary, not a set.

# 10. Common Set Methods
## add()
Adds an element to a set.
python
fruits.add("Orange")
## remove()
Removes an element from a set.
python
fruits.remove("Banana")
## len()
Returns the number of elements.
python
print(len(fruits))

# 11. Difference Between List, Tuple and Set
| Feature            | List | Tuple | Set  |
| ------------------ | ---- | ----- | ---- |
| Brackets           | `[]` | `()`  | `{}` |
| Ordered            | Yes  | Yes   | No   |
| Mutable            | Yes  | No    | Yes  |
| Duplicates Allowed | Yes  | Yes   | No   |

# 12. Programs Built Today
Days Tuple Program
Number Tuple Slicing
Fruit Set Manager
Student Subjects Manager

# 13. Functions and Methods Learned
add()
remove()
len()