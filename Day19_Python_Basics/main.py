#Exercise 1
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle")
rectangle1 = Rectangle()
rectangle1.area()

#Exercise 2
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
class Car(Vehicle):
    def move(self):
        print("Car is moving")
car1 = Car()
car1.move()

#Exercise 3
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        print("Payment Successful")
payment1 = UPI()
payment1.pay()

#Employee Role System
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass
class Developer(Employee):
    def work(self):
        print("Developer is writing code.")
class Designer(Employee):
    def work(self):
        print("Designer is creating UI.")
developer1 = Developer()
designer1 = Designer()
print("----------------------------")
print("Employee Role System")
print("----------------------------")
developer1.work()
designer1.work()
print("----------------------------")