#Exercise 1
import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Branch"])
    writer.writerow(["Mukti", 19, "AI & ML"])
print("CSV file created successfully!")

#Exercise 2
import csv
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Exercise 3
import csv
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Rahul", 20, "CSE"])
print("New student added successfully!")

#Student CSV Manager
import csv
try:
    with open("students.csv", "r") as file:
        pass
except FileNotFoundError:
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Branch"])
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
branch = input("Enter your Branch: ")
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, age, branch])
print("\nStudent added successfully!")
print("\n----------------------------")
print("Student Records")
print("----------------------------")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
print("----------------------------")