class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch
    def display(self):
        print("----------------------------")
        print("Student Details")
        print("----------------------------")
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Branch :", self.branch)
        print("----------------------------")
students = []
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter Student Name: ")
        try:
            age = int(input("Enter Student Age: "))
        except ValueError:
            print("Please enter a valid age!")
            continue
        branch = input("Enter Student Branch: ")
        student = Student(name, age, branch)
        students.append(student)
        print("\nStudent Added Successfully!")
    elif choice == "2":
        if len(students) == 0:
            print("\nNo Students Found.")
        else:
            print("\n===== Student List =====")
            for student in students:
                student.display()
    elif choice == "3":
        search_name = input("Enter Student Name to Search: ")
        found = False
        for student in students:
            if student.name.lower() == search_name.lower():
                print("\nStudent Found!")
                student.display()
                found = True
                break
        if not found:
            print("\nStudent Not Found.")
    elif choice == "4":
        print("\nThank you for using Student Management System!")
        break
    else:
        print("\nInvalid Choice! Please try again.")