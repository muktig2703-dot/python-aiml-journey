#Exercise 1
from datetime import datetime
now = datetime.now()
print("Current Date & Time:")
print(now)

#Exercise 2
from datetime import date
today = date.today()
print("Today's Date:")
print(today)

#Exercise 3
from datetime import datetime
now = datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%I:%M:%S %p"))

#Exercise 4
from datetime import datetime
birthday = datetime(2007, 3, 27)
print(birthday)

#Student Age Calculator
from datetime import datetime
now = datetime.now()
name = input("Enter your Name: ")
birth_year = int(input("Enter your Birth Year: "))
current_year = now.year
age = current_year - birth_year
print("----------------------------")
print("Student Details")
print("----------------------------")
print("Name         :", name)
print("Birth Year   :", birth_year)
print("Current Age  :", age)
print("Today's Date :", now.strftime("%d-%m-%Y"))
print("Current Time :", now.strftime("%I:%M %p"))
print("----------------------------")