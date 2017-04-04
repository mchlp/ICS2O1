
#Michael Pu
#2016/10/25
#ICS2O1
#Ms.Strelkovska
#ASCII Loops Exercises - 2

import random

while True:
    #Input
    inputCorrect = False
    goodInput = ["r", "R", "1", "p", "P", "2", "s", "S", "3", "!"]

    while inputCorrect == False:
        print ("--Accepted Throws--\nRock: r R 1\nPaper: p P 2\nScissors:s S 3\nExit: ! \n-------------------")
        throw = input("Enter your throw: ")
        if (throw in goodInput) == True:
            inputCorrect = True
        print()

    #Check if Exit

    if throw == "!":
        break

    #Processing
    
    rock = "rR1"
    paper = "pP2"
    scissors = "sS3"

    if (throw in rock) == True:
        userThrow = 1
    elif (throw in paper) == True:
        userThrow = 2
    elif (throw in scissors) == True:
        userThrow = 3

    compThrow = random.randint(1,3)

    if userThrow == 1:
        if compThrow == 1:
            result = "TIE"
        elif compThrow == 2:
            result = "WIN"
        else:
            result = "LOSE"
    elif userThrow == 2:
        if compThrow == 1:
            result = "WIN"
        elif compThrow == 2:
            result = "TIE"
        else:
            result = "LOSE"
    else:
        if compThrow == 1:
            result = "LOSE"
        elif compThrow == 2:
            result = "WIN"
        else:
            result = "TIE"

    displayThrow = ["ROCK", "PAPER", "SCISSORS"]

    #Output

    print("Player throws", displayThrow[userThrow-1])   
    print("Computer throws", displayThrow[compThrow-1])
    print("You " + result + "!")
    input("Enter any key to continue...")
    print("---------------------------------------------------")

#End Program

print("Good Bye.")





