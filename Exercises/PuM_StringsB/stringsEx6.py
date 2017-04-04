
#Michael Pu
#2016/09/26
#ICS2O1
#Ms.Strelkovska
#String Manipulation Exercises B - Part 6

#Input
width = int(input("Enter a width under 98 characters: "))
sen = input("Enter a short sentence (under %s characters): " %str(width))


#Calculations
empSpace = (width - len(sen))//2

#Output
print("."*empSpace + sen + "."*empSpace)


