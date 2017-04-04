#ICS20
#Demo 15/09
# Ask the user for a number, display a square root of this number and display first and second digits
import math
#input
num=input("Please enter 2-digit number ")
num=int(num)

#calculation
sRoot=math.sqrt(num)
sRoot=round(sRoot,2)
print("The square root is",sRoot)
d1=num//10
d2=num%10

#output
print("The first digit is",d1)
print("The second digit is",d2)
