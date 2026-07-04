#Exercise 1
days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(days[0])
print(days[-1])
print(len(days))

#Exercise 2
numbers = (5,10,15,20,25)
print(numbers[0:3])
print(numbers[-2:])

#Exercie 3
fruits = {"Apple","Banana","Mango"}
fruits.add("Orange")
fruits.remove("Banana")
print(fruits)

#Student Subjects Manager
student_subjects=set()
for i in range(5):
    subject = input("Enter a Subject : ")
    student_subjects.add(subject)
print("Student Subjects")
print("Subjects : ", student_subjects)
print("Total Subjects:", len(student_subjects))