
"""
 ==============================================================
  BioSkillz CodeStart — Python Foundations | Batch 01
  Task 01: Variables, Data Types, Input, Operators & Typecasting
 ==============================================================

 
 Name     : Sania Khalid
 Save as  : sania_khalid_task_01.py 

"""

# # ==============================================================
# # PART A: SESSION EXERCISES
# # ==============================================================

# # --------------------------------------------------------------
# # Exercise 1
# # --------------------------------------------------------------
print (7 / 2) #answer will be 3.5.
print(7 // 2) #the actual answer should be 3.5, but 5 will be roundoff and answer will be 3.
print("7" + "2") #answer will be 72 because i have used "+" in string, which is just write them together.
print(type(7.0)) #7.0 is decimal number, so the correct answer will be float.
print(2 + 3 * 4 ** 2) #here we'll apply BODMAS rule, and the correct answer will be 50.
print(bool("0")) # actually in boolean zero means false, but whenever we write it in quotation marks, it will be true.

""""
# # --------------------------------------------------------------
# # Exercise 2
# # --------------------------------------------------------------
# #  Errors
# #  Name = input("Name: ") #case sensitive error.
# #  print("Hello", name)

# #  age = input("Age: ")   #data type is not mentioned.
# #  print("next year:", age + 1)

# # print("Done   #quotation mark and bracket are not close.
"""

#Errorfree 
name = input("Name:") 
print("Hello", name)

age = int(input("Age: "))
print("next year:", age + 1)

print("Done")

# # --------------------------------------------------------------
# # Exercise 3
# # --------------------------------------------------------------

bill = float(input("Total Bill:"))
print(bill)

friends = int(input("Number of Friends:"))
print(friends)

share = bill / friends  #divide the bill among friends.
print(" Each pays", share)

leftover = bill % friends  #at the end, check remaining amount.
print("Leftover amount is", leftover)



# ==============================================================
# PART B: TASKS
# ==============================================================
""""
# --------------------------------------------------------------
# Task 1: Variables and Data Types
#
# Create four variables about yourself:
#   - your name   (string)
#   - your age    (integer)
#   - your height in metres (float)
#   - whether you are a student (boolean)
#
# Print each value along with its data type using type().
# Add at least one comment explaining your code.
#
# Example output:
#   Ali <class 'str'>
#   22 <class 'int'>
#   1.75 <class 'float'>
#   True <class 'bool'>
# --------------------------------------------------------------
"""
#First I create varaibles, then print it with its data type
name = ("Ali")
age = (22)
height = (1.75)
is_student = True
print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
""""
# --------------------------------------------------------------
# Task 2: Temperature Converter (Input and Typecasting)
#
# Ask the user to enter a temperature in Celsius.
# Convert the input to a float, then calculate and print the
# temperature in Fahrenheit and in Kelvin.
#
#   Fahrenheit = (Celsius * 9 / 5) + 32
#   Kelvin     = Celsius + 273.15
#
# Example output:
#   Enter temperature in Celsius: 37
#   Fahrenheit: 98.6
#   Kelvin: 310.15
# --------------------------------------------------------------
"""
#First I create a variable named celsius then add arthimatic operations that automatically convert fahrenheit and kelvin.
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin     = celsius + 273.15

print("Fahrenheit:" , fahrenheit)
print("Kelvin:" , kelvin)

""""
# --------------------------------------------------------------
# Task 3: Simple Calculator (Arithmetic Operators)
#
# Ask the user to enter two numbers and convert them to floats.
# Print the result of each of these operations:
#   addition, subtraction, multiplication, division,
#   floor division, modulus and exponent (power)
#
# Example output:
#   Enter first number: 17
#   Enter second number: 5
#   Addition: 22.0
#   Subtraction: 12.0
#   Multiplication: 85.0
#   Division: 3.4
#   Floor division: 3.0
#   Modulus: 2.0
#   Power: 1419857.0
# --------------------------------------------------------------
"""
#Create two variables and automatically arthimatic operations will apply on those two numbers which user will write
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

print("Addition:", first + second)
print("Subtractin:", first - second)
print("Multiplication:", first * second)
print("Division:", first / second)
print("Floor Division:", first // second)
print("Modulus:", first % second)
print("Power:", first ** second)
""""
# --------------------------------------------------------------
# Task 4: Savings Tracker (Assignment Operators)
#
# Start with a variable: savings = 1000
# Then update it step by step using assignment operators
# (+=, -=, *=), printing the new value after each step:
#   1. You receive 500 as a gift          (use +=)
#   2. You spend 300 on books             (use -=)
#   3. Your savings double by year end    (use *=)
#
# Example output:
#   Starting savings: 1000
#   After gift: 1500
#   After buying books: 1200
#   After doubling: 2400
# --------------------------------------------------------------
"""
#Here first I create a variable named savings then and applied assignment operator on that variable, which is adding, subracting and multiplying the savings.
savings = 1000
print("After savings:", savings)

savings += 500
print("After gift:", savings)

savings -= 300
print("After buying book:", savings)

savings *= 2
print("After doubling:", savings)



""""
# --------------------------------------------------------------
# Task 5: Scholarship Check (Comparison and Logical Operators)
#
# A student qualifies for a scholarship if:
#   - their marks are 80 or more, AND
#   - their attendance is 75% or more
#
# Ask the user for their marks and attendance (convert both to
# integers). Then print True or False for each check below.
# Do not use if statements; use comparison and logical
# operators only.
#
# Example output:
#   Enter your marks: 85
#   Enter your attendance percentage: 70
#   Marks 80 or more: True
#   Attendance 75% or more: False
#   Qualifies for scholarship: False
# --------------------------------------------------------------
"""
#Create 2 variables, then compare them such as marks should be greater than 80 and atendance should be greater than 75 then user will be qualify for the scholarship otherwise not.
marks = int(input("Enter your marks:"))
attendance = int(input("Enter your attendance:"))

marks_check = marks >= 80
attendance_check = attendance >= 75

scholarship = marks_check and attendance_check

print("Marks 80 or more:", marks_check)
print ("Attendance 75% or more:", attendance_check)
print("Qualifies for scholarship:", scholarship)


