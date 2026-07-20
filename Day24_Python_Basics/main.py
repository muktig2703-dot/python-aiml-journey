#Exercise 1 
import os
print("Current Working Directory:")
print(os.getcwd())

#Exercise 2
import os
items = os.listdir()
print("Files and Folders:")
for item in items:
    print(item)

#Exercise 3
import os
os.mkdir("MyFolder")
print("Folder created successfully!")

#Exercise 4
import os
if os.path.exists("student.json"):
    print("File exists.")
else:
    print("File not found.")

#File & Folder Inspector
import os
print("----------------------------")
print("Current Directory")
print("----------------------------")
print(os.getcwd())
print("\n----------------------------")
print("Files & Folders")
print("----------------------------")
items = os.listdir()
for item in items:
    print(item)
folder_name = input("\nEnter Folder Name: ")
if os.path.exists(folder_name):
    print("Folder already exists!")
else:
    os.mkdir(folder_name)
    print("Folder created successfully!")
file_name = input("\nEnter Filename: ")
if os.path.exists(file_name):
    print("File Found!")
else:
    print("File Not Found!")