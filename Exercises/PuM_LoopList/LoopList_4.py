
#Michael Pu
#2016/11/21
#ICS2O1
#Ms.Strelkovska
#Looping Through Lists Exercises 4

import string

sent = (input("Enter a sentence: ")).lower()

allMatch = True

for letter in string.ascii_lowercase:
    if letter not in sent:
        print("The sentence IS NOT a pangram.")
        allMatch = False
        break

if allMatch == True:
    print("The sentence IS a pangram.")
    
