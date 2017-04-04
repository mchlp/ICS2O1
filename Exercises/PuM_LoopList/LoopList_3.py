
#Michael Pu
#2016/11/21
#ICS2O1
#Ms.Strelkovska
#Looping Through Lists Exercises 3 

import random
numList = []

for i in range(random.randint(3,10)):
    numList.append(random.randint(3,9))

for item in numList:
    print("*"*item)
