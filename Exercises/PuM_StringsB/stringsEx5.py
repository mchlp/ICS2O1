
#Michael Pu
#2016/09/26
#ICS2O1
#Ms.Strelkovska
#String Manipulation Exercises B - Part 5

#Input
n = int(input("Enter a number: "))

#Calculations
nonBonus = ("\t"+("X "*n)+"\n")*n
emptyCol = (98-(n*2))//2
emptyRows = (32-n)//2
output = (("|") + (" "*emptyCol) + ("X "*n) + (" "*emptyCol) + ("|") + ("\n"))*n
output = ("-"*100 + "\n") + (("|" + " "*98 + "|" + "\n")*emptyRows) + (output) + (("|" + " "*98 + "|" + "\n")*emptyRows) + (("-"*100) + "\n")

#Output
print("Non-Bonus:\n"+ nonBonus)
print("Bonus:\n" + output)



