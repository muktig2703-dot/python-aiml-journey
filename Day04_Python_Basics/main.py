#Exercise 1
age = int(input("Enter your Age : "))
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

#Exercise 2
num_1 = int(input("Enter number: "))
if num_1 % 2 == 0:
    print("Even")
else:
    print("Odd")

#Exercise 3
num = int(input("Enter a number : "))
if num > 0:
    print("Number is Positive.")
elif num < 0:
    print("Number is Negative.")
else:
    print("Number is 0.")

#Student Result System
name = input("Enter your Name : ")
marks = int(input("Enter your Marks(out of 100) : "))
print("Name :", name)
print("Marks : ", marks)
if marks >= 90:
    print("Grade : A+")
elif marks >= 75:
    print("Grade : A")
elif marks >= 60:
    print("Grade : B")
elif marks >= 40:
    print("Grade : C")
else:
    print("Fail")