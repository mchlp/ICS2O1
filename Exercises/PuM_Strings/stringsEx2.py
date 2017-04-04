
#Michael Pu
#2016/09/19
#ICS2O1
#Ms.Strelkovska
#String Manipulation Exercises A - Part 2

#Input
inputName = input("What is your first and last name? ")

#Calculations
space = inputName.find(" ")
firstName = inputName[:space]
lastName = inputName[space+1:]
firstName = str.upper(firstName[:1]) + firstName[1:]
lastName = str.upper(lastName[:1]) + lastName[1:]

#Output
print("We will enter the name as: " + firstName + " " + lastName)

