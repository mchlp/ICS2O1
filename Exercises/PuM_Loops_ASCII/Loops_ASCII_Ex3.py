 


#Michael Pu
#2016/10/26
#ICS2O1
#Ms.Strelkovska
#ASCII Loops Exercises - 3

import random
import time

while True:
    print("   --------------------\n   | MIND READER GAME |\n   --------------------")

    print("\nChoose a two digit number.")
    input("Enter any key to continue...")

    print("\nAdd the two digits together.")
    input("Enter any key to continue...")

    print("\nSubtract your answer from your original answer.")
    input("Enter any key to continue...")

    print("\nFind your result in the following list and remember the symbol next to it.")
    input("Enter any key to continue to display the list...")

    charList = []

    for a in range(9729, 9885):
        charList.append(chr(a))

    magicChar = random.choice(charList)
    charList.remove(magicChar)

    print()

    for num in range(0, 20):
        for col in range(0,5):
            if (num+(col*20))%9 == 0:
                char = magicChar
            else:
                char = random.choice(charList)
                charList.remove(char)
            print("%2i. %s\t\t" %(num+(col*20), char), end="")
        print()

    print("\nWhen you have found your character, enter any key to continue...")
    input()
    print("\nNow stare at the screen and picture your symbol in your mind.")
    time.sleep(1)
    print("\nMind Readng In Progress...")
    count = 0
    while count < 40:
        print("-", end="")
        time.sleep(0.02)
        count = count + 1

    print("\nYour character is: " + magicChar)
    validInput = False
    while validInput == False:
        playAgain = input("\nWould you like to play again? [Enter Y to play again or N to exit.]")
        if playAgain == "Y" or playAgain == "N":
            validInput = True
    if playAgain == "N":
        break


    



