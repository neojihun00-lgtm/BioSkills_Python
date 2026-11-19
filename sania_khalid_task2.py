#Excercise 1
print("Python"[1:4]) #answer will be yth.
print("banana".count("an")) #answer will be 2 because "an" is mentioned twice.
print ("Hello"[-1]) #answer will be "o" because we count backward here.
print("zebra" < "apple") #answer will be false bacause apple comes before zebra alphabetically.
print(5 > 3 and 2 > 4)  #5 is greater than 3 which is correct but 2 is not greater than 4 which is false. therefore overall answer will be false because i have used "and" means both statements msut be true.
print(not "") #here actual answer should be false because string is empty but "not" will flips the result so answer will be true.

#Excercise 2
#Errors
# marks = int(input("Marks: "))
# if marks >= 50  here colon is missing  
#    print("Pass")
# else:           
# print("Fail")   in if condition we add indentation

# answer = input("Again? ")
# if answer = "yes":         here I'll change = to == "== means both side must be equal to each other" and when it will be yes process will restart
#    print("Restarting...")

#ErrorFree
marks = int(input("Marks: "))
if marks >= 50:
    print("Pass")
else:           
    print("Fail")  

answer = input("Again? ")
if answer =="yes":        
    print("Restarting...")

#Excercise 3
name = input("Student name: ").strip().title() #here I have used "strip" which will remove extra space and "title" will makes the firt letter of each name in uppercase.

marks = input("Marks (0-100): ")

if marks.isdigit(): #here I have used "isdigit" means checks that input contain digits or not.
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
        print(f"{name} scored {marks}/100 → Grade {grade}") #f means formatted string which makes code clean and easy to read.

else:
    print("Please enter marks as a number.")