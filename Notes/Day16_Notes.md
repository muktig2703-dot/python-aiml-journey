# Day 16 Notes - Object-Oriented Programming (OOP): Inheritance
# Topics Covered
Inheritance
Parent Class
Child Class
`super()` Function
Method Overriding
Student Management System

# 1. What is Inheritance?
## Definition
Inheritance is an Object-Oriented Programming (OOP) concept that allows one class to inherit the properties and methods of another class.
It promotes **code reusability** by allowing us to write common functionality once and use it in multiple classes.
Example:
python
class Person:
    pass
class Student(Person):
    pass
Here, `Student` inherits from the `Person` class.

# 2. Parent Class
A **Parent Class** (also called a Base Class or Superclass) is the class whose properties and methods are inherited by another class.
Example:
python
class Person:
    def display_name(self):
        print("Mukti")
The `Person` class is the parent class.

# 3. Child Class
A **Child Class** (also called a Derived Class or Subclass) inherits the features of the parent class and can also have its own additional properties and methods.
Example:
python
class Student(Person):
    pass
The `Student` class automatically gets access to the methods defined in the `Person` class.

# 4. The `super()` Function
The `super()` function is used to call methods or constructors from the parent class.
It helps avoid rewriting code and ensures the parent class is properly initialized.
Example:
python
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, branch):
        super().__init__(name)
        self.branch = branch
Here, `super().__init__(name)` calls the constructor of the `Person` class.

# 5. Method Overriding
Method Overriding occurs when a child class provides its own implementation of a method that already exists in the parent class.
Example:
python
class Animal:
    def speak(self):
        print("Animal speaks")
class Cat(Animal):
    def speak(self):
        print("Meow")
When:
python
cat = Cat()
cat.speak()
Output:
text
Meow
The child class method replaces the parent class method.

# 6. Student Management System
Today, a simple Student Management System was created using inheritance.
The program included:
Parent class (`Person`)
Child class (`Student`)
Constructor inheritance using `super()`
Method overriding
User input
Displaying student information
This project demonstrated how inheritance can reduce code duplication while keeping programs organized.

# 7. Advantages of Inheritance
Promotes code reuse.
Reduces duplicate code.
Makes programs easier to maintain.
Organizes code logically.
Supports hierarchical relationships between classes.
Simplifies future modifications and extensions.

# 8. Keywords Learned Today
`class`
Inheritance
Parent Class
Child Class
`super()`
Method Overriding