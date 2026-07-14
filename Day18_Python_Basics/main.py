#Exercise 1
class Bird:
    def sound(self):
        print("Bird Sound")
class Parrot(Bird):
    def sound(self):
        print("Parrot Talking")
parrot1 = Parrot()
parrot1.sound()

#Exericse 2
class Shape:
    def area(self):
        print("Calculating Area")
class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle = Length × Breadth")
class Circle(Shape):
    def area(self):
        print("Area of Circle = π × r²")
rectangle1 = Rectangle()
circle1 = Circle()
rectangle1.area()
circle1.area()

#Exercise 3
print(len("Artificial Intelligence"))
print(len([10, 20, 30, 40]))

#Employee Management System
class Employee:
    def work(self):
        print("Employee is working.")
class Developer(Employee):
    def work(self):
        print("Developer is writing code.")
class Designer(Employee):
    def work(self):
        print("Designer is creating UI designs.")
developer1 = Developer()
designer1 = Designer()
print("----------------------------")
print("Employee Management System")
print("----------------------------")
developer1.work()
designer1.work()
print("----------------------------")