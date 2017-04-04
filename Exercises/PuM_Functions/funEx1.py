
#Michael Pu
#2016/11/28
#ICS2O1
#Ms.Strelkovska
#Function Exercises A - 1

def listfind(value, searchList):
    try:
        return searchList.index(value)
    except ValueError:
        return -1

listOfWords = list(map(lambda line: line.strip("\n"), open("Eng_dictionary.txt")))
word = input("Enter a word: ")
print("It is at index position: " + str(listfind(word, listOfWords)))

