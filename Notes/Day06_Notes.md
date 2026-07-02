# Day 06 Notes - Strings in Python
# Topics Covered
Strings
String Indexing
Negative Indexing
String Slicing
String Methods
String Length

# 1. What is a String?
## Definition
A string is a sequence of characters enclosed within single quotes (`' '`) or double quotes (`" "`).
Examples:
python
name = "Mukti"
college = 'MITS'
Strings can contain letters, numbers, spaces, and special characters.

# 2. Creating Strings
Strings can be created using either single or double quotes.
Example:
python
language = "Python"
subject = 'Artificial Intelligence'
Both are valid in Python.

# 3. String Indexing
Each character in a string has an index (position).
Example:
text
M  u  k  t  i
0  1  2  3  4
Example:
python
name = "Mukti"
print(name[0])
print(name[2])
Output:
M
k
Indexing always starts from **0**.

# 4. Negative Indexing
Python also allows indexing from the end of the string.
Example:
text
M  u  k  t  i
-5 -4 -3 -2 -1
Example:
python
name = "Mukti"
print(name[-1])
Output:
i
Negative indexing is useful when you want the last characters without knowing the string length.

# 5. String Slicing
Slicing extracts a part of a string.
## Syntax
python
string[start:end]
The **start index is included**, but the **end index is excluded**.
Example:
python
word = "Python"
print(word[0:3])
Output:
Pyt
Example:
python
print(word[2:6])
Output:
thon
Using negative slicing:
python
print(word[-3:])

Output:
hon

# 6. Common String Methods
## len()
Returns the number of characters in a string.
python
name = "Mukti"
print(len(name))
Output:
5
## upper()
Converts all characters to uppercase.
python
print(name.upper())
Output:
MUKTI
## lower()
Converts all characters to lowercase.
python
print(name.lower())
Output:
mukti
## strip()
Removes spaces from the beginning and end of a string.
python
text = "  Python  "
print(text.strip())
Output:
Python
## replace()
Replaces one part of a string with another.
python
sentence = "I like Java"
print(sentence.replace("Java", "Python"))
Output:
I like Python

# 7. Programs Built Today
Character Index Finder
Name Case Converter
String Slicing Practice
Student Profile Formatter

# 8. Functions Learned
## len()
Returns the length of a string.
## upper()
Converts a string to uppercase.
## lower()
Converts a string to lowercase.
## strip()
Removes leading and trailing spaces.
## replace()
Replaces part of a string with another string.