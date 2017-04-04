#Doublets Game
#2016/11/08
#ICS2O1
#Michael Pu

import string
import time
import os
import msvcrt
import random
import collections
import colorama
import termcolor

#os.system("color 08")
#scrnWidth = 100
#os.system("mode con: cols=" + str(scrnWidth) +" lines=40")

def printColour(string, colour="cyan", bg=""):
    "(string, colour, bg="")"
    if bg == "":
        return(termcolor.colored(string, colour))
    else:
        return(termcolor.colored(string, colour, "on_"+bg))

def printGrid(rows, cols):
    for row in range(rows):
        print(printColour(" ---"*cols))
        for col in range(cols):
            print(printColour("| %s " %"a"), end="")
        print(printColour("|"))
    print(printColour(" ---"*cols))

colorama.init()
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
printGrid(rows, cols)
input()
