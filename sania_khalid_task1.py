# Excercise 1
print (7 / 2) #answer will be 3.5.
print(7 // 2) #the actual answer should be 3.5, but 5 will be roundoff and answer will be 3.
print("7" + "2") #answer will be 72 because i have used "+" in string, which is just write them together.
print(type(7.0)) #7.0 is decimal number, so the correct answer will be float.
print(2 + 3 * 4 ** 2) #here we'll apply BODMAS rule, and the correct answer will be 50.
print(bool("0")) # actually in boolean zero means false, but whenever we write it in quotation marks, it will be true.


# Excercise 2
#  Errors
#  Name = input("Name: ") #case sensitive error.
#  print("Hello", name)

#  age = input("Age: ")   #data type is not mentioned.
#  print("next year:", age + 1)

# print("Done   #quotation mark and bracket are not close.

#Errorfree 
name = input("Name:") 
print("Hello", name)

age = int(input("Age: "))
print("next year:", age + 1)

print("Done")


#Excercise 3
bill = float(input("Total Bill:"))
print(bill)

friends = int(input("Number of Friends:"))
print(friends)

share = bill / friends  #divide the bill among friends.
print(" Each pays", share)

leftover = bill % friends  #at the end, check remaining amount.
print("Leftover amount is", leftover)