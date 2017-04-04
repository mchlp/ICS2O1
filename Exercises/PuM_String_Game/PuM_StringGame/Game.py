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


#os.system("color 08")
scrnWidth = 100
os.system("mode con: cols=" + str(scrnWidth) +" lines=40")

#For My Reference
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

#Prepare Pair List
def preparePairList(wordLenList, cmplxList, dataList):
    pairList = []
    
    for startWord in dataList: 
        if len(startWord) in wordLenList:
            for cmplx in cmplxList:
                for endWord in dataList[startWord]["complex"][cmplx]:
                    pairList.append((startWord, endWord, dataList[startWord]["path"][cmplx][endWord]))
    return pairList            

#Find Random Pair in Pair List
def findRandomPair(pairList):
    return random.choice(pairList)
    
#Create Doublet Pair List        
def createData(complexity, toUseDict):
    
    
    print("\n"*4)
    print(printColour("Starting Game... This may take a while.".center(scrnWidth, " ")))
    
    #LOAD WORD LIST FROM FILE
    def loadWordList(file):
        wordListLoad = set()
        f = open(file, "r")
        
        for line in f:
            if (line.find("'")) == (-1):
                wordListLoad.add(line.strip().lower())
                #print(line)

        #print(wordList)
        return wordListLoad

    def combineWordList(changeList, baseList):
        for word in baseList:
            if word not in changeList:
                changeList.add(word)
        return changeList
        
    #COMPILE WORD LIST INTO DATALIST ({})    
    def findMatch(wordList):
        print(printColour(" |"), end="")   
        matchList = collections.OrderedDict()
        totalWords = len(wordList)
        lenDash = totalWords//(scrnWidth-4)
        count = 0
        for word in wordList:
            #print("Count:", count, "Processing:", word);
            count +=1
            if (count >= lenDash):
                print(printColour("-"), end="")
                count = 0
            matchList[word]=collections.OrderedDict()
            matchList[word]["complex"]=[]
            matchList[word]["path"]=[]
            matchList[word]["complex"].append(set())
            matchList[word]["path"].append(dict())
            for index in range(0, len(word)):
                wordhead = word[0:index]
                wordtrail = word[index+1:]
                charorder = ord(word[index:index+1])
                for char in range(97, 123):
                    if (char != charorder):
                        newword = wordhead + chr(char) + wordtrail
                        if (newword in wordList):
                            matchList[word]["complex"][0].add(newword)
                            matchList[word]["path"][0][newword] = [word]
                            #print("====find matched", word, "<=>", newword)
        print(printColour("|"))
        return matchList 
        
    #COMPILE ADD PAIRS TO DATA LIST ({})   
    def createPairList(dataList, wordList, complexity):        
        print(printColour(" |"), end="")    
        if (complexity<2):
            return
        lenDash = len(wordList)//(scrnWidth-4)
        count = 0
        for word in wordList:
            count +=1
            if (count % lenDash == 0):
                print(printColour("-"), end="")
            currcomplexity = 1
            #print("==============processing:", word)
            while(currcomplexity < complexity):
                dataList[word]["complex"].append(set())
                dataList[word]["path"].append(dict())
                for prevcomplexword in dataList[word]["complex"][currcomplexity-1]:
                    #print("word:", word," prev:",prevcomplexword, " match:",dataList[prevcomplexword]["complex"][0])
                    for complexword in dataList[prevcomplexword]["complex"][0]:
                        complexwordinshortpath = False
                        if (complexword == word):
                            complexwordinshortpath = True

                        for prevcomplex in range(0, currcomplexity):
                            if (complexword in dataList[word]["complex"][prevcomplex]):
                                complexwordinshortpath = True

                        if (complexwordinshortpath==False):
                            dataList[word]["complex"][currcomplexity].add(complexword)
                            dataList[word]["path"][currcomplexity][complexword] = (dataList[word]["path"][currcomplexity-1][prevcomplexword]+[prevcomplexword])
                            #print("find complex", currcomplexity+1, "from", word, "to prev", prevcomplexword, "to", complexword) 

                currcomplexity +=1
        print(printColour("|"))

            
    print(printColour("Loading pair words...".center(scrnWidth, " ")), end="")
    wordList = loadWordList(toUseDict)
    #wordList = loadWordList("Eng_dictionary.txt")
    #wordList = loadWordList("1000words.txt")
    print(printColour(((str(len(wordList))) +  " words loaded.").center(scrnWidth, " ")))
    
    print(printColour("Loading check words...".center(scrnWidth, " ")), end="")
    #checkWordList = loadWordList("1000words.txt")
    checkWordList = loadWordList("longWords.txt")
    #checkWordList = loadWordList(toUseDict)
    checkWordList = combineWordList(checkWordList, wordList)
    #print(checkWordList)
    #checkWordList = wordList
    print(printColour(((str(len(checkWordList))) +  " words loaded.").center(scrnWidth, " ")))
    
    print(printColour("Processing words...".center(scrnWidth, " ")), end="")
    dataList = findMatch(wordList)
    print(printColour(((str(len(dataList))) +  " words processed.").center(scrnWidth, " ")))
    
    print(printColour("Compiling words...".center(scrnWidth, " ")), end="")
    createPairList(dataList, wordList, complexity)
    print(printColour(((str(len(dataList))) +  " words compiled.").center(scrnWidth, " ")))
    
    return(dataList, checkWordList, wordList)
   
#Main Menu (Moving Cursor and Enter)
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
            #enterMenu(keyLoc)
            if keyLoc == 1:
                disInstruct()
            elif keyLoc == 2:
                gameMenu()
            else:
                print(printColour("Exiting Game...".center(scrnWidth, " ")))
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
    print(printColour("EASY: 1-2 Letter Changes".center(scrnWidth, " ")), end="")
    print(printColour("MEDIUM: 3-4 Letter Changes".center(scrnWidth, " ")), end="")
    print(printColour("HARD: 5-6 Letter Changes".center(scrnWidth, " ")), end="")
    print()
    print(printColour("Press <ENTER> to return to main menu.". center(scrnWidth," ")), end="")
    input()
    return

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
    #ENTER MENU - PRESS ENTER
    if keyLoc == 1:
        startGame(0)
    elif keyLoc == 2:
        startGame(1)
    elif keyLoc == 3:
        startGame(2)
    else:
        return

#Start New Game
def startGame(dif):

    global dataList
    
    if dif == 0:
        difMode = "EASY"
    elif dif == 1:
        difMode = "MEDIUM"
    else:
        difMode = "HARD"

    os.system("CLS")
    print("\n"*5)
    print(printColour(("Loading new game in " + difMode + " mode...").center(scrnWidth," ")))
    
    if dif == 0:
        wordLenList = [2,3,4]
        complexity = [0,1]
    elif dif == 1:
        wordLenList = [4,5,6,7,8,9]
        complexity = [2,3]
    else:
        wordLenList = [4,5,6,7,8,9]
        complexity = [4,5]
    pairList = preparePairList(wordLenList, complexity, dataList)
    pair = findRandomPair(pairList)
    #print("TESTING:", pair)
    print(printColour("Game is ready to begin... Press ENTER to continue.".center(scrnWidth, " ")))
    input()
    startSession(pair)
    return

#Start Playing Session
def startSession(matchPair):
    global attemptList
    
    os.system("CLS")
    startWord = matchPair[0]
    endWord = matchPair[1]
    path = matchPair[2]
    print(printColour("\n"*4))
    #print(printColour("Start:" + startWord))
    #print(printColour("End:" + endWord))
    #print(printColour(("Solution:", matchPair)))
    curLoc = 0
    curWord = startWord
    wordsTup = (startWord, [startWord.upper()], endWord, path) 
    gameCursor(wordsTup, 1)
    return

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
            #displaySession(wordsTup, curLoc, phase, alphaLoc, error, attmpWord)
            
        elif key == 77:
            if phase == 1:
                curLoc += 1
                if curLoc == wordLen:
                    curLoc = (wordLen-1)
            else:
                alphaLoc += 1
                if alphaLoc == alphaLen:
                    alphaLoc = 0   
            #displaySession(wordsTup, curLoc, phase, alphaLoc, error, attmpWord)
            
        elif key == 13:
            gameEnterButton(wordsTup, curLoc, alphaLoc, phase, moves)
            return
            
        elif key == 104:
            displaySession(wordsTup, curLoc, phase, alphaLoc, error, attmpWord, True)
            time.sleep(1)
            #os.system("CLS")
            #displaySession(wordsTup, curLoc, phase, alphaLoc, error, attmpWord)
        
        elif key == 109:
            #mainMenu()
            return
        
        else:
            pass  
            
        displaySession(wordsTup, curLoc, phase, alphaLoc, error, attmpWord)

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
            oldWord = wordsTup[1][-1]
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
            attempts = wordsTup[1]
            attempts.append(newWord)
            wordsTup = (wordsTup[0], attempts, wordsTup[2], wordsTup[3])
            if newWord.upper() == wordsTup[2].upper():
                os.system("CLS")
                displaySession(wordsTup, 0, 1)
                time.sleep(1)
                finishSession(moves, wordsTup)
                return
            moves += 1
            attemptList.append(newWord.upper())
            
            gameCursor(wordsTup, 1, 0, moves, False)
            return

#When User Finishes Puzzle            
def finishSession(moves, wordsTup):
    global attemptList

    os.system("CLS")
    print("\n"*4)
    printBoxed(["Congratulation! You've finished!"])
    print()
    print(printColour(("You got from " + wordsTup[0].upper() + " to " + wordsTup[2].upper()
    + " in " + str(moves+1) + " moves.").center(scrnWidth," ")))
    print()
    print(printColour(("Here are your moves: ").center(scrnWidth," ")))
    printBoxed(wordsTup[1])
    print()
    print(printColour(("Press ENTER to return to the main menu.").center(scrnWidth," ")))
    input()
    return
            
#Display Playing Session 
def displaySession(wordsTup, curLoc, phase, alphaLoc=0, error=False, attmpWord="", hint=False):
    
    os.system("CLS") 
    print(printColour(("\n"*4)))
    printBoxed([("Game In Progress")])
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
        
    if hint == True:
        printBoxed([str(wordsTup[3])])
    
    printBoxed([(wordsTup[1][-1].upper()), (" "*curLoc + "^" + " "*(len(wordsTup[0])-(curLoc+1)))])
    print()
    
    if phase > 1:
        letters = string.ascii_uppercase + "*"
        printBoxed([letters, (" "*alphaLoc + "^" + " "*(len(letters)-(alphaLoc+1)))])
    #print(printColour((wordsTup[1].upper()).center(scrnWidth, " ")), end="")
    #print(printColour((" "*curLoc + "^" + " "*(len(wordsTup[0])-curLoc)).center(scrnWidth, " ")))
    print()
    printBoxed(["End Word: " + (wordsTup[2]).upper()])
    
    print()
    print()
    print(printColour("Press M to Return to the Main Menu".center(scrnWidth, " ")))
    return

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

        
colorama.init()
complexity = 6
#os.system('color F3')

global attemptList
global checkWordList
global dif
global dataList

#toUseDict = "1000words.txt"
toUseDict = "Eng_dictionary.txt"

dif = 0
checkWordList = []
attemptList = []

os.system("CLS")

#preGameMenu()

start = time.time()
data = createData(complexity, toUseDict)
dataList = data[0]
checkWordList = data[1]
wordList = data[2]
end = time.time()

#print("TOTAL TIME", (end-start)/60)
#print("DONE")
print()
#print(dataList)
print()
print(printColour("All components loaded sucessfully.".center(scrnWidth, " ")))
print()
print(printColour("Press ENTER to start the game...".center(scrnWidth, " ")))
input()



introScreen = loadIntroScreen()
printIntroScreen()
#print("INTRO")
mainMenu()
               
