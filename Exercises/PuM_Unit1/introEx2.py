
#Michael Pu
#2016/09/12
#ICS2O1
#Ms.Strelkovska
#Unit 1 - Ex 2

##WITH 60 BOOKS

#Input
num = 60
print ("Number of Books: ", num)
coverPrice = 24.95
discount = 0.4
shipCostFirst = 3.0
shipCostRest = 0.75

#Calculations
totalCost = coverPrice * (1-discount) * num + shipCostFirst + shipCostRest * (num-1)

#Output
print ("Total Cost: $", round(totalCost,2),"\n")

##WITH USER-INPUTED NUMBER OF BOOKS

#Input
num = int(input("Enter the number of books you would like to purchase: "))
print ("Number of Books: ", num)
coverPrice = 24.95
discount = 0.4
shipCostFirst = 3.0
shipCostRest = 0.75

#Calculations
totalCost = coverPrice * discount * num + shipCostFirst + shipCostRest * (num-1)

#Output
print ("Total Cost: $", round(totalCost,2))
