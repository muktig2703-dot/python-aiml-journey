#Exercise 1 
try: 
    a = int(input("Enter a number : "))
    print(a)
except ValueError : 
    print("Please enter a valid number!")

#Exercise 2
try:
    a = int(input("Enter first number : "))
    b = int(input("Enter Second number : "))
    print(a/b)

except ValueError:
    print("Please enter a valid number!")

except ZeroDivisionError:
    print("Cannot be divided by Zero!")

#Exercise 3
try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    print(a*b)
except ValueError: 
    print("Please enter a valid number!")
else: print("Calculation Successful!")

#Safe Student Age Checker
try:
    name = input("Enter your Name : ")
    age = int(input("Enter your Age : "))
except ValueError:
    print("Invalid Age entered!")

else:
    print("Student Information")
    print("Name : ", name)
    print("Age : ", age)