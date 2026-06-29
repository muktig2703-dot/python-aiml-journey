#Exercise 1 
num_1 = int(input("Enter First number : "))
num_2 = int(input("Enter Second number : "))
total = num_1 + num_2
diff = num_1 - num_2
prod = num_1 * num_2
div = num_1 / num_2
floor_div = num_1 // num_2
mod = num_1 % num_2
power = num_1 ** num_2 
print(f"The sum is            :  {total}")
print(f"The difference is     :  {diff}")
print(f"The product is        :  {prod}")
print(f"The division is       :  {div}")
print(f"The floor division is :  {floor_div}")
print(f"The modulus is        :  {mod}")
print(f"The power is          :  {power}")

#Exercise 2
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print("Is", num1, "greater than", num2, "?")
print(num1>num2)
print(num1<num2)
print(num1==num2)
print(num1!=num2)

#Exercise 3
age = int(input("Enter your age : "))
salary = int(input("Enter your salary : "))
print("Age above 18?")
print(age>18)
print("Salary above 50000?")
print(salary>50000)

#Student Marks Calculator
name = input("Enter your name : ")
maths_marks = int(input("Enter your marks in Maths: "))
physics_marks = int(input("Enter your marks in Physics : "))
chemistry_marks = int(input("Enter your marks in Chemistry : "))
total_marks = maths_marks + physics_marks + chemistry_marks
avg_marks = (maths_marks + physics_marks + chemistry_marks)/3
percentage = (total_marks/300)*100
print("---------------------------------")
print("Student Report Card")
print("---------------------------------")
print("Name       : ", name)
print("Math       : ", maths_marks)
print("Physics    : ", physics_marks)
print("Chemistry  : ", chemistry_marks)
print("Total      : ", total_marks)
print("Average    : ", avg_marks)
print("Percentage : ", percentage)
print("---------------------------------")