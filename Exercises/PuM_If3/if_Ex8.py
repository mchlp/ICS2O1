
#Michael Pu
#2016/10/13
#ICS2O1
#Ms.Strelkovska
#If/Else Exercises C - 8

#Input
year = int(input("Enter a year: "))
#Calculations
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            yearType = "leap"
        else:
            yearType = "common"
    else:
        yearType = "leap"            
else:
    yearType = "common"

#Output
print ("It is a " + yearType + " year")

