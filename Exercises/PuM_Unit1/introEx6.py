
#Michael Pu
#2016/09/12
#ICS2O1
#Ms.Strelkovska
#Unit 1 - Ex 6

#Input
numPeople = int(input("Enter the number of people: "))
slices = 32

#Calculations
wholeSlices = 32//numPeople
leftOverSlices = 32%numPeople
decimalSlices = 32/numPeople

#Output
print("Option 1:", wholeSlices,"slice(s) each,",leftOverSlices, "leftover")
print("Option 2:", decimalSlices, "slice(s) each")
