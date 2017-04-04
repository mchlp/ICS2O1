
#Michael Pu
#2016/09/19
#ICS2O1
#Ms.Strelkovska
#String Manipulation Exercises A - Part 1

#Input
sentence = input("Enter a sentence: ")

#Calculations
letterCount = len(sentence)
first5 = sentence[0:5]
last5 = sentence[-5:]
upper = str.upper(sentence)
lower = str.lower(sentence)

#Output
print("It has", letterCount, "letters")
print("First 5: ", first5)
print("Last 5: ", last5)
print("UPPERCASE: ", upper)
print("lowercase: ", lower)

