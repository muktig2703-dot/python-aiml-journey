# Day 18 Notes - Object-Oriented Programming (OOP): Polymorphism
# Topics Covered
Polymorphism
Method Overriding
Built-in Polymorphism
Duck Typing
Employee Management System

# 1. What is Polymorphism?
## Definition
Polymorphism is one of the four main principles of Object-Oriented Programming (OOP). The word **Polymorphism** means **"many forms."**
It allows different classes to have methods with the **same name** but perform **different actions** depending on the object.
Example:
python
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Woof!")
class Cat(Animal):
    def speak(self):
        print("Meow!")
Although all classes use the same method name (`speak()`), each object behaves differently.

# 2. Method Overriding
Method Overriding occurs when a child class provides its own implementation of a method that already exists in the parent class.
Example:
python
class Bird:
    def sound(self):
        print("Bird Sound")
class Parrot(Bird):
    def sound(self):
        print("Parrot Talking")
Calling:
python
parrot = Parrot()
parrot.sound()
Output:
text
Parrot Talking
The child class overrides the parent class method.

# 3. Built-in Polymorphism
Python already provides many examples of polymorphism through built-in functions.
Example:
python
print(len("Artificial Intelligence"))
print(len([10, 20, 30, 40]))
Output:
text
23
4
The same `len()` function works for different data types such as strings, lists, tuples, dictionaries, and sets.

# 4. Duck Typing
Python follows the concept of **Duck Typing**.
The idea is:
> "If it walks like a duck and quacks like a duck, treat it like a duck."
Python focuses on **what an object can do**, rather than what type it is.
Example:
python
class Dog:
    def speak(self):
        print("Woof!")
class Cat:
    def speak(self):
        print("Meow!")
def make_sound(animal):
    animal.speak()
make_sound(Dog())
make_sound(Cat())
Both objects work because they provide a `speak()` method.

# 5. Employee Management System
Today's mini project demonstrated polymorphism using inheritance.
The project included:
Parent class (`Employee`)
Child classes (`Developer` and `Designer`)
Method overriding using `work()`
Different outputs from the same method name
This showed how different objects can respond differently to the same method call.

# 6. Advantages of Polymorphism
Makes programs flexible and reusable.
Reduces code duplication.
Improves readability.
Makes it easy to extend programs by adding new classes.
Allows the same interface to work with different object types.
Supports cleaner and more maintainable code.

# 7. Keywords Learned Today
Polymorphism
Method Overriding
Parent Class
Child Class
Duck Typing
Built-in Polymorphism