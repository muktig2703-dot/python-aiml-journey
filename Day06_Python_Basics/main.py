#Exercise 1
name= "Mukti Gupta"
print(name[0])
print(name[-1])
print(len(name))

#Exercise 2
name = input("Ente your name : ")
print(name.upper())
print(name.lower())

#Exercise 3
college = "Madhav Institute of  Technology & Science"
print(college[0:6])
print(college[-7:])

#Student Profile Formatter
name = input("Enter your Name : ")
college = input("Enter your College : ")
branch = input("Enter your Branch : ")
print("-------------------------------------")
print("Student Profile")
print("-------------------------------------")
print("Name           : ", name)
print("College        : ", college)
print("Branch         : ", branch)
print("Uppercase Name : ", name.upper())
print("Lowercase Name : ", name.lower())
print("Name length    :", len(name))
print("-------------------------------------")