
#Michael Pu
#2016/10/25
#ICS2O1
#Ms.Strelkovska
#ASCII Loops Exercises - 1

import random

#Input
students = int(input("How many students are in your class: "))

#Calculations

markList = ["A", "B", "B", "C", "D"]

print()

for a in range(1, students+1):
    mark = random.choice(markList)
    print("%3i.\t%s" %(a, mark))





