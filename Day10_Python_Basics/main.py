#Exercise 1
def introduction():
    print("My name is Mukti.")
    print("I am learning Python.")
introduction()

#Exercise 2
def greet(name):
    print("Hello", name)
name = input("Enter your Name : ")
greet(name)

#Exercise 3
def square(number):
    print("Square : ", number*number)
number = int(input("Enter a Number : "))
square(number)

#Student Report Function
def student_report(name, age, branch):
    print("-------------------------")
    print("Student Report")
    print("-------------------------")
    print("Name   : ", name)
    print("Age    : ", age)
    print("Branch : ", branch)
    print("-------------------------")
name = input("Enter your Name : ")
age = int(input("Enter your Age : "))
branch = input("Enter your Branch : ")
student_report(name, age, branch)