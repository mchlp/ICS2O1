
#Michael Pu
#2016/09/12
#ICS2O1
#Ms.Strelkovska
#Unit 1 - Ex 7

import datetime

#Input
birthYear = int(input("Enter your year of birth: "))

#Calculations
curYear = datetime.datetime.now().year
age = curYear - birthYear

#Output
print("You are ", age, " year(s) old.")


