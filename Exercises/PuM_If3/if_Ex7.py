
#Michael Pu
#2016/10/12
#ICS2O1
#Ms.Strelkovska
#If/Else Exercises C - 7

import datetime

#Input
sec = int(input("Enter a number of seconds: "))
#Calculations
time = datetime.datetime.fromtimestamp(sec)
timedelta = datetime.timedelta(seconds = sec)
if sec < 60:
    #print (time.strftime("%S"))
    print (timedelta.seconds)
elif sec > 59 and sec <= 3599:
    print (time.strftime("%M:%S"))
elif sec > 3599 and sec <= 86399:
    print (time.strftime("%I:%M:%S"))
elif sec > 86399:
    print (str(timedelta.days) + " days, " + time.strftime("%I:%M:%S"))

