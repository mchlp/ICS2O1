
#Michael Pu
#2016/10/05
#ICS2O1
#Ms.Strelkovska
#Nested If/Else Exercises - 3

import random

#Input
num = random.randint(-3,3)

#Calculations
print ("Random number is", num)

if num > 0 or num < 0:
    if num > 0:
        print ("Positive Number")
    else:
        print ("Negative Number")
else:
    print ("Zero")

