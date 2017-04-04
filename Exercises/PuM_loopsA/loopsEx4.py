
#Michael Pu
#2016/10/21
#ICS2O1
#Ms.Strelkovska
#Repetition Exercises A - 4

#Input
name = input("Enter you name: ")

#Calculations
print ("The name", name, "would be: ", end="")
for a in name:
    print(str(ord(a)),end=", ")
