# Day 23 Notes - Working with CSV Files in Python
# Topics Covered
CSV (Comma-Separated Values)
Python `csv` Module
`csv.writer()`
`csv.reader()`
Writing CSV Files
Reading CSV Files
Appending Data
Student CSV Manager Project

# 1. What is CSV?
## Definition
CSV (Comma-Separated Values) is a simple file format used to store tabular data.
Each line in a CSV file represents one row, and each value is separated by a comma.
Example:
csv id="cvcumr"
Name,Age,Branch
Mukti,19,AI & ML
Rahul,20,CSE
CSV files are widely used because they are lightweight, easy to read, and supported by almost every programming language and spreadsheet application.

# 2. Python `csv` Module
Python provides a built-in `csv` module for reading from and writing to CSV files.
Import statement:
python id="kn6elc"
import csv
No additional installation is required.

# 3. `csv.writer()`
The `csv.writer()` function is used to write data to a CSV file.
Example:
python id="g56mhs"
import csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Branch"])
The `writerow()` method writes a single row to the file.

# 4. `csv.reader()`
The `csv.reader()` function reads data from a CSV file.
Example:
python id="24t4gq"
import csv
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
Each row is returned as a Python list.

# 5. Writing a CSV File
To create a new CSV file:
python id="sxpklv"
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Branch"])
Opening the file with `"w"` mode creates a new file or overwrites an existing one.

# 6. Reading a CSV File
To display all records:
python id="w07s95"
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
This reads every row one by one.

# 7. Appending Data
To add new records without deleting existing data:
python id="x8v7cb"
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Rahul", 20, "CSE"])
The `"a"` mode stands for **append**.

# 8. Student CSV Manager Project
Today's mini project allowed users to:
Create the CSV file if it did not exist.
Write the header row.
Take student details as input.
Append new student records.
Display all stored records.
This project demonstrated practical CSV file management.

# 9. Why Use `newline=""`?
When writing CSV files on Windows, using:
python id="g9v1hs"
newline=""
prevents blank lines from appearing between rows.
It is considered the recommended practice when using the `csv` module.

# 10. Advantages of CSV
Simple and lightweight
Easy to read and edit
Supported by Excel and Google Sheets
Easy to import into databases
Widely used in Data Science and Machine Learning
Can store large amounts of tabular data

# 11. Keywords Learned Today
CSV
`csv`
`csv.writer()`
`csv.reader()`
`writerow()`
Append
Read
Write
Header
Record