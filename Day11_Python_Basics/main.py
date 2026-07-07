#Exercise 1
file = open("hello.txt", "w")
file.write("Hello Python!")
file.close()

#Exercise 2
file = open("hello.txt", "r")
content = file.read()
print(content)
file.close()

#Exercise 3
file = open("hello.txt", "a")
file.write("\nI am learning Python.")
file.close()
file = open("hello.txt", "r")
content = file.read()
print(content)

#Student Record System
name = input("Enter your Name : ")
age = int(input("Enter your Age : "))
branch = input("Enter your Branch : ")
file = open("student_record.txt", "w")
file.write(f"Name : {name}\n")
file.write(f"Age : {age}\n")
file.write(f"Branch : {branch}\n")
file.close()
file = open("student_record.txt", "r")
content = file.read()
print(content)