#Exercise 1
class Student:
    def __init__(self, name):
        self.name = name
student1 = Student("Mukti")
print("Name:", student1.name)

#Exercise 2 
class Student:
    def __init__(self, branch):
        self._branch = branch
student1 = Student("AI & ML")
print("Branch:", student1._branch)

#Exercise 3 
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
account = BankAccount(5000)
print("Balance:", account.get_balance())

#Student Profile Manager 
class Student:
    def __init__(self, name, age, branch):
        self.name = name
        self._branch = branch
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        self.__age = new_age
    def display(self):
        print("----------------------------")
        print("Student Profile")
        print("----------------------------")
        print("Name   :", self.name)
        print("Branch :", self._branch)
        print("Age    :", self.get_age())
        print("----------------------------")
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
branch = input("Enter your Branch: ")
student1 = Student(name, age, branch)
student1.display()
new_age = int(input("Enter Updated Age: "))
student1.set_age(new_age)
print("\nUpdated Student Information")
student1.display()