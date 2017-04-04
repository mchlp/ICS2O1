#Programming Test 2 Bonus
#2016/11/30
#Michael Pu

import string

ordSent = ""
sent = input("Enter a sentence: ").upper()
for letter in string.ascii_uppercase:
    for char in sent:
        if char == letter:
            ordSent += char
print(sent)    
print(ordSent)
