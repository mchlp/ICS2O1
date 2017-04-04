
#Michael Pu
#2016/10/04
#ICS2O1
#Ms.Strelkovska
#If/Else Exercises A - 2

#Input
word = input("What is your word? ")

#Calculations
length = len(word)
if length % 2 == 0:
    print("The word '" + word + "' has an even number of letters.")
else:
    print("The word '" + word + "' has an odd number of letters.")
