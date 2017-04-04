#Michael Pu
#2016/09/12
#ICS2O1
#Ms.Strelkovska
#Unit 1 - Ex 5
import math

#Input
x1 = int(input("Enter the x value of the first coordinate: "))
y1 = int(input("Enter the y value of the first coordinate: "))
x2 = int(input("Enter the x value of the second coordinate: "))
y2 = int(input("Enter the y value of the second coordinate: "))

#Calculations
xDif = abs(x1-x2)
yDif = abs(y1-y2)
distance = math.sqrt(xDif**2 + yDif**2)
roundDis = round(distance,2)

#Output
print("Distance: ", distance)
print("Rounded Distance: ", roundDis)
