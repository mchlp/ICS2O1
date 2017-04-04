
#Final Project - Game
#Tank Wars
#Michael Pu & Samuel Liu
#ICS2O1
#2016/12/06
#SCREEN RESOLUTION: H 768 W 1366 1280 x 1024

import pygame
from pygame.locals import *  
import os
import time
import random

#SET UP GAME
def setupGame(resourcePath):

    #Loading Screen
    def dispalyLoading(screen):
        #Loading screen 
        loadingScreen = pygame.surface.Surface(size)
        loadingScreen.fill((100,100,100))
        #Loading screen background
        loadGameBGPic = pygame.image.load(resourcePath + "gameOverBackground.png").convert_alpha()
        loadGameBG = pygame.transform.scale(loadGameBGPic, size)
        loadGameBGRect = loadGameBG.get_rect()
        loadGameBGRect.center = loadingScreen.get_rect().center
        #Loading screen text
        loadFont = pygame.font.Font(resourcePath+"blackOpsOne.ttf", size[1]//7)
        loadFont2 = pygame.font.Font(resourcePath+"blackOpsOne.ttf", size[1]//20)
        loadText = loadFont.render("Loading Game...", True, (200,200,200))
        loadText2 = loadFont2.render("This may take a while.", True, (200,200,200))
        loadTextRect = loadText.get_rect()
        loadTextRect2 = loadText2.get_rect()
        loadTextRect.midtop = (loadGameBGRect.centerx, loadGameBGRect.centery-40-size[1]//7-size[1]//20)
        loadTextRect2.midtop = (loadGameBGRect.centerx, loadGameBGRect.centery-size[1]//20-10)
        
        #Blit to screen
        loadingScreen.blit(loadGameBG, loadGameBGRect)
        loadingScreen.blit(loadText, loadTextRect)
        loadingScreen.blit(loadText2, loadTextRect2)
        screen.blit(loadingScreen, (0,0))
        pygame.display.update()
        
        #return loadingScreen, y cord of bottom of text
        return (loadingScreen, loadTextRect2.bottom)
    
    #Screen when loading is finished
    def doneLoading(loadingScreen, lastTextBotttom):
        
        global fonts
        global colours
        #text
        loadFont = pygame.font.Font(fonts["bops1"], size[1]//25)
        loadText = loadFont.render("Loading Complete.", True, colours["light grey"])
        loadText2 = loadFont.render("Press any key or click to continue...", True, colours["light grey"])
        loadTextDash = loadFont.render("-----", True, colours["light grey"])
        loadTextRect = loadText.get_rect()
        loadTextRect2 = loadText2.get_rect()
        loadTextDashRect = loadTextDash.get_rect()
        loadTextDashRect.midtop = (screen.get_rect().centerx, lastTextBotttom+30)
        lastTextBotttom += loadTextDashRect.height+30
        loadTextRect.midtop = (screen.get_rect().centerx, lastTextBotttom+10)
        lastTextBotttom += loadTextRect.height+10
        loadTextRect2.midtop = (screen.get_rect().centerx, lastTextBotttom+10)
        
        #keep going flag
        keepGoing = True
        
        #speed at which the text flashes
        flashLimit = fpsRate*0.8
        flashCounter = flashLimit
        visible = True
        
        while keepGoing:
            #fps rate
            clock.tick(fpsRate)
            
            #if flash counter is up
            if flashCounter <= 0:
                #cover up old screen
                screen.blit(loadingScreen, (0,0))
                screen.blit(loadTextDash, loadTextDashRect)
                screen.blit(loadText, loadTextRect)
                
                if not visible:
                    #show text
                    screen.blit(loadText2, loadTextRect2)
                    visible = True
                else:
                    #do not show text
                    visible = False
                flashCounter = flashLimit    
            flashCounter -= 1
            
            #check for key or mouse down
            for ev in pygame.event.get():
                if ev.type == pygame.KEYDOWN:
                    keepGoing = False
                    break
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if ev.button == 1 or ev.button == 3 or ev.button == 2:
                        keepGoing = False
                        break
            pygame.display.update()        
            

    def testRes(squareSize, fontSize, displayW, displayH):
        spacing = displayH//100
        #test screen display
        testScreen = pygame.display.set_mode((displayW,displayH), pygame.FULLSCREEN)
        testScreen.fill((255,128,0))
        
        #instruction text
        instructFont = pygame.font.Font(resourcePath+"calibril.ttf", int(fontSize*1.5))
        explainFont = pygame.font.Font(resourcePath+"calibril.ttf", fontSize)
        instructText = instructFont.render("Testing the full screen compatability of your screen...", True, (0,0,0))
        instructText2 = explainFont.render("Press ESCAPE if any part of the screen is not visible.", True, (0,0,0))
        instructRect = instructText.get_rect()
        instructRect2 = instructText2.get_rect()
        imageBottom = spacing*4
        instructRect.midtop = (displayW//2, imageBottom+spacing)
        imageBottom += instructRect.h+spacing
        instructRect2.midtop = (displayW//2, imageBottom+spacing)
        imageBottom += instructRect.h+spacing
        testScreen.blit(instructText, instructRect)
        testScreen.blit(instructText2, instructRect2)
        
        #test image
        #trImage = pygame.image.load(resourcePath+"checkerboard.png")
        trImage = pygame.image.load(resourcePath+"testRes.jpg")
        trImage = pygame.transform.scale(trImage, (squareSize,squareSize))
        trImageRect = pygame.Rect(trImage.get_rect())          
        trImageRect.midtop = (displayW//2,imageBottom+spacing*2)
        imageBottom += trImageRect.h+spacing*2
        testScreen.blit(trImage, trImageRect)
        
        explainText = explainFont.render("Are the side lengths of the shape above equal AND the orange background fills the entire screen?", True, (0,0,0))
        explainRect = explainText.get_rect()
        explainRect.midtop = (displayW//2, imageBottom+spacing*3)
        imageBottom += explainRect.h+spacing*3
        testScreen.blit(explainText, explainRect)
        #display buttons
        yesButton = pygame.image.load(resourcePath+"yButton.png")
        noButton = pygame.image.load(resourcePath+"nButton.png")
        yRect = yesButton.get_rect()
        yRect.center = ((displayW//3)*1,imageBottom+spacing*5)
        nRect = noButton.get_rect()
        nRect.center = ((displayW//3)*2,imageBottom+spacing*5)
        testScreen.blit(yesButton, yRect)
        testScreen.blit(noButton, nRect)
        #update display
        pygame.display.flip()
        #get button press
        while True:
            for ev in pygame.event.get():
                if ev.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    #yes button
                    if yRect.collidepoint(pos):
                        return True
                    #no button
                    elif nRect.collidepoint(pos):
                        return False
                elif ev.type == KEYDOWN:
                    if ev.key == K_ESCAPE:
                        #escape button
                        return False

    #Set up screen
    def setupDisplay():
        global screen
        global images
        global size
        import platform
        
        #Window top y position
        winYPos = 50
        
        #Check Resolution for Full Screen
        checkFullScreenRes = False
        
        #Detect Display Info
        displayInfo = pygame.display.Info()
        displayH = displayInfo.current_h
        displayW = displayInfo.current_w

        #TEMP TESTING
        #displayW = 640
        #displayH = 480
        #displayH = 768
        #displayW = 1366
        #TEMP TESTING
        
        print("SCREEN RESOLUTION:", "H", displayH, "W", displayW)
        
        gameH = displayH-200
        gameW = displayW-20
        
        #Set Screen Size
        if gameH == -1 or gameW == -1:
            size = (1366,768)
            os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (winYPos, winYPos)
            #default size
        else:
            #round to nearest 25 pixels 
            gameW = gameW - gameW%25
            gameH = gameH - gameH%25 + 75
            
            if gameH > 1600 or gameW > 1600:
                #screen larger than background image
                size = (min(1600, gameW), min(1600, gameH))
                #center opening window
                os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (displayW//2-min(1600, gameW)//2, winYPos)
                screen = pygame.display.set_mode(size) 
            else:
                if checkFullScreenRes:
                #check for full screen resolution compatability
                    ynGoodRes = testRes(((min(displayW, displayH))//5)*2, displayH//35, displayW, displayH)
                    if ynGoodRes:
                        #full screen
                        size = (displayW, displayH)
                        screen = pygame.display.set_mode(size, pygame.FULLSCREEN) 
                    else:
                        #not full screen
                        size = (gameW, gameH)
                        #center opening window
                        os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (displayW//2-gameW//2, winYPos)
                        screen = pygame.display.set_mode(size)
                else:
                    #not full screen
                    size = (gameW, gameH)
                    #center opening window
                    os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (displayW//2-gameW//2, winYPos)
                    screen = pygame.display.set_mode(size)
            #size = (gameW, gameH)
            print(size)
            
        if platform.system() == "Windows":
            #os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])
            #os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (displayW//2-gameW//2,1)
            #os.environ['SDL_VIDEO_CENTERED'] = '1'
            os.environ['SDL_VIDEODRIVER'] = 'windib'  
        
        #caption
        pygame.display.set_caption("Tank Wars")
        #TEMP
        #icon 
        pygame.display.set_icon(pygame.image.load(resourcePath+"icon.png"))
        screen.fill((100,100,100))
        return screen

    #Open Images
    def loadImages():
        global images
        images = {}
        
        directions = ["U", "D", "L", "R"]
        #one image list
        oImageList = {"trImage":"testRes.jpg", "bgImage":"dirt.jpg", "tank1Temp":"tank1.png", "wall":"wall2.png", "bWall":"bWall.png"
        ,"ammo":"ammo.png", "heart":"heart.png", "skull":"skull.png", "blank":"blank.png", "ghost":"ghost.png", "GObg":"gameOverBackground.png"
        ,"LBbg":"gameOverLeaderboardBackground.png", "rankSlot":"rankSlot.png", "rankingTitleBG":"titleSlot.png", "rankSlotTitle":"rankSlotTitle.png"
        ,"shotsFired":"shotsFired.png", "shotsHit":"shotsHit.png", "accuracy":"accuracy.png", "shotsTaken":"shotsTaken.png", "netDamage":"netDamage.png"
        ,"time":"time.png" ,"help":"help.png", "helpLong":"helpLong.png", "rankingBlank":"rankingBlank.png", "pauseFull":"pauseFull.png", "powerUp":"powerUp.png"
        ,"pauseFade":"pauseFade.png", "playFull":"playFull.png", "settingsBG":"settingsBG.png"}
        
        #direction image list (4 images)
        dImageList = {"missile":"missile.png", "bWall":"bWall.png"}
        
        #add buttons to image list
        for button in ["restart", "mainMenu", "playAgain", "quit"]:
            oImageList[button+"But"] = button+".png"
            oImageList[button+"ButSel"] = button+"Sel.png"
        
        #add power ups to image list
        for powerUp in ["Ammo", "Speed", "DoubleLife"]:
            oImageList["pu"+powerUp] = "pu"+powerUp+".png"
        oImageList["puAmmoImage"] = "puAmmoImage.png"
        
        #add cracked wall to image list
        for cWall in range(1, 3+1):
            oImageList["wallCracked"+str(cWall)] = "wall2Crack"+str(cWall)+".png"
        
        #add tanks to image list
        for tankNum in range(4+1):
            dImageList["tank"+str(tankNum)] = "tank"+str(tankNum)+".png"
            oImageList["tank"+str(tankNum)] = "tank"+str(tankNum)+".png"
        
        #load one images
        for loadOImage in oImageList:
            images[loadOImage] = pygame.image.load(resourcePath + oImageList[loadOImage]).convert_alpha()
        #load direction images
        for loadDImage in dImageList:
            for direct in directions:
                dot = dImageList[loadDImage].find(".")
                fileName = dImageList[loadDImage][:dot] + direct + dImageList[loadDImage][dot:]
                images[loadDImage+direct] = pygame.image.load((resourcePath + fileName)).convert_alpha()
        #load explosion frames
        for explosionImage in range(1, 19+1):
            images["explosion"+str(explosionImage)] = pygame.image.load(resourcePath + "explosion (" + str(explosionImage) + ").gif")
            images["sExplosion"+str(explosionImage)] = pygame.image.load(resourcePath + "sExplosion (" + str(explosionImage) + ").png")
            
    #Load Maps
    def loadMap():
        global maps
        maps = {}
        #open map file
        mapFile = open(resourcePath + "mapDataBase.txt")
        addData = False
        for line in mapFile:
            line = line.strip()
            if line == "***":
                #new map
                if addData:
                #end of map
                    addData = False
                    maps[mapCount] = curMap
                else:
                #start of map
                    addData = True
                    curMap = []
                continue
            elif addData:
                if line in "1234567890":
                    #map number
                    mapCount = int(line)
                else:
                    #add line to current map list
                    curMap.append(line) 

    def loadSounds():
        global sounds
        sounds = {}
        soundListWAV = {"smallExplosion":"smallExplosion.wav", "bigExplosion":"bigExplosion.wav", "shoot":"pew.wav", "powerUp":"powerUp.wav"
        ,"victory":"victory.wav", "leaderboard":"leaderboard.wav", "countDown":"cwBeep.wav", "countDownFin":"cwFinBeep.wav"}
        for sound in soundListWAV:
            sounds[sound] = pygame.mixer.Sound(resourcePath + soundListWAV[sound])
            
    def loadFonts():
        global fonts
        fonts = {}
        fontList = {"bops1":"blackOpsOne.ttf", "tankFont":"tankFont.ttf", "roboto":"roboto.ttf", "openSans":"openSans.ttf"}
        for font in fontList:
            fonts[font] = resourcePath + fontList[font]
            
    def loadColours():
        global colours
        colours = {"black":(0,0,0), "white":(255,255,255), "grey":(128,128,128), "silver":(192,192,192),
        "light grey":(200,200,200), "dark grey":(50,50,50)}
    
    setupDisplay()
    
    #loading screen
    returnData = dispalyLoading(screen)
    lastTextBotttom = returnData[1]
    loadingScreen = returnData[0]
    
    loadImages()
    loadMap()
    loadSounds()
    loadFonts()
    loadColours()  
    
    #done loading screen
    doneLoading(loadingScreen, lastTextBotttom)

def startGame(resourcePath, mapNum, numPlayer, bgMusicName, score, returnMainMenu):
    global screen
    global images
    global sounds
    global size
    global fonts
    global colours
    
    def preGameStart(gameScreen):
        global fonts
        global screen
        global sounds
        #countdown from number (default 3)
        countDownLimit = 3
        #text
        countDownFont = pygame.font.Font(fonts["bops1"], size[1]//5)
        #background
        preGameBG = pygame.transform.scale(images["GObg"], size)
        preGameBGRect = preGameBG.get_rect()
        preGameBGRect.center = screen.get_rect().center
        #set countdown tracker
        countDownNum = countDownLimit
        countDownNumLen = 0
        #1 second = fpsRate ticks
        countDownNumLenLimit = fpsRate
        
        while countDownNum >= 0:
            #Set up fps rate
            clock.tick(fpsRate)
            
            #check for events
            for ev in pygame.event.get():
                pass
                
            #text
            if countDownNum > 0: 
                #countdown number
                if countDownNumLen == 0:
                    sounds["countDown"].play()
                text = str(countDownNum)
            else:
                #countdown finished --> Start!
                if countDownNumLen == 0:
                    sounds["countDownFin"].play()
                text = "Start!"
            
            countDownText = countDownFont.render(text, True, colours["light grey"])
            countDownRect = countDownText.get_rect()
            countDownRect.center = screen.get_rect().center
            
            #blit images to screen
            screen.blit(gameScreen, (0,0))
            screen.blit(preGameBG, preGameBGRect)
            screen.blit(countDownText, countDownRect)
            pygame.display.update()
            
            countDownNumLen += 1
            
            #countdown counter done --> next number
            if countDownNumLen > countDownNumLenLimit:
                countDownNumLen = 0
                countDownNum -= 1
    
    #Game Over Function   
    def gameOver(ranking, gameScreen, returnMainMenu):
        global screen
        global fonts
        global prevSlotYPos
        
        #create groups
        leadrbrdMouseGroup = pygame.sprite.Group()
        leadrbrdGroup = pygame.sprite.Group()
        leadrbrdObjGroup = pygame.sprite.Group()
        
        #rankings slot
        class rankingSlot(pygame.sprite.Sprite):
        
            #title slot
            class rankingTitle(pygame.sprite.Sprite):
                def __init__(self, obj, col, slot):
                    self.slot = slot
                    self.col = col
                    pygame.sprite.Sprite.__init__(self)
                    #text
                    self.font = pygame.font.Font(fonts["roboto"], 15)
                    self.titleText = self.font.render(obj[0], True, colours["black"])
                    self.titleImage = obj[1]
                    self.image = self.titleImage
                    self.rect = self.image.get_rect()
                    self.rect.center = (75*(self.col-1)+30+self.slot.rect.left, self.slot.rect.centery)
                
                #check if mouse collides with slot
                def update(self, mousePos):
                    #check if mouse is colliding with the heading image
                    if self.rect.collidepoint(mousePos):
                        #text - collide
                        self.image = self.titleText
                    else:
                        #image - no collide
                        self.image = self.titleImage
                    self.rect = self.image.get_rect()
                    self.rect.center = (75*(self.col-1)+30+self.slot.rect.left, self.slot.rect.centery)
                    
                    
            #player slots
            class rankingText(pygame.sprite.Sprite):
                #text
                def __init__(self, text, col, slot):
                    pygame.sprite.Sprite.__init__(self)
                    self.col = col
                    self.slot = slot
                    self.font = pygame.font.Font(fonts["roboto"], 25)
                    self.image = self.font.render(text, True, colours["light grey"])
                    self.rect = self.image.get_rect()
                    self.rect.center = (75*(self.col-1)+30+self.slot.rect.left, self.slot.rect.centery)
                    
            #player images
            class rankingImage(pygame.sprite.Sprite):
                def __init__(self, num, image, col, slot):
                    pygame.sprite.Sprite.__init__(self)
                    self.num = num
                    self.slot = slot
                    self.col = col
                    #image
                    self.tankImage = image
                    self.image = self.tankImage
                    self.rect = self.image.get_rect()
                    self.rect.center = (75*(self.col-1)+30+self.slot.rect.left, self.slot.rect.centery)
                    #text
                    self.font = pygame.font.Font(fonts["roboto"], 20)
                    self.text = self.font.render("Player "+str(self.num), True, colours["light grey"])
              
                #check if mouse collides with image
                def update(self, mousePos):
                    if self.rect.collidepoint(mousePos):
                        #display text - collide
                        self.image = self.text
                    else:
                        #display image - no collide
                        self.image = self.tankImage
                    self.rect = self.image.get_rect()
                    self.rect.center = (75*(self.col-1)+30+self.slot.rect.left, self.slot.rect.centery)
                    
            def __init__(self, bgRect, data, place=None):
                #create slots
                global prevSlotYPos
                pygame.sprite.Sprite.__init__(self)
                self.bg = bgRect
                #slot spacing
                self.spacing = 10
                
                if data["num"] == 0:
                    #headings slot
                    self.image = images["rankSlotTitle"]
                    self.rect = self.image.get_rect()
                    self.rect.midtop = (self.bg.midtop[0], prevSlotYPos+self.spacing)
                    prevSlotYPos += self.image.get_height()+self.spacing
                    #headings text
                    self.data = []
                    self.data.append(("Rank", images["rankingBlank"]))
                    self.data.append(("Tank", images["rankingBlank"]))
                    self.data.append(("Shots Fired", images["shotsFired"]))
                    self.data.append(("Shots Hit", images["shotsHit"]))
                    self.data.append(("Accuracy", images["accuracy"]))
                    self.data.append(("Shots Taken", images["shotsTaken"]))
                    self.data.append(("Power Ups", images["powerUp"]))
                    self.data.append(("Time", images["time"]))
                    #for heading in headings text list --> create raknkingTitle object
                    for num, titleObj in enumerate(self.data):
                        newObj = self.rankingTitle(titleObj, num+1, self)
                        leadrbrdMouseGroup.add(newObj)
                        leadrbrdObjGroup.add(newObj)
                    
                else:
                    self.image = images["rankSlot"]
                    self.rect = self.image.get_rect()
                    self.rect.midtop = (self.bg.midtop[0], prevSlotYPos+self.spacing)
                    prevSlotYPos += self.image.get_height()+self.spacing
                    self.data = []
                    #place
                    self.data.append(str(place))
                    #tank image
                    self.data.append(images["tank"+str(data["num"])])
                    #shots fired
                    self.data.append(str(data["shots"]))
                    #shots hit
                    self.data.append(str(data["kills"]))
                    #accuracy
                    if data["shots"] > 0:
                        self.data.append("%.1f%s" %(data["kills"]/data["shots"]*100, "%"))
                    else:
                        self.data.append("0%")
                    #damage taken
                    self.data.append(str(data["damage"]))
                    #power ups
                    self.data.append(str(data["powerUps"]))
                    #time survived
                    if type(data["time"]) == float:
                        self.data.append(str(int(data["time"]//60))+":"+str(data["time"]%60).zfill(2))
                    else:
                        self.data.append(data["time"])
                    #create objects for each info object
                    for num, infoObj in enumerate(self.data):
                        if type(infoObj) != str:
                            newObj = self.rankingImage(data["num"], infoObj, num+1, self)
                            leadrbrdMouseGroup.add(newObj)
                        else:
                            newObj = self.rankingText(infoObj, num+1, self)
                        leadrbrdObjGroup.add(newObj)
                        
        class helpButton(pygame.sprite.Sprite):
            #help button
            class helpText(pygame.sprite.Sprite):
                def __init__(self, helpBox, text):
                    self.text = text
                    self.helpBox = helpBox
                    pygame.sprite.Sprite.__init__(self)
                    #text
                    self.font = pygame.font.Font(fonts["openSans"], 25)
                    self.image = self.font.render(self.text, True, colours["white"])
                    self.rect = self.image.get_rect()
                    self.rect.midleft = (self.helpBox.rect.left+images["help"].get_rect().right+10,
                    self.helpBox.rect.top+self.helpBox.image.get_rect().height//2)
                       
            def __init__(self, text, bgRect):
                #image, button
                global prevSlotYPos
                pygame.sprite.Sprite.__init__(self)
                self.prevSlotYPos = prevSlotYPos
                self.expanded = False
                self.bgRect = bgRect
                #image
                self.image = images["help"]
                self.rect = self.image.get_rect()
                self.rect.topleft = (self.bgRect.left, self.prevSlotYPos+10)
                prevSlotYPos += self.rect.height+10
                self.text = self.helpText(self, text)
                
            def update(self, mousePos):
                #check if mouse if colliding with help button
                if self.rect.collidepoint(mousePos):
                    #expand
                    self.image = images["helpLong"] 
                    leadrbrdObjGroup.add(self.text)
                else:
                    #shrink
                    self.image = images["help"] 
                    leadrbrdObjGroup.remove(self.text)
                self.rect = self.image.get_rect()
                self.rect.topleft = (self.bgRect.left,self.prevSlotYPos+10)
                
        class bottomButtons(pygame.sprite.Sprite):
            def __init__(self, type):
                pygame.sprite.Sprite.__init__(self)
                self.type = type
                self.selImage = images[self.type+"ButSel"]
                self.unSelImage = images[self.type+"But"]
                self.image = self.unSelImage
                self.rect = self.image.get_rect()
                
            def update(self, mousePos):
                if self.rect.collidepoint(mousePos):
                    self.image = self.selImage
                else:
                    self.image = self.unSelImage
                    
            def clicked(self):
                if self.type == "restart":
                    pygame.mixer.music.stop()
                    pygame.mixer.stop()
                    for player in score:
                        score[player] = 0
                    startGame(resourcePath, mapNum, numPlayer, bgMusicName, score, returnMainMenu)
                if self.type == "mainMenu":
                    pass
                    #RETURN TO MAIN MENU
                    #TEMP
                if self.type == "playAgain":
                    pygame.mixer.music.stop()
                    pygame.mixer.stop()
                    startGame(resourcePath, mapNum, numPlayer, bgMusicName, score, returnMainMenu)
                if self.type == "quit":
                    pygame.quit()
                    exit()
                
        #play victory sound
        sounds["victory"].play()
        
        #game over leaderboard background
        gameOverLB = images["LBbg"]
        gameOverLBRect = gameOverLB.get_rect()
        gameOverLBRect.center = screen.get_rect().center
        
        #game over background
        gameOverBG = pygame.transform.scale(images["GObg"], size)
        gameOverBGRect = gameOverBG.get_rect()
        gameOverBGRect.center = screen.get_rect().center
        
        #scoreboard (top)
        global prevSlotYPos
        prevSlotYPos = (gameOverLBRect.top+10)
        #prevSlotYPos = rankingRect.bottom
        
        #ranking title text
        rankingFont = pygame.font.Font(fonts["bops1"],35)
        rankingSur = rankingFont.render("Rankings", True, colours["light grey"])
        rankingRect = rankingSur.get_rect()
        rankingRect.midtop = (gameOverLBRect.centerx, prevSlotYPos)
        rankingTitleBG = images["rankingTitleBG"]
        rankingTitleRect = rankingTitleBG.get_rect()
        rankingTitleRect.center = rankingRect.center
        prevSlotYPos += rankingRect.height
        
        #leaderboard slots
        leadrbrdGroup.add(rankingSlot(gameOverLBRect ,{"num":0}))
        ranking.reverse()
        #add players to scoreboard
        for place, player in enumerate(ranking):
            leadrbrdGroup.add(rankingSlot(gameOverLBRect, player, place+1))
            score[player["num"]] += numPlayer-(place+1)
        print(score)
        
        #add help button
        rankingsHelpButton = helpButton("Mouse Over Images for Explanation", gameOverLBRect)    
        leadrbrdMouseGroup.add(rankingsHelpButton)
        leadrbrdGroup.add(rankingsHelpButton)
        #prevSlotYPos += rankingsHelpButton.rect.bottom
        
        #bottom button bar
        bottomButtonBar = []
        prevSlotYPos += 10
        buttonSpacing = 10
        leadrbrdButRestart = bottomButtons("restart")
        leadrbrdButPlayAgain = bottomButtons("playAgain")
        if returnMainMenu:
            leadrbrdButMainMenu = bottomButtons("mainMenu")
        else:
            leadrbrdButMainMenu = bottomButtons("quit")
        
        leadrbrdButMainMenu.rect.midtop = (gameOverLBRect.centerx, prevSlotYPos)
        leadrbrdButPlayAgain.rect.topleft = (leadrbrdButMainMenu.rect.right+buttonSpacing, prevSlotYPos)
        leadrbrdButRestart.rect.topright = (leadrbrdButMainMenu.rect.left-buttonSpacing, prevSlotYPos)

        leadrbrdMouseGroup.add(leadrbrdButMainMenu)
        leadrbrdMouseGroup.add(leadrbrdButPlayAgain)
        leadrbrdMouseGroup.add(leadrbrdButRestart)
        leadrbrdGroup.add(leadrbrdButMainMenu)
        leadrbrdGroup.add(leadrbrdButPlayAgain)
        leadrbrdGroup.add(leadrbrdButRestart)
        bottomButtonBar.append(leadrbrdButMainMenu)
        bottomButtonBar.append(leadrbrdButPlayAgain)
        bottomButtonBar.append(leadrbrdButRestart)
      
        #show leaderboard flag
        showLeaderboard = True
        
        while showLeaderboard:
            #Set up fps rate
            clock.tick(fpsRate)
            
            #fill background
            screen.fill((100,100,100))
            
            #check if sound is being player
            if not pygame.mixer.get_busy():
                sounds["leaderboard"].play(loops=-1)
            
            for ev in pygame.event.get():
                #Exit Button
                if ev.type == pygame.QUIT:
                    keepGoing = False
                if ev.type == pygame.KEYDOWN:
                    if ev.key == K_ESCAPE:
                        keepGoing = False
                        break
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if ev.button == 1:
                        for button in bottomButtonBar:
                            if button.rect.collidepoint(ev.pos):
                                button.clicked()
                    
            #get mouse position
            mousePos = pygame.mouse.get_pos()
            
            #update mouse sensitive sprites
            leadrbrdMouseGroup.update(mousePos) 
            
            #blit stuff to screen
            screen.blit(gameScreen, (0,0))
            screen.blit(gameOverBG, gameOverBGRect)
            screen.blit(gameOverLB, gameOverLBRect)
            screen.blit(rankingTitleBG, rankingTitleRect)
            screen.blit(rankingSur, rankingRect)
            
            #draw background images
            leadrbrdGroup.draw(screen)
            #draw foreground images
            leadrbrdObjGroup.draw(screen)
            
            pygame.display.flip()

    #Set up keepGoing flag
    keepGoing = True

    #Setup game screen
    gameScreen = pygame.surface.Surface(size)
    
    class Tank(pygame.sprite.Sprite):      
        def __init__(self, x, y, num, numPlayer, powerUpList, settings):
            self.num = num
            self.tankNum = self.num
            #set up tank settings
            #player:[ammo, life]
            self.settings = settings
            self.dead = False
            self.face = "R"
            self.totalPlayer = numPlayer
            self.missileRegenTime = 2
            self.missileRegenCount = 0
            self.missileLimit = self.settings[0]
            self.missileLeft = self.missileLimit
            self.moveRate = 3  
            self.defaultMoveRate = self.moveRate
            self.lives = self.settings[1]
            self.imageNum = str(self.tankNum)
            self.powerUpTime = 10
            self.totalShot = 0
            self.hitShot = 0
            self.damage = 0
            self.powerUpCount = 0
            self.ghost = False
            self.addedToRankList = False
            self.moveList = []
            if self.num == 1:
                self.ghost = True
                
            #power up status
            self.powerUpStatus = {}
            for powerUp in powerUpList:
                self.powerUpStatus[powerUp] = False
   
            #create tank
            pygame.sprite.Sprite.__init__(self)
            self.image = images["tank"+self.imageNum+"R"]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = getYCord(y)
            #set previous direction
            self.prevFace = "R"
            
        def move(self, deltaX, deltaY):
            self.deltaX = deltaX*self.moveRate
            self.deltaY = deltaY*self.moveRate
            #set temp in case of collision
            self.tempRect = self.rect.copy()
            self.tempImage = self.image
            #add change
            self.rect.x += self.deltaX
            self.rect.y += self.deltaY
            self.image = images["tank"+self.imageNum+self.face]
            #get new dimensions
            self.rect.width = self.image.get_width()
            self.rect.height = self.image.get_height()
            #move tank
            if self.prevFace == "R":
                if self.face == "D": 
                    self.rect.topright = self.tempRect.topright
                if self.face == "U":
                    self.rect.bottomright = self.tempRect.bottomright
            if self.prevFace == "L":
                if self.face == "D": 
                    self.rect.topleft = self.tempRect.topleft
                if self.face == "U":
                    self.rect.bottomleft = self.tempRect.bottomleft
            if self.prevFace == "U":      
                if self.face == "L":
                    self.rect.topright = self.tempRect.topright
                if self.face == "R":
                    self.rect.topleft = self.tempRect.topleft
            if self.prevFace == "D":
                if self.face == "L":
                    self.rect.bottomright = self.tempRect.bottomright
                if self.face == "R":
                    self.rect.bottomleft = self.tempRect.bottomleft
                    
            #create temp tank group without current tank
            tempTankGroup = tankGroup.copy()
            tempTankGroup.remove(self)
            
            #check for collision with missile
            if pygame.sprite.spritecollide(self, wallGroup, False):
                #revert to temp settings
                self.rect.x = self.tempRect.x
                self.rect.y = self.tempRect.y
                self.image = self.tempImage
                self.face = self.prevFace
            #check for collision with other tank
            elif pygame.sprite.spritecollide(self, tempTankGroup, False):
                #revert to temp settings
                self.rect.x = self.tempRect.x
                self.rect.y = self.tempRect.y
                self.image = self.tempImage
                self.face = self.prevFace
            else:
                #confirm movement
                self.prevFace = self.face
                
        def launch(self):
            #missile powerup --> missileLeft = -1
            if self.missileLeft == -1 or self.missileLeft > 0:
                self.totalShot += 1
                if self.missileLeft > 0:
                    self.missileLeft -= 1
                missileGroup.add(Missile(self, self.face))
                print("LAUNCH MISSILE BY TANK", self.num, self.missileLeft, "MISSILES LEFT")
                
                                             
        def collide(self, colMissile):
            #if collide with missile
            explosionGroup.add(Explosion(self, "Tank"))
            self.lives -= 1
            self.damage += 1
            print("COLLIDE WITH TANK", self.num, "-", self.lives, "LIVES LEFT")
            
        def addToRankings(self):
            global playerRank
            global gameTimeCounter
            
            #add tank to rankings list
            if not self.addedToRankList:
                #dead tank
                if self.dead:
                    self.addedToRankList = True
                    playerRank.append({"num":self.num, "shots":self.totalShot, "kills":self.hitShot,
                    "damage":self.damage, "time":(gameTimeCounter/60), "powerUps":self.powerUpCount})
                #final alive tank
                else:
                    self.addedToRankList = True
                    playerRank.append({"num":self.num, "shots":self.totalShot, "kills":self.hitShot,
                    "damage":self.damage, "time":"-", "powerUps":self.powerUpCount})
            
                
        def update(self):
            global tankStat
            #regen missile coutner
            if not self.dead and self.missileLeft != -1:
                self.missileRegenCount += 1
                if self.missileRegenCount >= self.missileRegenTime*fpsRate:
                    if self.missileLeft < self.missileLimit:
                        self.missileLeft += 1
                        print("MISSILE REGEN")
                    self.missileRegenCount = 0
                
            #check if lives are out
            if self.lives <= 0:
                if not self.dead:
                    self.dead = True
                    self.addToRankings()
                if not self.ghost:
                    self.kill()
                    tankDict.pop(self.num)
                else:
                    self.image = images["blank"]
                    if self.missileLeft <= 1:
                        self.missileLeft += 1   
            tankStat.append(self.dead) 
                          
            #check for power ups
            for powerUp in self.powerUpStatus:
                if not self.powerUpStatus[powerUp] is False:
                    if powerUp == "ammo":
                        if self.powerUpStatus[powerUp] is True:
                            self.powerUpStatus[powerUp] = self.powerUpTime*fpsRate
                            self.missileLeft = -1  
                        elif self.powerUpStatus[powerUp] <= 0:
                            self.missileLeft = self.missileLimit
                            self.powerUpStatus[powerUp] = False
                        else:
                            self.powerUpStatus[powerUp] -= 1  
                    if powerUp == "speed":
                        if self.powerUpStatus[powerUp] is True:
                            self.powerUpStatus[powerUp] = self.powerUpTime*fpsRate
                            self.moveRate = self.defaultMoveRate+2
                        elif self.powerUpStatus[powerUp] <= 0:
                            self.moveRate = self.defaultMoveRate
                            self.powerUpStatus[powerUp] = False
                        else:
                            self.powerUpStatus[powerUp] -= 1     
                    if powerUp == "doubleLife":
                        if self.powerUpStatus[powerUp] is True:
                            self.lives *= 2
                            if self.lives > self.settings[1]:
                                self.lives = self.settings[1]
                            self.powerUpStatus[powerUp] = False
           
    class Explosion(pygame.sprite.Sprite):
        def __init__(self, colObj, type, othObj=0):
            #create explosion
            self.type = type
            print(self.type)
            self.frameRate = 2
            self.frame = self.frameRate
            pygame.sprite.Sprite.__init__(self)
            if self.type == "Tank":
                #play explosion sound
                sounds["bigExplosion"].play()
                self.image = images["explosion1"]
                self.rect = self.image.get_rect()
                self.rect.center = colObj.rect.center
            elif self.type == "Missile":
                #play explosion sound
                sounds["smallExplosion"].play()
                self.image = images["sExplosion1"]
                self.rect = self.image.get_rect()
                posObj1 = colObj.rect.center
                posObj2 = othObj.rect.center
                #Get Midpoint between two missiles
                midPoint = (posObj2[0]+((posObj1[0]-posObj2[0])//2), posObj2[1]+((posObj1[1]-posObj2[1])//2))
                self.rect.center = midPoint
            
        def update(self):
            #update explosion 
            if self.frame <= 18*self.frameRate:
                if self.type == "Tank":
                    self.image = images["explosion"+str((self.frame//self.frameRate)+1)]
                elif self.type == "Missile":
                    self.image = images["sExplosion"+str((self.frame//self.frameRate)+1)]
                self.frame += 1
            else:
                self.kill()
    
    class Missile(pygame.sprite.Sprite): 
        def __init__(self, tank, face):
            self.missileRate = 10
            #PLAY PEW SOUND
            #sounds["shoot"].play()
            #create missile
            self.tank = tank
            self.tankX = self.tank.rect.x
            self.tankY = self.tank.rect.y
            missileLaunch = {"R":(75, 25), "U":(25,0), "L":(0,25), "D":(25,75)}
            self.face = face
            self.bounceCount = 0
            pygame.sprite.Sprite.__init__(self)
            self.image = images["missile"+face]
            self.rect = self.image.get_rect()
            if self.face == "U":
                self.rect.midbottom = (self.tankX+(missileLaunch[self.face][0]), self.tankY+(missileLaunch[self.face][1]))
            if self.face == "D":
                self.rect.midtop = (self.tankX+(missileLaunch[self.face][0]), self.tankY+(missileLaunch[self.face][1]))
            if self.face == "R":
                self.rect.midleft = (self.tankX+(missileLaunch[self.face][0]), self.tankY+(missileLaunch[self.face][1]))
            if self.face == "L":
                self.rect.midright = (self.tankX+(missileLaunch[self.face][0]), self.tankY+(missileLaunch[self.face][1]))
                
            collideWall = pygame.sprite.spritecollide(self, wallGroup, False)            
            if collideWall:
                self.bounce(collideWall[0])     
            else:
                self.move(self.missileRate)
            
        def bounce(self, collideWall):
            #When the missile bounces
            bounceLimit = 0
            wallExplosion = True
            if self.bounceCount < bounceLimit:
                bounceList = {"U":"D", "D":"U", "L":"R", "R":"L"}
                self.face = bounceList[self.face]
                self.bounceCount += 1
                print("Bounce", self.bounceCount, "of", bounceLimit)
                while pygame.sprite.spritecollide(self, wallGroup, False):
                    self.move(1)
            else:
                if collideWall.destroyable:
                    collideWall.hit()
                if wallExplosion:
                    explosionGroup.add(Explosion(self, "Missile", self))
                self.kill()
            
        def update(self):    
            tempMissileGroup = missileGroup.copy()
            tempMissileGroup.remove(self)
            #check for collision with missile
            #Check for collision with double missile size (ratio)
            colObjList = pygame.sprite.spritecollide(self, tempMissileGroup, True, pygame.sprite.collide_rect_ratio(2))
            if colObjList:
                for colObj in colObjList:
                    colObj.kill()
                    explosionGroup.add(Explosion(colObj, "Missile", self))
                    self.kill()
                    
            #check for collision with tanks
            tankColList = pygame.sprite.spritecollide(self, tankGroup, False)
            if tankColList:
                for colTank in tankColList:
                    if colTank != self.tank:
                        self.tank.hitShot += 1 
                    colTank.collide(self)
                    self.kill()
                    break
                print(self.tank.hitShot)
                
            #check for collision with walls
            collideWall = pygame.sprite.spritecollide(self, wallGroup, False)            
            if collideWall:
                self.bounce(collideWall[0])     
            else:
                self.move(self.missileRate)
            
        def move(self, moveValue):
            #move missile
            self.deltaX = 0
            self.deltaY = 0
            if self.face == "U":
                self.deltaY = -moveValue
            elif self.face == "D":
                self.deltaY = moveValue
            elif self.face == "R":
                self.deltaX = moveValue
            elif self.face == "L":
                self.deltaX = -moveValue
            self.rect.x += self.deltaX
            self.rect.y += self.deltaY
            self.image = images["missile"+self.face] 
            
    class powerUp(pygame.sprite.Sprite):
        #create powerups
        def __init__(self, x, y, type):
            pygame.sprite.Sprite.__init__(self)
            self.type = type
            self.claim = False
            self.displayTime = 20*fpsRate
            self.x = x
            self.y = getYCord(y)
            #power up image
            self.imageName = "pu"+self.type[0].capitalize()+self.type[1:]
            self.image = images[self.imageName]           
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x,self.y)
        
        def update(self):
            #check for collision with tank
            collideTankList = pygame.sprite.spritecollide(self, tankGroup, False)
            self.displayTime -= 1
            
            #check if display time timed out
            if self.displayTime <= 0:
                self.kill()
            else:
                if collideTankList:
                    #collided with tank
                    sounds["powerUp"].play()
                    self.kill()
                    for collideTank in collideTankList:
                        #give tank power up
                        collideTank.powerUpStatus[self.type] = True
                        collideTank.powerUpCount += 1
                    

    class Wall(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = images["wall"]
            self.destroyable = True
            self.destroyLimit = 3
            self.destroyCount = self.destroyLimit
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = getYCord(y)
            
        def hit(self):
            self.destroyCount -= 1
            if self.destroyCount < 0:
                self.kill()
            else:   
                self.image = images["wallCracked"+str(self.destroyLimit-self.destroyCount)]
            
    class boundWall(pygame.sprite.Sprite):
        def __init__(self, x, y, side):
            pygame.sprite.Sprite.__init__(self)
            self.destroyable = False
            self.image = images["bWall"+side]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = getYCord(y)
            
    class playerInfo(pygame.sprite.Sprite):
        #player info bar
        def __init__(self, tank, playerNum, totalPlayer, height, yPos):
            self.spacing = 10
            self.barWidth = size[0]-50
            self.playerNum = playerNum
            self.yPos = yPos
            self.tank = tank
            self.playerImageWidth = images["tank"+str(self.playerNum)].get_width()
            pygame.sprite.Sprite.__init__(self)
            #Set Player Info Fill Colour & Size
            self.leftover = self.barWidth - (self.barWidth//totalPlayer)*totalPlayer
            
            if playerNum < totalPlayer:
                self.image = pygame.Surface((self.barWidth//totalPlayer, height))
            if playerNum ==  totalPlayer:
                #last player --> add leftover space
                self.image = pygame.Surface((self.barWidth//totalPlayer+self.leftover, height))
                
            self.rect = self.image.get_rect()

            if self.playerNum == 1:
                self.image.fill((74,160,216))
                self.rect.topleft = (0, yPos)
            if self.playerNum == 2:
                self.image.fill((61,188,22))
                if totalPlayer == 2:
                    self.rect.topright = ((self.barWidth, yPos))
                if totalPlayer >= 3:
                    self.rect.topleft = ((self.barWidth//totalPlayer, yPos))
            if self.playerNum == 3:
                self.image.fill((198,100,176))
                if totalPlayer == 3:
                    self.rect.topright = ((self.barWidth, yPos))
                if totalPlayer >= 4:
                    self.rect.topleft = ((self.barWidth//totalPlayer*2, yPos))
            if self.playerNum == 4:
                self.image.fill((200,117,44))
                self.rect.topright = ((self.barWidth, yPos))
            
            #add ammo bar
            self.infoAmmoBar = ammoBar(self.tank, playerNum, self)
            #add life bar
            self.infoLifeBar = lifeBar(self.tank, playerNum, self)
            #get coordinate for player image
            self.imageCord = (self.infoAmmoBar.rect.right + (self.infoLifeBar.rect.left - self.infoAmmoBar.rect.right)//2, self.rect.centery)
            #add image
            self.infoImage = playerImage(self.tank, self.imageCord, self)
            #add sprites to group
            playerInfoImageGroup.add(self.infoImage)            
            playerInfoImageGroup.add(self.infoAmmoBar)
            playerInfoImageGroup.add(self.infoLifeBar)

                
    class playerImage(pygame.sprite.Sprite):
        #player info bar image
        def __init__(self, tank, cord, playerInfoObj):
            pygame.sprite.Sprite.__init__(self)
            self.tank = tank
            self.tankNum = self.tank.tankNum
            self.playerInfoObj = playerInfoObj
            self.image = images["tank"+str(self.tankNum)]
            self.rect = self.image.get_rect()
            #self.rect.center = (playerInfoObj.rect.left+(1*(playerInfoObj.rect.width//3)), playerInfoObj.rect.centery)
            self.rect.center = cord
        def update(self):
            if self.tank.dead:
                self.rect.center = self.playerInfoObj.rect.center
        
    
    class ammoBar(pygame.sprite.Sprite):
        def __init__(self, tank, playerNum, playerInfoObj):
            #width of each ammo image
            self.width = 25
            pygame.sprite.Sprite.__init__(self)
            self.tank = tank
            self.playerInfoObj = playerInfoObj
            self.ammoLeft = self.tank.missileLeft
            #image
            self.image = images["ammo"].subsurface((0, 0, (self.width*self.ammoLeft), (images["ammo"].get_height())))
            self.rect = self.image.get_rect()
            self.rect.midleft = (self.playerInfoObj.rect.midleft[0]+self.playerInfoObj.spacing, self.playerInfoObj.rect.midleft[1])
        
        def update(self):
            if self.tank.lives > 0:
                #if lives > 0
                self.ammoLeft = self.tank.missileLeft
                if self.ammoLeft >= 0:
                    #display ammo left
                    self.image = images["ammo"].subsurface((0, 0, (self.width*self.ammoLeft), (images["ammo"].get_height())))
                else:
                    #power up
                    self.image = images["puAmmoImage"]
                self.rect = self.image.get_rect()
                self.rect.midleft = (self.playerInfoObj.rect.midleft[0]+self.playerInfoObj.spacing, self.playerInfoObj.rect.midleft[1])
            else:
                if self.tank.ghost:
                    #ghost mode
                    self.image = images["ghost"]
                else:
                    #dead mode
                    self.image = images["skull"]
                    
                #image rect
                self.rect = self.rect = self.image.get_rect()
                #self.rect.midleft = (self.playerInfoObj.rect.centerx+self.playerInfoObj.playerImageWidth//2+
                #self.playerInfoObj.spacing, self.playerInfoObj.rect.centery)
                self.rect.midright = (self.playerInfoObj.infoImage.rect.left-5, self.playerInfoObj.rect.centery)
           
    
    class lifeBar(pygame.sprite.Sprite):
        def __init__(self, tank, playerNum, playerInfoObj):
            #width of each heart image
            self.width = 30
            self.playerInfoObj = playerInfoObj
            pygame.sprite.Sprite.__init__(self)
            self.tank = tank
            self.lifeLeft = self.tank.lives
            #image
            self.image = images["heart"].subsurface((0, 0, (self.width*self.lifeLeft), (images["heart"].get_height())))
            self.rect = self.image.get_rect()
            self.rect.midright = (self.playerInfoObj.rect.midright[0]-self.playerInfoObj.spacing, self.playerInfoObj.rect.midright[1])
        
        def update(self):
            self.lifeLeft = self.tank.lives
            self.image = images["heart"].subsurface((0, 0, (self.width*self.lifeLeft), (images["heart"].get_height())))
            
            if self.lifeLeft <= 0:
                if self.tank.ghost:
                #ghost mode
                    self.image = images["ghost"]
                else:
                #dead mode
                    self.image = images["skull"]
                #image rect
                self.rect = self.rect = self.image.get_rect()
                #self.rect.midright = (self.playerInfo.rect.center[0]-self.playerInfo.playerImageWidth//2-
                #self.playerInfo.spacing, self.playerInfo.rect.center[1])
                self.rect.midleft = (self.playerInfoObj.infoImage.rect.right+5, self.playerInfoObj.rect.centery)
                
    class settingsBar(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            #self.image = pygame.Surface((50,50))
            #self.image.fill(colours["dark grey"])
            
            #text
            self.myfont = pygame.font.Font(fonts["bops1"], 150)
            self.pauseText = self.myfont.render("PAUSED", True, colours["light grey"])
            self.pauseTextRect = self.pauseText.get_rect()
            self.pauseTextRect.center = screen.get_rect().center
            self.image = images["settingsBG"].subsurface(0,0,50,50)
            self.rect = self.image.get_rect()
            self.rect.topright = (size[0],0)
            settingsIconGroup.add(pauseButton(self))
            
        def pause(self):
            #pause function
            print(size)
            #background (darker screen)
            self.pauseBG = self.image
            self.pauseBGrect = self.rect
            #pause text
            self.image = pygame.transform.scale(images["GObg"], size)
            self.image.blit(self.pauseBG, self.pauseBGrect)
            self.image.blit(self.pauseText, self.pauseTextRect)
            self.rect = self.image.get_rect()
            self.rect.center = screen.get_rect().center
            #clear tank movement list
            for tankNum in tankDict:
                tankDict[tankNum].moveList = []
                tankMove[tankNum]["x"] = 0
                tankMove[tankNum]["y"] = 0
            
        def unpause(self):
            #unpause function
            self.image = images["settingsBG"].subsurface(0,0,50,50)
            self.rect = self.image.get_rect()
            self.rect.topright = (size[0],0)
            
        
    class pauseButton(pygame.sprite.Sprite):
        #pause button
        def __init__(self, setBar):
            pygame.sprite.Sprite.__init__(self)
            self.setBar = setBar
            #image
            self.image = images["pauseFade"]
            self.rect = self.image.get_rect()
            self.rect.topright = (size[0]-5, 5)
            self.paused = False
            
        def update(self, mousePos, mouseDownPos):
            if self.rect.collidepoint(mousePos):
                #if collide with mouse
                self.image = images["pauseFull"]
            else:
                #if normal
                self.image = images["pauseFade"]
            if mouseDownPos != None and self.rect.collidepoint(mouseDownPos):
                #if clicked
                self.paused = True
                #pause game
                self.setBar.pause()
                #icon image --> play image
                self.image = images["playFull"]  
                
                while self.paused:
                    #loop to check for unpause click
                    for ev in pygame.event.get(): 
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            if ev.button == 1:
                                if self.rect.collidepoint(ev.pos):
                                    #if clicked: unpause
                                    self.paused = False
                                    self.setBar.unpause()           
                    screen.fill((0,0,0))
                    screen.blit(gameScreen, (0,0))                    
                    settingsGroup.draw(screen)
                    settingsIconGroup.draw(screen)
                    pygame.display.update()
                             
    #Set up status bar
    global statusBarHeight
    statusBarHeight = 50  
    
    #Create Groups for Sprites
    allSprites = pygame.sprite.Group()
    playerInfoGroup = pygame.sprite.Group()
    playerInfoImageGroup = pygame.sprite.Group()
    missileGroup = pygame.sprite.Group()
    explosionGroup = pygame.sprite.Group()
    wallGroup = pygame.sprite.Group()
    nonDestroyWallGroup = pygame.sprite.Group()
    tankGroup = pygame.sprite.Group()
    powerUpGroup = pygame.sprite.Group()
    settingsGroup = pygame.sprite.Group()
    settingsIconGroup = pygame.sprite.Group()
    
    #add sprites to allSprites group
    allSprites.add(playerInfoGroup)
    allSprites.add(playerInfoGroup)
    allSprites.add(missileGroup)
    allSprites.add(explosionGroup)
    allSprites.add(wallGroup)
    allSprites.add(tankGroup)
    allSprites.add(powerUpGroup)
    allSprites.add(settingsGroup)
    allSprites.add(settingsIconGroup)
    
    tankPosList = []
    
    #Power up settings
    powerUpOn = True
    powerUpDict = {"ammo":2, "speed":1, "doubleLife":2}
    powerUpList = []
    for powerUpChance in powerUpDict:
        powerUpList.extend([powerUpChance]*powerUpDict[powerUpChance])
        
    #TEMP TESTING
    powerUpFreq = (30//numPlayer,40//numPlayer)
    #powerUpFreq = (1,2)
    #TEMP TESTING
    nextPowerUp = random.randint(powerUpFreq[0]*fpsRate, powerUpFreq[1]*fpsRate)
    powerUpLocList = []
    
    #Settings/Pause Button
    settingsGroup.add(settingsBar())
    
    #Get coordinate for playing field
    def getYCord(y):
        global statusBarHeight
        y += statusBarHeight
        return y
    
    #Set Up Scene
    #boundary walls
    for bWallCol in range((size[0]//25)+1):
        wallGroup.add(boundWall(bWallCol*25, 0, "U"))
        wallGroup.add(boundWall(bWallCol*25, size[1]-12-statusBarHeight, "D"))
    for bWallRow in range((size[1]//25)+1):
        wallGroup.add(boundWall(0, bWallRow*25, "L"))
        wallGroup.add(boundWall(size[0]-12, bWallRow*25,  "R"))
    
    
    #Tanks and walls
    for rowNum, row in enumerate(maps[mapNum][:size[1]//25-4]):
        for colNum, col in enumerate(row[:size[0]//25-4]):
            if col == "W":
                wallGroup.add(Wall((colNum+1)*25, (rowNum+1)*25))
            if col == "T":
                tankPosList.append(((colNum+1)*25, (rowNum+1)*25))     
            if col == "." or  col == "O":
                powerUpLocList.append(((colNum+1)*25, (rowNum+1)*25))
   
    #Set up tanks & set up player info bar
    tankDict = {}
    tankMove = {}
    misLimit = 5
    faceList = ["R","D","L","U"]   
    #Get max ammo and health
    playerInfoWidth = (size[0]-50)//numPlayer-80
    maxAmmo = min((playerInfoWidth//3)//25, 6)
    maxLife = min((2*(playerInfoWidth//3))//30, 10)
    settings = (maxAmmo, maxLife)
    #TEMP TESTING
    #settings = (0,0)
    #settings = {1:[1,1], 2:[6,8], 3:[4,6], 4:[3,5]}
    for tankNum in range(1, numPlayer+1):
        tankPos = random.choice(tankPosList)
        tankPosList.remove(tankPos)
        tankDict[tankNum] = Tank(tankPos[0], tankPos[1], tankNum, numPlayer, powerUpList, settings)
        tankMove[tankNum] = {"x":0, "y":0}
        tankGroup.add(tankDict[tankNum])
        playerInfoGroup.add(playerInfo(tankDict[tankNum], tankNum, numPlayer, statusBarHeight, 0))
        
    tankControls = {
    1:{K_w:"U", K_a:"L", K_d:"R", K_s:"D", K_v:"X"}, 
    2:{K_KP5:"U", K_KP1:"L", K_KP3:"R", K_KP2:"D", K_KP_ENTER:"X"},
    3:{K_i:"U", K_j:"L", K_l:"R", K_k:"D", K_SLASH :"X"},
    4:{K_UP:"U", K_LEFT:"L", K_RIGHT:"R", K_DOWN:"D", K_RETURN:"X"}}
    moveDict = {"U":(0,-1), "D":(0,1), "L":(-1,0), "R":(1,0)}

    #Create explosions
    explosionCount = 0
    
    #Build walls
    bWallWidth = images["bWall"].get_width()
    blockWidth = images["wall"].get_width()
    
    #Time to end game after last tank standing
    gameEndCountdown = 1*fpsRate
    
    #Track tank standings
    global playerRank
    playerRank = []
    global gameTimeCounter
    gameTimeCounter = 0
    
    #Countdown run flag
    preGameStartRun = True
    
    #Actual game loop
    try:
        while keepGoing:
            #Refresh Screen
            screen.blit(gameScreen, (0,0))
            pygame.display.update()
        
            #Set up fps rate
            clock.tick(fpsRate)
            gameTimeCounter += 1
            
            #Tank Status List
            global tankStat
            tankStat = []
            
            #Set default mouse down position
            mouseDownPos = None
            
            #Check for events
            for ev in pygame.event.get():
                #Exit Button
                if ev.type == pygame.QUIT:
                    keepGoing = False
                #Button Down
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == K_ESCAPE:
                        keepGoing = False
                        break
                    for tankNum in tankDict:
                        for key in tankControls[tankNum]:
                            if ev.key == key:
                                if tankControls[tankNum][key] == "X":
                                    tankDict[tankNum].launch()
                                else:
                                    tankDict[tankNum].moveList.append(tankControls[tankNum][key])
                                    tankDict[tankNum].face = tankDict[tankNum].moveList[-1]
                                    tankMove[tankNum]["x"] = moveDict[tankDict[tankNum].moveList[-1]][0]
                                    tankMove[tankNum]["y"] = moveDict[tankDict[tankNum].moveList[-1]][1]
                elif ev.type == pygame.KEYUP:
                    for tankNum in tankDict:
                        if ev.key in tankControls[tankNum]:
                            if tankControls[tankNum][ev.key] != "X":
                                if tankControls[tankNum][ev.key] in tankDict[tankNum].moveList:
                                    tankDict[tankNum].moveList.remove(tankControls[tankNum][ev.key])
                                if len(tankDict[tankNum].moveList) > 0:
                                    tankDict[tankNum].face = tankDict[tankNum].moveList[-1]
                                    tankMove[tankNum]["x"] = moveDict[tankDict[tankNum].moveList[-1]][0]
                                    tankMove[tankNum]["y"] = moveDict[tankDict[tankNum].moveList[-1]][1]
                                else:
                                    tankMove[tankNum]["x"] = 0
                                    tankMove[tankNum]["y"] = 0
                elif ev.type == pygame.MOUSEBUTTONDOWN:
                    if ev.button == 1:
                        mouseDownPos = ev.pos
            
            #Power up function
            if powerUpOn:
                if gameTimeCounter >= nextPowerUp:
                    openCord = False
                    while openCord == False:
                        newCord = random.choice(powerUpLocList)
                        openCord = True
                        for tank in tankDict:
                            if tankDict[tank].rect.collidepoint(newCord):
                                openCord = False
                                break
                    newType = random.choice(powerUpList)
                    nextPowerUp = gameTimeCounter + random.randint(powerUpFreq[0]*fpsRate, powerUpFreq[1]*fpsRate)
                    powerUpGroup.add(powerUp(newCord[0], newCord[1], newType))
                
            #Get Mouse Position
            mousePos = pygame.mouse.get_pos()            
            
            #Display Background    
            gameScreen.fill((100,100,100))
            gameScreen.blit(images["bgImage"], (0,0))
            
            #Display Status Bar
            playerInfoGroup.draw(gameScreen)
            playerInfoImageGroup.update()
            playerInfoImageGroup.draw(gameScreen)
            
            #Display Wall
            wallGroup.draw(gameScreen)
            
            #Display Power Up
            powerUpGroup.update()
            powerUpGroup.draw(gameScreen)
            
            #Update & Display Tank
            for tankNum in tankDict:
                tankDict[tankNum].move(tankMove[tankNum]["x"], tankMove[tankNum]["y"])
            
            tankGroup.update()
            tankGroup.draw(gameScreen)
           
            #Update & Display Missile
            missileGroup.update()
            missileGroup.draw(gameScreen)
            
            #Update & Draw Collosion
            explosionGroup.update()
            explosionGroup.draw(gameScreen)   
            
            #Display Settings Bar
            settingsGroup.draw(gameScreen)
            settingsIconGroup.update(mousePos, mouseDownPos)
            settingsIconGroup.draw(gameScreen)
            
            #Check if countdown has run yet
            if preGameStartRun:
                preGameStart(gameScreen)
                preGameStartRun = False
                #Start playing background music
                pygame.mixer.music.load(resourcePath + bgMusicName)
                pygame.mixer.music.play(-1)

            #Test Stuff
            
            #Check if any tanks are alive
            if tankStat.count(False) <= 1:
                gameEndCountdown -= 1
                if gameEndCountdown <= 1:
                    pygame.mixer.music.stop()
                    print("GAME OVER")
                    for tank in tankDict:
                        tankDict[tank].addToRankings()
                    gameOver(playerRank, gameScreen, returnMainMenu)
                    input()
                    
            
    finally:
        pygame.quit()
        

global screen
global fonts
global images
global maps
global sounds
global size
global colours

#Initalize Stuff
pygame.init()
pygame.mixer.init()
pygame.display.init()

#Set up framerate
fpsRate = 60
clock = pygame.time.Clock()
    
#Set Game Settings
mapNum = 2
numPlayer = 4
returnMainMenu = False

#bgMusic: 1-8
bgMusicList = {1:"cinema", 2:"battle", 3:"desert", 4:"beach", 5:"underwater", 6:"starship", 7:"athletic", 8:"awesome"}
bgMusicNum = 5
bgMusicName = bgMusicList[bgMusicNum]+".mp3"

#Get Path to Working Directory and Resources Directory Path
curPath = os.getcwd()
resourcePath = curPath + "/resources/"

#Set Up Game
setupGame(resourcePath)

#Set up Score
score = {}
for player in range(1, numPlayer+1):
    score[player] = 0

#Start Acutal Game
startGame(resourcePath, mapNum, numPlayer, bgMusicName, score, returnMainMenu)
#pygame.quit()
