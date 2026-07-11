# Day 15 Notes - Object-Oriented Programming (OOP): Classes & Objects
# Topics Covered
Object-Oriented Programming (OOP)
Classes
Objects
Constructor (`__init__`)
`self` Keyword
Methods
Creating Objects
Student Class Mini Project

# 1. What is Object-Oriented Programming (OOP)?
## Definition
Object-Oriented Programming (OOP) is a programming paradigm that organizes code using **classes** and **objects**.
Instead of writing only functions, OOP allows us to create blueprints (classes) and build objects from them.
Real-world examples include:
Car
Mobile Phone
Student
Bank Account
Each object has **attributes (data)** and **methods (behavior)**.

# 2. What is a Class?
A **class** is a blueprint used to create objects.
It defines the properties and behaviors that objects created from it will have.
Example:
python
class Student:
    pass
The `pass` keyword creates an empty class.

# 3. What is an Object?
An **object** is an instance of a class.
Once a class is created, multiple objects can be created from it.
Example:
python
class Student:
    pass
student1 = Student()
Here, `student1` is an object of the `Student` class.

# 4. Constructor (`__init__`)
A constructor is a special method that is automatically called whenever an object is created.
It is used to initialize the object's data.
Example:
python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
When an object is created:
python
student1 = Student("Mukti", 19)
the constructor automatically stores the values inside the object.

# 5. The `self` Keyword
`self` refers to the current object.
It is used to access the object's attributes and methods.
Example:
python
self.name = name
Here:
`self.name` → Attribute of the object
`name` → Value passed to the constructor

# 6. Methods
A **method** is a function defined inside a class.
Methods describe what an object can do.
Example:
python
class Student:
    def introduction(self):
        print("Hello")
Calling the method:
python
student1.introduction()
Output:
text
Hello

# 7. Programs Built Today
Student Class
Constructor Practice
Introduction Method
Student Information Display Project

# 8. Advantages of OOP
Organizes code efficiently
Makes programs easier to maintain
Encourages code reuse
Improves readability
Suitable for large software projects
Models real-world objects naturally

# 19. Keywords Learned Today
`class`
`object`
`__init__`
`self`