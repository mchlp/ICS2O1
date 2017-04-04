
#Michael Pu
#2016/09/16
#ICS2O1
#Ms.Strelkovska
#Unit 1 - Exercise Set 3 - Ex 3

#Input
money = int(input("Enter the number of cents less than $1.00: "))

#Calculations
num25 = money//25
leftover = money%25
num10 = leftover//10
leftover = leftover%10
num5 = leftover//5
leftover = leftover%5
num1 = leftover

#Output
print("")
print("%-10s %-10s %-10s %-10s %-10s" %("Money", "Quarters", "Dimes", "Nickels", "Cents"))
print("%-10i %-10i %-10i %-10i %-10i" %(money, num25, num10, num5, num1))



