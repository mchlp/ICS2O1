#Programming Test 1 - Part 1
#2016/10/18
#ICS2O1
#Michael Pu

#TSUNAMI SPEED PROBLEM

import math
import random

h = int(input("Enter the depth of the water in metres: "))
d = int(input("Enter the distance the tsunami wave will travel in metres: "))

if h <= 0:
    if d <= 0:
        print("\nThe depth and the distance cannot be a negative number or zero.")
    else:
        print("\nThe depth of the water cannot be a negative number or zero.")
elif d <= 0:
    print("\nThe distance cannot be a negative number or zero.")

else:
    time = d/(math.sqrt(9.8*h))
    numHour = int(time//3600)
    leftMin = time%3600
    numMin = int(leftMin//60)
    numSec = int(leftMin%60)
    print("\nThe Tsunami will be there in", numHour, "hour(s)", numMin, "minute(s)", numSec, "seconds(s)")
    
msg = ["Good-Bye", "Bye-Bye", "Bye. Thank you for using our time calculator."]
ranNum = random.randint(0,2)
print(msg[ranNum])
