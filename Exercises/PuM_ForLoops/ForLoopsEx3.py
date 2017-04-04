
#Michael Pu
#2016/11/01
#ICS2O1
#Ms.Strelkovska
#For Loops Exercises - 3

#Input
print("Enter two numbers. Press enter after each.")
numInput1 = int(input())
numInput2 = int(input())

num1 = min(numInput1, numInput2)
num2 = max(numInput1, numInput2)

#Calculations
sumNum = 0
print("----------------------")
for x in range(num1, num2+1):
    print(x)
    sumNum = sumNum + x
print("Sum of numbers from %i to %i is %i" %(num1, num2, sumNum))
    






