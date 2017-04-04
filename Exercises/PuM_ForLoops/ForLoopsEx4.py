
#Michael Pu
#2016/11/01
#ICS2O1
#Ms.Strelkovska
#For Loops Exercises - 4

import random

#Calculations
numList = []

for ranNum in range(0,16):
    numList.append(random.randint(1, 100))

num = 0

for row in range(0,4):
    for col in range(0,4):
        printNum = str(numList[num])
        printNum = printNum.rjust(2)
        print(printNum, end=" ")
        num = num + 1
    print(end="\n")
        
    





