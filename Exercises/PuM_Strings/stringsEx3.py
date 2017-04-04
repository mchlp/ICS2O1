
#Michael Pu
#2016/09/19
#ICS2O1
#Ms.Strelkovska
#String Manipulation Exercises A - Part 3

#Input
fileName = input("Enter a file name: ")

#Calculations
dot = fileName.find(".")
ext = fileName[dot+1:]

#Output
print('The extension of that file is "' + ext + '"')

