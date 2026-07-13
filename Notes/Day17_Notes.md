# Day 17 Notes - Object-Oriented Programming (OOP): Encapsulation
# Topics Covered
Encapsulation
Public Attributes
Protected Attributes
Private Attributes
Getter Methods
Setter Methods
Student Profile Manager

# 1. What is Encapsulation?
## Definition
Encapsulation is one of the core principles of Object-Oriented Programming (OOP). It refers to the practice of **bundling data (attributes) and methods (functions) together inside a class** while controlling how that data is accessed or modified.
Encapsulation helps protect an object's data from unintended changes and improves the security and maintainability of programs.
Real-world example:
 **Bank Account**
You can check your balance.
You can deposit or withdraw money.
You cannot directly change your balance without using the proper methods.

# 2. Public Attributes
A **public attribute** can be accessed directly from anywhere in the program.
Example:
python
class Student:
    def __init__(self, name):
        self.name = name
student = Student("Mukti")
print(student.name)
Here, `name` is a public attribute.

# 3. Protected Attributes
A **protected attribute** is created by adding a single underscore (`_`) before its name.
Example:
python
class Student:
    def __init__(self, branch):
        self._branch = branch
Although protected attributes can still be accessed directly, they are intended for internal use within the class and its subclasses.

# 4. Private Attributes
A **private attribute** is created by adding double underscores (`__`) before its name.
Example:
python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
Private attributes cannot be accessed directly from outside the class.
Instead, getter and setter methods should be used.

# 5. Getter Methods
A **getter method** returns the value of a private attribute.
Example:
python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
Usage:
python
account = BankAccount(5000)
print(account.get_balance())


# 6. Setter Methods
A **setter method** updates the value of a private attribute in a controlled manner.
Example:
python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def set_balance(self, balance):
        self.__balance = balance
Setter methods can also include validation before updating the value.

# 7. Student Profile Manager
Today, a Student Profile Manager program was created using encapsulation.
The project included:
Public attribute (`name`)
Protected attribute (`branch`)
Private attribute (`age`)
Getter method (`get_age()`)
Setter method (`set_age()`)
Display method
Updating private data using a setter
This project demonstrated how encapsulation protects sensitive information while allowing controlled access.

# 8. Advantages of Encapsulation
Protects important data from direct modification.
Improves data security.
Makes code easier to maintain.
Allows validation before updating values.
Improves code organization.
Encourages better programming practices.

# 9. Keywords Learned Today
Encapsulation
Public Attribute
Protected Attribute
Private Attribute
Getter
Setter