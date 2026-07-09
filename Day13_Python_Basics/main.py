#Exercise 1
import calculator
result = calculator.add(10,20)
print(result)

#Exercise 2
import math
print(math.sqrt(64))
print(math.pi)

#Exercise 3
import random
print(random.randint(1, 100))

#Student Utility Module
import student_utils
name = input("Enter your Name : ")
age = int(input("Enter your Age : "))
branch = input("Enter your Branch : ")
student_utils.display_students(name, age, branch)