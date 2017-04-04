
#Michael Pu
#2016/10/05
#ICS2O1
#Ms.Strelkovska
#If/Else Exercises A - 5

#Input
while True:
    try:
        hoursInput = input("How many hours did you work this week(>=0)? ")
        hours = float(hoursInput)
        if hours < 0:
            raise ValueError
        break
    except ValueError:
        print (hoursInput+" is not a valid number of hours. Please enter a positive number or zero. \n")
        
while True:
    try:
        wageInput = input("What is your hourly wage(>=0)? ")
        wage = float(wageInput)
        if wage < 0:
            raise ValueError
        break
    except ValueError:
        print (wageInput+" is not a valid wage. Please enter a positive number or zero.\n")
        

#Calculations
if hours > 40:
    pay = wage*40 + (wage*1.5)*(hours-40)
else:
    pay = wage*hours
    
#Ouput
print ("-----------------------------")
print ("Hours: %-10.2f" %hours)
print ("Wage: %-10.2f" %wage)
print ("Gross Earning of this Week: $%-10.2f" %pay)
