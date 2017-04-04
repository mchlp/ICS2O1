#Doublets Game
#2016/11/08
#ICS2O1
#Michael Pu

import string
import time
import os
import msvcrt
import colorama
import termcolor

def instructions():
    '''
    0 = Black       8 = Gray
    1 = Blue        9 = Light Blue
    2 = Green       A = Light Green
    3 = Aqua        B = Light Aqua
    4 = Red         C = Light Red
    5 = Purple      D = Light Purple
    6 = Yellow      E = Light Yellow
    7 = White       F = Bright White
    '''

    '''
    colorama.init()
    print(termcolor.colored('Hello, World!', 'green', 'on_red'))
    '''

#Print with Colour
def printColour(string, colour, bg=""):
    "(string, colour, bg="")"
    if bg == "":
        print(termcolor.colored(string, colour))
    else:
        print(termcolor.colored(string, colour, "on_"+bg))
    
#Load Intro Screen
def loadIntroScreen():
    introScreen = []
    file = open("introScreen.txt", "r", -1, "UTF8")
    for line in file:
        introScreen.append(line.strip("\n"))
    return introScreen

#Print Intro Screen (1st Time)  
def printIntroScreen():

    global introScreen

    introFrameLines = [[10],[9,10],[8,9,10],[7,8,9,10],[6,7,8,9,10],[5,6,7,8,9,10],[4,5,6,7,8,9,10],[3,4,5,6,7,8,9,10],[2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]]

    introFrame = []
   
    for processframe in introFrameLines:
        os.system("CLS")
        for line in processframe:
            printColour(introScreen[line], 'green')
            #print(introScreen[line])
        time.sleep(0.2)

#Print Intro Screen (Without Animation)
def rePrintIntroScreen():
    global introScreen
    
    for frame in range(1,11):
        printColour(introScreen[frame], 'green')

#Create Doublet Pair List        
def createPairList(wordLen, complxity):
    #LOAD WORD LIST FROM FILE

    def loadWordList(file):
        print("\nLoading words...")
        f = open(file, "r")
        wordList = []
        wordCount = 0
        
        for line in f:
            if (line.find("'")) == (-1):
                wordList.append(line.strip())
                wordCount += 1
                #print(line)

        #print(wordList)
        print(wordCount, "words loaded.")
        return wordList

    def processWords(checkWordList):
        #TURN WORD LIST INTO DICTIONARY - {WORD:DICTIONARY MATCHES}

        def createWordDict(word):
            letterList = []
            newWordList = []
            for letter in word:
                letterList.append(letter)
                
            for letterIndex in range(len(letterList)):
                newLetterList = list(letterList)
                for switchLetter in string.ascii_lowercase:
                    newWord = ""
                    newLetterList[letterIndex] = switchLetter
                    for newLetter in newLetterList:
                        newWord += newLetter
                    #print("CHECK:", newWord)
                    if ((newWord in wordList) and (newWord != word)):
                        #print("MATCH:", newWord)
                        newWordList.append(newWord)
            return newWordList
       
        matchList = {}
        progressCount = 0
        totalProgress = len(checkWordList)
        print("\nProcessing words...")
        for word in checkWordList:
            #print("PROCESSING:", word)
            tempWordDict = createWordDict(word)
            #if len(tempWordDict) > 0:
            matchList[word] = tempWordDict
            progressCount += 1
            #print("Processed", progressCount, "of", totalProgress, "words.")
        print(progressCount, "words processed.")
        return matchList

    def filterWords(wordList, wordLen):
        #TAKE OUT WORDS THAT ARE NOT SPECIFICED LENGTH
        newWordList = []
        for word in wordList:
            if len(word)in wordLen:
                newWordList.append(word)
        return newWordList

    def createConnectionList(matchList, cmplx):
        #CREATE LIST OF PAIRS

        def findConnections(matchList, tempMatchList, path, cmplx, oldList):
            if cmplx > 0:
                curWord = path[-1]
                #print("   "*cmplx, "PROCESSING", curWord, "PATH", path, "COMPX", cmplx)
                if len(matchList[curWord]) > 0:
                    #print("SEARCHING", curWord, tempMatchList[curWord])
                    if len(path) > 1:
                        remList = (path[:-1]) + oldList
                        #print("REMOVE LIST", remList)
                        for remWord in remList:
                            #print("FROM", remList, "BEFORE REMOVE", remWord)
                            if remWord in tempMatchList[curWord]:
                                #print("FROM", tempMatchList[curWord], "REMOVE", remWord)
                                (tempMatchList[curWord]).remove(remWord)
                            # except ValueError:

                    oldList = oldList + matchList[curWord]
                            
                    for word in tempMatchList[curWord]:
                        tempPath = list(path)
                        #tempMatchList[curWord] = []
                        #print("NEW SEARCH", word)
                        tempPath.append(word)
                        findConnections(matchList, tempMatchList, tempPath, cmplx-1, oldList)
                else:
                    #print("NO MORE CONNECTIONS", tempMatchList[curWord])
                    pass
            else:
                #print("NO MORE COMPLEXITY", path)
                global pairList
                pairList.append(path)
                #print("NEW LIST", pairList)
            

        global pairList
        pairList = []

        for rootWord in matchList:
            path = [rootWord]
            tempMatchList = dict(matchList)
            #print("\t---CALL FUNCTION WITH WORD---", path)
            findConnections(matchList, tempMatchList, path, cmplx, [])

        return pairList            

    #wordList = loadWordList("Eng_dictionary.txt")
    wordList = loadWordList("1000words.txt")
    checkWordList = loadWordList("1000words.txt")
    #checkWordList = loadWordList("Eng_dictionary.txt")
    
    checkWordList = filterWords(checkWordList, wordLen)
    
    matchList = processWords(checkWordList)
    #print(matchList, "\n")
    
    pairList = []

    print("\nBuilding words pairs...")
    
    for cmplx in complexity:
        pairList = pairList + (createConnectionList(matchList, cmplx))
        
    #print(pairList)
    print(len(pairList), "pairs built.")

#Display Main Menu
def mainMenu():
    #MAIN MENU NAVAGATING
    keyLoc = 1  
    while True:
        os.system("CLS")
        if keyLoc == 1:
            keyTup = ("->", "", "")
        elif keyLoc == 2:
            keyTup = ("", "->", "")     
        else:
            keyTup = ("", "", "->")

        rePrintIntroScreen()
        print(
    '''
    \t\t MAIN MENU  
    
    \t\t Use the arrow keys to move up and down. Press enter to select.
    \t\t\t %3s 1. Instructions
    \t\t\t %3s 2. New Game
    \t\t\t %3s 3. Exit
    
    ''' %keyTup)

        key = ord(msvcrt.getch())
        #time.sleep(0.01)
        #print(key)
        if key == 72:
            keyLoc -= 1
            if keyLoc == 0:
                keyLoc = 3
        elif key == 80:
            keyLoc += 1
            if keyLoc == 4:
                keyLoc = 1
        elif key == 13:
            enterMenu(keyLoc)
            return
        else:
            pass

#Press Enter in Main Menu         
def enterMenu(keyLoc):
    #ENTER MENU - PRESS ENTER
    if keyLoc == 1:
        disInstruct()
    elif keyLoc == 2:
        print("NEW GAME")
    else:
        exit()

#Display Instructions      
def disInstruct():
    os.system("CLS")
    print('''
	INSTRUCTIONS
	
    The aim of the game is to get from an inital word
    to afinal word by changing only one letter per line.
    Note that every line must be a valid word. Sometimes there
    are several possibilities.

    Press <enter> to return to main menu.
    ''')
    input()
    mainMenu()

    
colorama.init()
wordLen = [4]
complexity = [5,6]
#os.system('color F3')

introScreen = loadIntroScreen()    
printIntroScreen()
createPairList(wordLen, complexity)
mainMenu()
input()
                
