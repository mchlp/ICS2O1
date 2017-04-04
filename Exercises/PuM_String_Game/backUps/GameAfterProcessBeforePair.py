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
import random
import collections


#os.system("color F3")
#os.system('mode con: cols=100 lines=30')
scrnWidth = 100

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
    "(string, colour, bg="")"

#Print Colour
def printColour(string, colour="cyan", bg=""):
    "(string, colour, bg="")"
    if bg == "":
        return(termcolor.colored(string, colour))
    else:
        return(termcolor.colored(string, colour, "on_"+bg))
    
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

    introFrameLines = [[10],[9,10],[8,9,10],[7,8,9,10],[6,7,8,9,10],[5,6,7,8,9,10],[4,5,6,7,8,9,10]
    ,[3,4,5,6,7,8,9,10],[2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,2,4,5,6,7,8,9,10]
    ,[1,2,3,4,5,6,7,8,9,10],[1,2,2,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,2,4,5,6,7,8,9,10]
    ,[1,2,3,4,5,6,7,8,9,10],[1,2,2,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,2,4,5,6,7,8,9,10]
    ,[1,2,3,4,2,6,2,8,2,10],[1,2,3,2,5,2,7,2,9,2],[1,2,3,4,2,6,2,8,2,10],[1,2,3,2,5,2,7,2,9,2]
    ,[1,2,3,4,2,6,2,8,2,10],[1,2,3,2,5,2,7,2,9,2],[1,2,3,4,2,6,2,8,2,10],[1,2,3,2,5,2,7,2,9,2]
    ,[1,2,3,4,5,6,7,8,2],[1,2,3,4,5,6,7,8,2,10],[1,2,3,4,5,6,7,2,9,10],[1,2,3,4,5,6,2,8,9,10]
    ,[1,2,3,4,5,2,7,8,9,10],[1,2,3,4,2,6,7,8,9,10],[1,2,3,2,5,6,7,8,9,10],[1,2,3,4,2,6,7,8,9,10]
    ,[1,2,3,4,5,2,7,8,9,10],[1,2,3,4,5,6,2,8,9,10],[1,2,3,4,5,6,7,2,9,10],[1,2,3,4,5,6,7,8,2,10]
    ,[1,2,3,4,5,6,7,8,9,2]]

    introFrame = []
   
    for processframe in introFrameLines:
        os.system("CLS")
        print("\n"*2)
        for line in processframe:
            print(printColour(introScreen[line]))
            #print(introScreen[line])
        time.sleep(0.1)
        
    print()

#Print Intro Screen (Without Animation)
def rePrintIntroScreen():
    global introScreen
    print("\n"*2)
    for frame in range(1,11):
        print(printColour(introScreen[frame]))

#Filter Pair List
def filterPairList(wordLen, complexity, pairList): 
    oldPairList = []
    newPairList = []
    for word in pairList:
        #print("WORD", word)
        if len(word[0]) in wordLen:
            #print("GOOD LEN", wordLen)
            if len(word) in complexity:
                #print("GOOD COM", complexity)
                oldPairList.append(word)
                newPairList.append([word[0],word[-1]])
                #input()
    return (oldPairList, newPairList)

#Create Doublet Pair List        
def createPairList(wordLen, complexity):

    global wordList
    global checkWordList
    global toUseDict
    
    #LOAD WORD LIST FROM FILE
    print("\n"*4)
    print(printColour("Starting Game... This may take up to eight mintues.".center(scrnWidth, " ")))
    
    def loadWordList(file):
        #global wordList
        wordListLoad = collections.OrderedDict()
        global totalWords
        f = open(file, "r")
        wordCount = 0
        
        for line in f:
            if (line.find("'")) == (-1):
                word = line.strip().lower()
                wordListLoad[word] = []
                wordCount += 1
                #print(line)

        #print(wordList)
        totalWords = wordCount
        return wordListLoad

    def processWords(wordList):
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
       
        progressCount = 0
        print(printColour("Processing words...".center(scrnWidth, " ")), end="")
        totalWords = len(wordList)
        oneDash = totalWords//(scrnWidth-2)
        counter = 0
        print(printColour(" |"), end="")
        keylist = list(wordList.keys())
        for word in keylist:
            counter += 1
            if counter > oneDash:
                print(printColour("-"), end="")
                counter = 0
            #print("PROCESSING:", word)
            #print(word)
            tempWordDict = createWordDict(word)
            #if len(tempWordDict) > 0:
            wordList[word] = tempWordDict
            progressCount += 1
            #print("Processed", progressCount, "of", totalWords, "words.")
        print(printColour("|"), end="")
        print(printColour((str(progressCount) + " words processed.").center(scrnWidth, " ")))
        return wordList

    def filterWords(wordList, wordLen):
        #TAKE OUT WORDS THAT ARE NOT SPECIFICED LENGTH
        newWordList = []
        for word in wordList:
            if len(word)in wordLen:
                newWordList.append(word)
        return newWordList

    def createConnectionList(matchList, cmplx, tCmplx):
    
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
        
        totalWords = len(matchList)
        oneDash = (totalWords*tCmplx)//(scrnWidth-2)
        counter = 0
         
        for rootWord in matchList:
            counter += 1
            if counter > oneDash:
                print(printColour("-"), end="")
                counter = 0
            path = [rootWord]
            tempMatchList = dict(matchList)
            #print("\t---CALL FUNCTION WITH WORD---", path)
            findConnections(matchList, tempMatchList, path, cmplx, [])
        
        return pairList            
   
    print(printColour("Loading pair words...".center(scrnWidth, " ")), end="")
    wordList = loadWordList(toUseDict)
    #wordList = loadWordList("Eng_dictionary.txt")
    #wordList = loadWordList("1000words.txt")
    print(printColour(((str(len(wordList))) +  " words loaded.").center(scrnWidth, " ")))
    print(printColour("Loading check words...".center(scrnWidth, " ")), end="")
    #checkWordList = loadWordList("1000words.txt")
    checkWordList = loadWordList("Eng_dictionary.txt")
    #checkWordList = wordList
    print(printColour(((str(len(checkWordList))) +  " words loaded.").center(scrnWidth, " ")))

    #wordList = filterWords(wordList, wordLen)
    #print(wordList)
    matchList = processWords(wordList)
    #print(matchList, "\n")
    
    pairList = []
    
    print()
    print(printColour("Building words pairs...".center(scrnWidth, " ")), end="")
    
    print(printColour(" |"), end="")    
    for cmplx in complexity:
        pairList = pairList + (createConnectionList(matchList, cmplx, len(complexity)))
    print(printColour("|"))
        
    #print(pairList)
    print(printColour((str(len(pairList)) + " pairs built.").center(scrnWidth, " ")))
    
    
    return pairList
    
#Main Menu 
def mainMenu():
    #MAIN MENU NAVAGATING
    keyLoc = 1  
        
    while True:
        os.system("CLS")

        rePrintIntroScreen()
        printMenu(keyLoc)
        

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

#Print Menu
def printMenu(keyLoc):

    # PRINT TOP PART OF MENU
    keyIns = ["Use the ARROW KEYS to move up and down.", "Press ENTER to select.", ""]
    print(printColour("\n                   -------------------------------------------------------------"))
    for line in keyIns:
        print(printColour(("                  |")), end="")
        print(printColour(line.center(61, " ")), end="")
        print(printColour(("|")))

    # print(printColour('''
                   # -------------------------------------------------------------
                  # | Use the arrow keys to move up and down.                     |
                  # | Press enter to select.                                      |
                  # |                                                             |'''))
    
    #PRINT BOTTOM OF MENU
    keyList = ["1. Instructions"
             , "2. New Game    "
             , "3. Exit        "]

    #if keyLoc == 1:
        #keyList = ["     1. Instructions", "     2. New Game", "     3. Exit"]
        #keyList[0] = "  => 1. Instructions"
    #elif keyLoc == 2:
        #keyList = ["     1. Instructions", "     2. New Game", "     3. Exit"]
        #keyList[1] = "  => 2. New Game"   
    #else:
        #keyList = ["     1. Instructions", "     2. New Game", "     3. Exit"]
        #keyList[2] = "  => 3. Exit"
            
    keyLoc -= 1
    keyListFormat = [("cyan",""),("cyan",""),("cyan","")]
    keyListFormat[keyLoc] = ("white","cyan")
    for a in range(3):
        print(printColour("                  |                       "), end="")
        print("%-20s" %(printColour(keyList[a],(keyListFormat[a])[0],(keyListFormat[a])[1])), end="")
        print(printColour("                       |"))
    print(printColour("                  |                                                             |"))
    print(printColour("                   --------------------------------------------------------------"))                
            
#Press Enter in Main Menu         
def enterMenu(keyLoc):
    #ENTER MENU - PRESS ENTER
    if keyLoc == 1:
        disInstruct()
    elif keyLoc == 2:
        gameMenu()
    else:
        exit()

#Display Instructions      
def disInstruct():
    os.system("CLS")
    print()
    print()
    print()
    print()
    printBoxed(["How to Play"])
    #print(printColour("--------------".center(scrnWidth, " ")), end="")
    #print(printColour("|INSTRUCTIONS|".center(scrnWidth, " ")), end="")
    #print(printColour("--------------".center(scrnWidth, " ")), end="")
    print()
    print(printColour("The aim of the game is to get from an inital word".center(scrnWidth, " ")), end="")
    print(printColour("to a final word by changing only one letter each time.".center(scrnWidth, " ")), end="")
    print(printColour("Note that every change must result in a valid word.".center(scrnWidth, " ")), end="")
    print()
    printBoxed(["Levels"])
    print()
    print(printColour("There are three level options:".center(scrnWidth, " ")), end="")
    print()
    print(printColour("EASY: 1-3 Letter Changes".center(scrnWidth, " ")), end="")
    print(printColour("MEDIUM: 4-5 Letter Changes".center(scrnWidth, " ")), end="")
    print(printColour("HARD: 5+ Letter Changes".center(scrnWidth, " ")), end="")
    print()
    print(printColour("Press <ENTER> to return to main menu.". center(scrnWidth," ")), end="")
    input()
    mainMenu()

#New Game Menu
def gameMenu():
    keyLoc = 1  
        
    while True:
        os.system("CLS")

        rePrintIntroScreen()
        printGameMenu(keyLoc)
        

        key = ord(msvcrt.getch())
        #time.sleep(0.01)
        #print(key)
        if key == 72:
            keyLoc -= 1
            if keyLoc == 0:
                keyLoc = 3
        elif key == 80:
            keyLoc += 1
            if keyLoc == 5:
                keyLoc = 1
        elif key == 13:
            enterGameMenu(keyLoc)
            return
        else:
            pass         

#Print New Game Menu
def printGameMenu(keyLoc):

    # PRINT TOP PART OF MENU
    keyIns = ["Use the ARROW KEYS to move up and down."
            , "Press ENTER to select."
            , "", "1. Instructions"
            , "2. New Game    "
            , ""]
    print(printColour("\n                   -------------------------------------------------------------"))
    for line in keyIns:
        print(printColour(("                  |")), end="")
        print(printColour(line.center(61, " ")), end="")
        print(printColour(("|")))
    
    #PRINT BOTTOM OF MENU
    keyList = ["A. Easy                   "
             , "B. Medium                 "
             , "C. Hard                   "
             , "D. Return to Previous Menu"]
            
    keyLoc -= 1
    keyListFormat = [("cyan",""),("cyan",""),("cyan",""),("cyan","")]
    keyListFormat[keyLoc] = ("white","cyan")
    for a in range(4):
        print(printColour("                  |                           "), end="")
        print("%-20s" %(printColour(keyList[a],(keyListFormat[a])[0],(keyListFormat[a])[1])), end="")
        print(printColour("        |"))
    print(printColour("                  |                                                             |"))
    print(printColour("                  |                       3. Exit                               |"))
    print(printColour("                  |                                                             |"))
    print(printColour("                   --------------------------------------------------------------"))     

#Press Enter in Game Menu
def enterGameMenu(keyLoc):
    global diff
    #ENTER MENU - PRESS ENTER
    if keyLoc == 1:
        diff = 0
        startGame()
    elif keyLoc == 2:
        diff = 1
        startGame()
    elif keyLoc == 3:
        diff = 2
        startGame()
    else:
        mainMenu()

#Start New Game
def startGame():

    global pairList
    global dif
    
    if dif == 0:
        difMode = "EASY"
    elif dif == 1:
        difMode = "MEDIUM"
    else:
        difMode = "HARD"

    os.system("CLS")
    print("\n"*5)
    print(printColour(("Loading new game in " + difMode + " mode...").center(scrnWidth," ")))
    
    #print(pairList)
    
    if dif == 0:
        wordLen = [1,2,3,4,5,6,7,8,9]
        complexity = [1,2,3]
    elif dif == 1:
        wordLen = [3,4,5,6,7,8,9]
        complexity = [4,5]
    else:
        wordLen = [4,5,6,7,8,9]
        complexity = [5,6,7,8]
    twoPairList = filterPairList(wordLen, complexity, pairList)
    #print(twoPairList)
    #input()
    matchPair = random.choice(twoPairList[0])
    print(printColour("Game is ready to begin... Press ENTER to continue.".center(scrnWidth, " ")))
    input()
    startSession(matchPair)

#Start Playing Session
def startSession(matchPair):
    global attemptList
    
    os.system("CLS")
    startWord = matchPair[0]
    endWord = matchPair[-1]
    print(printColour("\n"*4))
    #print(printColour("Start:" + startWord))
    #print(printColour("End:" + endWord))
    #print(printColour(("Solution:", matchPair)))
    curLoc = 0
    curWord = startWord
    wordsTup = (startWord, curWord, endWord)
    attemptList = wordsTup[0]
    gameCursor(wordsTup, 1)

#Control Cursor Movement in Game
def gameCursor(wordsTup, phase, curLoc=0, moves=0, error=False, attmpWord=""):
    alphaLoc = 0
    
    os.system("CLS")    
    displaySession(wordsTup, curLoc, phase, alphaLoc, error, attmpWord)
    
    wordLen = len(wordsTup[0])
    alphaLen = len(string.ascii_uppercase+"*")       
    
    while True:
        key = ord(msvcrt.getch())
        #time.sleep(0.01)
        #print(key)
        if key == 75:
            if phase == 1:
                curLoc -= 1
                if curLoc == -1:
                    curLoc = 0
            else:
                alphaLoc -=1
                if alphaLoc == -1:
                    alphaLoc = alphaLen-1         
            displaySession(wordsTup, curLoc, phase, alphaLoc, error, attmpWord)
            
        elif key == 77:
            if phase == 1:
                curLoc += 1
                if curLoc == wordLen:
                    curLoc = (wordLen-1)
            else:
                alphaLoc += 1
                if alphaLoc == alphaLen:
                    alphaLoc = 0   
            displaySession(wordsTup, curLoc, phase, alphaLoc, error, attmpWord)
            
        elif key == 13:
            gameEnterButton(wordsTup, curLoc, alphaLoc, phase, moves)
            return
        else:
            pass       

#When Enter is Pressed in Game Menu            
def gameEnterButton(wordsTup, curLoc, alphaLoc, phase, moves):
    global checkWordList
    global attemptList
    
    if phase == 1:
        gameCursor(wordsTup, 2, curLoc, moves, False)
    else:
        if alphaLoc == 26:
            gameCursor(wordsTup, 1, curLoc, moves, False)
        else:
            letters = string.ascii_uppercase + "*"
            oldWord = wordsTup[1]
            letterList = []
            for letter in oldWord:
                letterList.append(letter)
            letterList[curLoc] = letters[alphaLoc]
            newWord = ""
            for letter in letterList:
                newWord += letter
            if newWord.lower() not in checkWordList:
                #print("ERROR", newWord, wordList, newWord.lower() in wordList)
                gameCursor(wordsTup, 2, curLoc, moves, True, newWord)
                return
            if newWord.upper() == wordsTup[2].upper():
                os.system("CLS")
                displaySession((wordsTup[0], newWord, wordsTup[2]), 0, 1)
                time.sleep(1)
                attemptList.append(wordsTup[2])
                finishSession(moves, wordsTup)
                return
            moves += 1
            wordsTup = (wordsTup[0], newWord, wordsTup[2])
            attemptList.append(newWord.upper())
            
            gameCursor(wordsTup, 1, 0, moves, False)

#When User Finishes Puzzle            
def finishSession(moves, wordsTup):
    global attemptList
    global dif

    os.system("CLS")
    print("\n"*4)
    printBoxed(["Congratulation! You've completed a puzzle from " + diff + " mode."])
    print()
    print(printColour(("You got from " + wordsTup[0].upper() + " to " + wordsTup[2].upper()
    + " in " + str(moves) + " moves.").center(scrnWidth," ")))
    print()
    print(printColour(("Here are your moves: ").center(scrnWidth," ")))
    printBoxed(attemptList)
    print()
    print(printColour(("Press ENTER to return to the main menu.").center(scrnWidth," ")))
    input()
    mainMenu()
            
#Display Playing Session 
def displaySession(wordsTup, curLoc, phase, alphaLoc=0, error=False, attmpWord=""):
    global dif
    
    os.system("CLS") 
    print(printColour(("\n"*4)))
    printBoxed([("Game In Progress - " + dif)])
    print()
    printBoxed(["Start Word: " + (wordsTup[0]).upper()])
    print()
    
    instruction = ["Use the LEFT and RIGHT ARROW to move the cursor."]
    
    if phase == 1:
        instruction.append("Press ENTER to select the letter you wish to modify.")
    else:
        instruction.append("Press ENTER to select which letter you wish to change to.")
        instruction.append("Select the * to change the letter you wish to modify.")
        
    printBoxed(instruction)
    
    if error == True:  
        printBoxed(["Try again.", attmpWord.upper() + " is not a word."])
    
    printBoxed([(wordsTup[1].upper()), (" "*curLoc + "^" + " "*(len(wordsTup[0])-(curLoc+1)))])
    print()
    
    if phase > 1:
        letters = string.ascii_uppercase + "*"
        printBoxed([letters, (" "*alphaLoc + "^" + " "*(len(letters)-(alphaLoc+1)))])
    #print(printColour((wordsTup[1].upper()).center(scrnWidth, " ")), end="")
    #print(printColour((" "*curLoc + "^" + " "*(len(wordsTup[0])-curLoc)).center(scrnWidth, " ")))
    print()
    printBoxed(["End Word: " + (wordsTup[2]).upper()])

#Print Boxed Text  
def printBoxed(text):
    #Find Max Length
    max = 0
    for testLine in text:
        if len(testLine) > max:
            max = len(testLine)
            
    print(printColour(("-"*(max + 2)).center(scrnWidth, " ")), end="")
    for line in text:
        totalFill = (max-len(line))
        leftFill = totalFill//2
        rightFill = totalFill-leftFill
        print(printColour(("| " + " "*leftFill + line + " "*rightFill + " |").center(scrnWidth, " ")), end="")
    print(printColour(("-"*(max + 2)).center(scrnWidth, " ")), end="")

#Pre-Game Menu    
def preGameMenu():
    print("\n"*4)
    keyLoc = 0         
    while True:
        os.system("CLS")
        printPreGameMenu(keyLoc)
       
        key = ord(msvcrt.getch())
        #time.sleep(0.01)
        #print(key)
        if key == 72:
            keyLoc -= 1
            if keyLoc == -1:
                keyLoc = 0
        elif key == 80:
            keyLoc += 1
            if keyLoc == 2:
                keyLoc = 1
        elif key == 13:
            enterPreGameMenu(keyLoc)
            return
        else:
            pass       
        
#Print Pre-Game Menu
def printPreGameMenu(keyLoc):
    # PRINT TOP PART OF MENU
    print("\n"*4)
    printBoxed(["Select a dictionary to use."])
    print
    print(printColour("Use the arrow keys to move up and down.".center(scrnWidth, " ")))
    print(printColour("Press ENTER to select.".center(scrnWidth, " ")))
    print(printColour("\n                   -------------------------------------------------------------"))

    keyList = ["Dictionary 1 - 1000 Words (Loading Time: 1 Minute)"
             , "Dictionary 2 - 9000 Words (Loading Time: 8 Minutes)"]
            
    keyListFormat = [("cyan",""),("cyan",""),("cyan","")]
    keyListFormat[keyLoc] = ("white","cyan")
    for a in range(len(keyList)):
        print(printColour("                  |                       "), end="")
        print("%-20s" %(printColour(keyList[a],(keyListFormat[a])[0],(keyListFormat[a])[1])), end="")
        print(printColour("                       |"))
    print(printColour("                  |                                                             |"))
    print(printColour("                   --------------------------------------------------------------")) 
    
def enterPreGameMenu(keyLoc):
    global toUseDict
    if keyLoc == 1:
        toUseDict = "1000words.txt"
    else:
        toUseDict = "Eng_dictionary.txt"

        
colorama.init()
wordLen = [1,2,3,4,5,6,7,8,9,10]
complexity = [1,2,3,4,5,6,7,8,9,10]
#os.system('color F3')

global toUseDict
global attemptList
global pairList
global wordList
global checkWordList
global dif

toUseDict = "Eng_dictionary.txt"
dif = 0
wordList = []
checkWordList = []
attemptList = []

os.system("CLS")

#preGameMenu()

start = time.time()
pairList = createPairList(wordLen, complexity)
end = time.time()

print("TOTAL TIME", (end-start)/60)
#print("DONE")
print()
print(printColour("All components loaded sucessfully.".center(scrnWidth, " ")))
print()
print(printColour("Press ENTER to start the game...".center(scrnWidth, " ")))
input()



introScreen = loadIntroScreen()
printIntroScreen()

mainMenu()
                
