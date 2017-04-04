
#Michael Pu
#2016/09/16
#ICS2O1
#Ms.Strelkovska
#Unit 1 - Exercise Set 3 - Ex 2

#Input
num = int(input("Enter a 3 digit number: "))

#Calculations
hunDig = num // 100
tenDig = num // 10 - hunDig * 10
oneDig = num - hunDig * 100 - tenDig * 10

#Output
print("The hundreds-place digit is: ", hunDig)
print("The tens-place digit is: ", tenDig)
print("The ones-place digit is: ", oneDig)


