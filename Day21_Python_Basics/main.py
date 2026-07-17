#Exercise 1
import json
student = {
    "name": "Mukti",
    "age": 19,
    "branch": "AI & ML"
}
json_data = json.dumps(student, indent=4)
print(json_data)

#Exercise 2
import json
json_string = '''
{
    "name":"Mukti",
    "age":19,
    "branch":"AI & ML"
}
'''
student = json.loads(json_string)
print(student)
print(student["name"])

#Exercise 3
import json
student = {
    "name": "Mukti",
    "age": 19,
    "branch": "AI & ML"
}
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
print("JSON file created successfully!")

#Student JSON Saver
import json
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
branch = input("Enter your Branch: ")
student = {
    "name": name,
    "age": age,
    "branch": branch
}
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
print("\nStudent data saved successfully!")
with open("student.json", "r") as file:
    student_data = json.load(file)
print("\n----------------------------")
print("Student Details")
print("----------------------------")
print("Name   :", student_data["name"])
print("Age    :", student_data["age"])
print("Branch :", student_data["branch"])
print("----------------------------")