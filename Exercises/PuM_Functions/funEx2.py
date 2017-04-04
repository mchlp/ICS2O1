
#Michael Pu
#2016/11/28
#ICS2O1
#Ms.Strelkovska
#Function Exercises A - 2

def palindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        else:
            return False

while True:
    print(palindrome(input("Enter a word: ")))
