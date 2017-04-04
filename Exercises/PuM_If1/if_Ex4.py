
#Michael Pu
#2016/10/05
#ICS2O1
#Ms.Strelkovska
#If/Else Exercises A - 4

#Input
while True:
    try:
        inputstr=input("Enter your first number: ")
        num1 = float(inputstr)
        
        inputstr=input("Enter your second number: ")
        num2 = float(inputstr)
        
        inputstr=input("Enter your third number: ")
        num3 = float(inputstr)
        break
    except ValueError:
        print (inputstr + " is not a valid number. Please enter a number.\n")

#Calculations
if num1 > num2:
    if num1 > num3:
        larNum = num1
    else:
        larNum = num3
else:
    if num2 > num3:
        larNum = num2
    else:
        larNum = num3

#Ouput
print ("The largest number is:", larNum)
