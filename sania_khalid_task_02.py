
"""
==============================================================
 BioSkillz CodeStart — Python Foundations | Batch 01
 Task 02: Strings & Conditional Statements
==============================================================

 Name     : Sania Khalid
 Save as  : sania_khalid_task_02.py 
"""


# ==============================================================
# PART A: SESSION EXERCISES
# ==============================================================

# --------------------------------------------------------------
# Exercise 1
# --------------------------------------------------------------

# 
print("Python"[1:4]) #answer will be yth.
print("banana".count("an")) #answer will be 2 because "an" is mentioned twice.
print ("Hello"[-1]) #answer will be "o" because we count backward here.
print("zebra" < "apple") #answer will be false bacause apple comes before zebra alphabetically.
print(5 > 3 and 2 > 4)  #5 is greater than 3 which is correct but 2 is not greater than 4 which is false. therefore overall answer will be false because i have used "and" means both statements msut be true.
print(not "") #here actual answer should be false because string is empty but "not" will flips the result so answer will be true.

# --------------------------------------------------------------
# Exercise 2
# --------------------------------------------------------------

""""
Errors
marks = int(input("Marks: "))
if marks >= 50  #Here colon is missing  
    print("Pass")
else:           
print("Fail")   #In "if" condition we add indentation

answer = input("Again? ")
if answer = "yes":         #Here I'll change = to == "== means both side must be equal to each other" and when it will be yes process will restart
print("Restarting...")
"""

#ErrorFree
marks = int(input("Marks: "))
if marks >= 50:
     print("Pass")
else:           
     print("Fail")  

answer = input("Again? ")
if answer =="yes":        
  print("Restarting...")


# --------------------------------------------------------------
# Exercise 3
# --------------------------------------------------------------

name = input("Student name: ").strip().title() # strip() removes extra spaces, and title() makes the first letter of each name uppercase.

marks = input("Marks (0-100): ")

if marks.isdigit():  # isdigit() checks whether the input contains digits or not.
    marks = int(marks)

    if marks > 100:
        print("Marks must be 0-100")

    else:
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"

        print(f"{name} scored {marks}/100 → Grade {grade}") # f means formatted string, which makes code clean and easy to read.

else:
    print("Please enter marks as a number.")

# ==============================================================
# PART B: TASKS
# ==============================================================
""""
# --------------------------------------------------------------
# Task 1: Name Formatter (String Methods)
#
# Ask the user to enter their full name. Then print:
#   - the name in uppercase          (use upper())
#   - the name in lowercase          (use lower())
#   - the name in title case         (use title())
#   - the total number of characters, including spaces (use len())
#   - how many times the letter "a" appears (use count())
#
# Example output:
#   Enter your full name: ayesha khan
#   Uppercase: AYESHA KHAN
#   Lowercase: ayesha khan
#   Title case: Ayesha Khan
#   Total characters: 11
#   Number of 'a': 3
# --------------------------------------------------------------
"""
# I created a variable that asks the user to enter their name. then aplied different string methods to
#automatically convert the name into uppercase, lowercase ande count length etc.
name = input("Enter your name:")
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title case:", name.title())
print("Total characters:", len(name))
print("Number of 'a':", name.count("a"))

""""
# --------------------------------------------------------------
# Task 2: Email Breakdown (Indexing and Slicing)
#
# Ask the user to enter an email address. Then print:
#   - the first character               (use indexing)
#   - the last character                (use negative indexing)
#   - the position of "@"               (use find())
#   - the username, the part before "@" (use slicing)
#   - the domain, the part after "@"    (use slicing)
#   - whether it is a Gmail address     (use endswith())
#
# Hint: Save the position of "@" in a variable first, then use
# it inside your slices.
#
# Example output:
#   Enter your email: ali.khan@gmail.com
#   First character: a
#   Last character: m
#   Position of @: 8
#   Username: ali.khan
#   Domain: gmail.com
#   Gmail address: True
# --------------------------------------------------------------
"""
# 
email = input("Enter your email: ")

at_position = email.find("@")

username = email[:at_position]
domain = email[at_position + 1:]

print("First character:", email[0])
print("Last character:", email[-1])
print("Position of @:", at_position)
print("Username:", username)
print("Domain:", domain)
print("Gmail address:", email.endswith("@gmail.com"))

""""
# --------------------------------------------------------------
# Task 3: Report Card (f-strings and Typecasting)
#
# Ask the user for their name and their marks in three
# subjects, each out of 100. Convert the marks to floats.
# Calculate the total and the percentage, then print a short
# report using f-strings. Show the percentage with exactly
# 2 decimal places.
#
#   Percentage = (Total / 300) * 100
#
# Hint: {percentage:.2f} shows a number with 2 decimal places.
#
# Example output:
#   Enter your name: Sara
#   Enter marks for Subject 1: 78
#   Enter marks for Subject 2: 85.5
#   Enter marks for Subject 3: 90
#   ----- Report Card -----
#   Name: Sara
#   Total: 253.5 out of 300
#   Percentage: 84.50%
# --------------------------------------------------------------
"""
# I created few variables to ask for the student name & subject's marks then applied percentage formula which 
# will count the overall percentage of the student. At the end, print all variables to display the student card.
name = input("Enter your name: ")

subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

total = subject1 + subject2 + subject3
percentage = (total / 300) * 100

print("----- Report Card -----")
print(f"Name: {name}")
print(f"Total: {total} out of 300")
print(f"Percentage: {percentage:.2f}%")

""""
# --------------------------------------------------------------
# Task 4: Grade Calculator (if, elif and else)
#
# Ask the user to enter their marks (0 to 100) and convert them
# to an integer. Print their grade using this scale:
#
#   85 to 100  ->  A
#   70 to 84   ->  B
#   55 to 69   ->  C
#   40 to 54   ->  D
#   0 to 39    ->  F
#
# If the marks are below 0 or above 100, print "Invalid marks".
#
# Hint: Check for invalid marks first.
#
# Example output 1:
#   Enter your marks: 72
#   Grade: B
#
# Example output 2:
#   Enter your marks: 105
#   Invalid marks
# --------------------------------------------------------------
"""
# Here I used conditions to check user's marks and assign then suitable grade.
marks = int(input("Enter your marks: "))

# Checking marks and assigning a grade
if marks < 0 or marks > 100:
    print("Invalid marks")

elif marks >= 85:
    print("Grade: A")

elif marks >= 70:
    print("Grade: B")

elif marks >= 55:
    print("Grade: C")

elif marks >= 40:
    print("Grade: D")

else:
    print("Grade: F")

""""
# --------------------------------------------------------------
# Task 5: Login Checker (Nested Conditions)
#
# The correct login details are:
#   username: codestart
#   password: python123
#
# Ask the user for a username and a password.
#   - The username should NOT be case-sensitive, and extra
#     spaces should be ignored. (Use strip() and lower().)
#   - The password IS case-sensitive.
#
# Use a nested if statement:
#   - If the username is correct, check the password:
#       correct password -> "Login successful. Welcome to CodeStart!"
#       wrong password   -> "Incorrect password. Please try again."
#   - If the username is wrong -> "Username not found."
#
# Example output 1:
#   Enter username:   CodeStart
#   Enter password: python123
#   Login successful. Welcome to CodeStart!
#
# Example output 2:
#   Enter username: codestart
#   Enter password: Python123
#   Incorrect password. Please try again.
#
# Example output 3:
#   Enter username: student
#   Enter password: python123
#   Username not found.
# --------------------------------------------------------------
"""
# I Created 2 variables, username and password. I used "strip" & "lower" to remove extra space and convert 
# username into lowercase, also added some conditions that check whether the user entered correct username and password
# if not then display a massage that "incorrect password"
name = input("Enter your name:")
password = input("Enter password: ")


username = username.strip().lower()


if username == "codestart":

    if password == "python123":
        print("Login successful. Welcome to CodeStart!")

    else:
        print("Incorrect password. Please try again.")

else:
    print("Username not found.")
