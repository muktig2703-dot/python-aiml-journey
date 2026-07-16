# Day 20 Notes - Student Management System (Mini Project)
# Topics Covered
Object-Oriented Programming (OOP)
Classes and Objects
Constructors
Methods
Lists of Objects
Menu-Driven Programs
Exception Handling
Searching Data

# 1. Project Overview
Today's project was a **Student Management System**, a menu-driven application that allows users to manage student records.
The project combines multiple Python concepts learned over the previous 19 days into one practical application.
Features include:
Add Student
View Students
Search Student
Exit Program

# 2. Student Class
A class is a blueprint used to create objects.
The `Student` class stores information about each student.
Example:
python
class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch
The constructor (`__init__`) initializes the student's data whenever a new object is created.

# 3. Objects
An object is an instance of a class.
Example:
python
student = Student("Mukti", 19, "AI & ML")
Each object stores its own values for name, age, and branch.

# 4. Methods
Methods are functions defined inside a class.
Example:
python
def display(self):
The `display()` method prints the student's details in a structured format.
Methods help organize code and make it reusable.

# 5. Lists of Objects
Instead of storing dictionaries or tuples, this project stores **Student objects** inside a list.
Example:
python
students = []
New student objects are added using:
python
students.append(student)
This is a common approach used in Object-Oriented Programming.

# 6. Menu-Driven Programs
The project uses an infinite `while` loop to repeatedly display a menu until the user chooses to exit.
Example menu:
text
1. Add Student
2. View Students
3. Search Student
4. Exit
Menu-driven programs are commonly used in command-line applications.

# 7. Searching Data
The project allows users to search for a student by name.
The comparison is made case-insensitive using:
python
student.name.lower() == search_name.lower()
This ensures that different letter cases (uppercase/lowercase) still produce a successful match.

# 8. Exception Handling
The program validates the user's input while entering the student's age.
Example:
python
try:
    age = int(input("Enter Student Age: "))
except ValueError:
    print("Please enter a valid age!")
Exception handling prevents the program from crashing due to invalid input.

# 9. Concepts Used
Today's project combined many Python concepts together:
Classes & Objects
Constructors
Methods
Lists
Loops
Conditional Statements
Exception Handling
Searching
This demonstrates how multiple concepts work together in a real application.

# 10. Advantages of the Project
Organizes student data using classes.
Uses reusable methods.
Provides a user-friendly menu.
Validates user input.
Demonstrates practical use of Object-Oriented Programming.
Easy to expand with additional features.

# 11. Keywords Learned Today
Project
Student Class
Object
Constructor
Method
List of Objects
Menu-Driven Program
Search
Exception Handling