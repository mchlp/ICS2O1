
#Michael Pu
#2016/09/13
#ICS2O1
#Ms.Strelkovska
#Unit 1 - Ex 3

import datetime

##INPUT
#Set Start Time
startTime = datetime.datetime(1,1,1,6,52,00)
#Set Speeds
easyPaceSpeed = datetime.timedelta(minutes = 6, seconds = 15)
tempoPaceSpeed = datetime.timedelta(minutes = 5, seconds = 32)
#Get User Input
easyPaceDis = int(input("Enter the distance you will run at an easy pace: "))
tempoPaceDis = int(input("Enter the distance you will run at an tempo pace: "))

##CALCULATIONS
#Calculate Time
easyPaceTime = easyPaceDis * easyPaceSpeed
tempoPaceTime = tempoPaceDis * tempoPaceSpeed
finishTime = (startTime + easyPaceTime + tempoPaceTime)
startDate = startTime.day
finishDate = finishTime.day
durationDate = finishDate - startDate
durationDate = str(durationDate)
#Convert Time into Print Format
startTimePrint = startTime.strftime("%I:%M:%S %p ")
startTimePrint = startTimePrint.lstrip('0')
finishTimePrint = finishTime.strftime("%I:%M:%S %p ")
finishTimePrint = finishTimePrint.lstrip('0')

##OUTPUT
if durationDate == "0":
    print("If you leave at " + startTimePrint + ", you will be home at " + finishTimePrint)
else: 
    print("If you leave at " + startTimePrint + ", you will be home at " + finishTimePrint + ", " + durationDate + " days later.")

