#Exercise 1
name = input("Enter your Name : ")
age = input("Enter your Age : ")
favourite_programming_language = input("Enter your favourite programming language : ")
print("Hello", name)
print("You are", age, "years old.")
print("Your favourite programming language is", favourite_programming_language)

#Exercise 2
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
total = num_1 + num_2
difference = num_1 - num_2
product = num_1 * num_2
division = num_1/num_2
print("Sum : ", total)
print("Difference : ", difference)
print("Product : ", product)
print("Division : ", division)

#Exercise 3
name = input("Enter your Name : ")
age = int(input("Enter your age : "))
next_age = age + 1
print("Hello", name)
print("Next year you will be", next_age , "years old.")

#Student Registration Form
name = input("Enter your Name : ")
age = int(input("Enter your Age : "))
college = input("Enter your College name : ")
branch = input("Enter your Branch name : ")
favourite_subject = input("Enter your Favourite Subject : ")
dream_company = input("Enter your Dream Company : ")
print("------------------------------------")
print("Student Registration Details")
print("------------------------------------")
print("Name              : ", name)
print("Age               : ", age)
print("College           :", college)
print("Branch            : ", branch)
print("Favourite Subject : ", favourite_subject)
print("Dream Company     : ", dream_company)
print("------------------------------------")
print("Registration Successful!")
print("Welcome to the Python AI & ML Python Bootcamp!")