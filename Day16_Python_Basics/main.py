# Exercise 1
class Person:
    def display_name(self):
        print("Name: Mukti")
class Student(Person):
    pass
student1 = Student()
student1.display_name()

#Exercise 2
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, branch):
        super().__init__(name)
        self.branch = branch
student1 = Student("Mukti", "AI & ML")
print("Name:", student1.name)
print("Branch:", student1.branch)

# Exercise 3
class Animal:
    def speak(self):
        print("Animal speaks")
class Cat(Animal):
    def speak(self):
        print("Meow")
cat1 = Cat()
cat1.speak()

#Student Management System
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Student(Person):
    def __init__(self, name, age, branch):
        super().__init__(name, age)
        self.branch = branch
    def display(self):
        print("--------------------------")
        print("Student Details")
        print("--------------------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)
        print("--------------------------")
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
branch = input("Enter your Branch: ")
student1 = Student(name, age, branch)
student1.display()