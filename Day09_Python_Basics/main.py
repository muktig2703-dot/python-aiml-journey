#Exercise 1
student = {
    "name": "Mukti",
    "age": 19,
    "branch": "AI & ML"
}
print(student["name"])
print(student["age"])
print(student["branch"])

#Exercise 2
student["age"] = 20
student["college"] = "MITS"
print(student)

#Exercise 3
print(student.keys())
print(student.values())
print(student.items())

#Student Information System
name = input("ENter your Name : ")
age = int(input("Enter your Age : "))
branch = input("Enter your Branch : ")
college = input("Enter your College : ")
dream_company = input("Enter your Dream Company : ")
student = {
    "name" : name,
    "age"  : age,
    "branch" : branch,
    "college" : college,
    "dream company" : dream_company
}
print("-----------------------------")
print("Student Information")
print("-----------------------------")
print(student)
print("-----------------------------")
print("dictionary keys : ", student.keys())
print("dictionary values : ", student.values())