#----FOR loop----
#Exercise 1
for i in range(1,11):
    print(i)

#Exercise 2
for i in range(5):
    print("Python")

#----WHILE loop----
#Exercise 3
count = 10
while count>=1:
    print(count)
    count-=1

#Multiplication Table
num = int(input("Enter a number : "))
for i in range(1,11):
    print(f"{num}x{i} = {num * i}")