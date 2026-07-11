#Exercise 1
class Student:
    pass
student1 = Student()

#Exercise 2 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Mukti", 19)
print(student1.name)
print(student1.age)

#Exercise 3
class Student:
    def __init__(self, name):
        self.name = name
    def introduction(self):
        print("Hello,", self.name)
student1 = Student("Mukti")
student1.introduction()

#Mini Project – Student Class
class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch
    def display(self):
        print("-----------------------")
        print("Student Details")
        print("-----------------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
branch = input("Enter your Branch: ")
student1 = Student(name, age, branch)
student1.display()