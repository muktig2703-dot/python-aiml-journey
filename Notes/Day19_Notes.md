# Day 19 Notes - Object-Oriented Programming (OOP): Abstraction
# Topics Covered
Abstraction
Abstract Classes
Abstract Methods
ABC Module
`@abstractmethod` Decorator
Employee Role System

# 1. What is Abstraction?
## Definition
Abstraction is one of the four main principles of Object-Oriented Programming (OOP). It is the process of **hiding implementation details** and showing only the essential features of an object.
In abstraction, the user interacts with **what an object does**, not **how it does it**.
### Real-Life Example
🚗 **Car**
When driving a car, you use the steering wheel, accelerator, and brake pedals. You do not need to understand the internal workings of the engine to drive the car.
Similarly, in programming, abstraction hides complex implementation details and exposes only the necessary functionality.

# 2. Abstract Class
An **Abstract Class** is a class that cannot be instantiated (an object cannot be created directly from it).
It acts as a blueprint for other classes.
In Python, abstract classes are created using the **ABC (Abstract Base Class)** module.
Example:
python
from abc import ABC
class Shape(ABC):
    pass

# 3. Abstract Method
An **Abstract Method** is a method that is declared in an abstract class but does not contain any implementation.
Every child class must provide its own implementation of the abstract method.
Example:
python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
Any class inheriting from `Shape` must implement the `area()` method.

# 4. ABC Module
The **ABC** module stands for **Abstract Base Class**.
It provides the tools required to create abstract classes and abstract methods in Python.
Import statement:
python
from abc import ABC, abstractmethod

# 5. `@abstractmethod` Decorator
The `@abstractmethod` decorator is used to declare an abstract method inside an abstract class.
It ensures that every child class implements the required method.
Example:
python
class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle")
If a child class does not implement all abstract methods, Python will not allow an object of that class to be created.

# 6. Employee Role System
Today's mini project demonstrated abstraction using an Employee Role System.
The project included:
Abstract class (`Employee`)
Abstract method (`work()`)
Child class (`Developer`)
Child class (`Designer`)
Different implementations of the `work()` method
This ensured that every employee role had its own implementation of the `work()` method while following the same structure.

# 7. Advantages of Abstraction
Hides unnecessary implementation details.
Makes programs easier to understand.
Improves code organization.
Encourages code consistency.
Makes large projects easier to maintain.
Provides a clear structure for child classes.

# 8. Keywords Learned Today
Abstraction
Abstract Class
Abstract Method
ABC
`@abstractmethod`
Blueprint