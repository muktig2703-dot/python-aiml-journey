#Exercise 1
subjects = ["Physics", "Maths", "Python", "AI", "ML"]
print(subjects[0])
print(subjects[-1])
print(len(subjects))

#Exercise 2
marks = [85,92,78,88,95]
print(marks[0])
print(marks[-1])
print(marks[2])

#Exercise 3
languages = ["Python","Java","C++"]
languages.append("JavaScript")
languages.remove("Java")
print(languages)

#Student Marks Manager
student_marks = []
for i in range(5):
    mark=int(input("Enter marks : "))
    student_marks.append(mark)
print("Student Marks ")
print("Marks : ", student_marks)
print("Highest Marks : ", max(student_marks))
print("Lowest Marks : ", min(student_marks))
print("Total Subjects : ", len(student_marks))