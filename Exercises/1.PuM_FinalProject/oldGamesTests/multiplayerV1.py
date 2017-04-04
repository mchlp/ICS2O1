
#Final Project - Game
#"NAME OF GAME"
#Michael Pu & Samuel Liu
#ICS2O1
#2016/12/06
#SCREEN RESOLUTION: H 768 W 1366

import pygame
from pygame.locals import *  
import os
import time
import random

#SET UP GAME
def setupGame(resourcePath):

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
                    if yRect.collidepoint(pos):
                        return True
                    elif nRect.collidepoint(pos):
                        return False
                elif ev.type == KEYDOWN:
                    if ev.key == K_ESCAPE:
                        return False

    #Set up screen
    def setupDisplay():
        global screen
        global images
        global size
        import platform
        
        #Check Resolution for Full Screen
        checkFullScreenRes = True
        
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
            #default size
        else:
            gameW = gameW - gameW%25
            gameH = gameH - gameH%25 + 75
            if gameH > 1600 or gameW > 1600:
                size = (min(1600, gameW), min(1600, gameH))
                screen = pygame.display.set_mode(size) 
            else:
                if checkFullScreenRes:
                    ynGoodRes = testRes(((min(displayW, displayH))//5)*2, displayH//35, displayW, displayH)
                    if ynGoodRes:
                        size = (displayW, displayH)
                        screen = pygame.display.set_mode(size, pygame.FULLSCREEN) 
                    else:
                        size = (gameW, gameH)
                        screen = pygame.display.set_mode(size)
                else:
                    size = (gameW, gameH)
                    screen = pygame.display.set_mode(size)
            #size = (gameW, gameH)
            print(size)
            
        if platform.system() == "Windows":
            os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (displayW//2-gameW//2,1)
            #os.environ['SDL_VIDEO_CENTERED'] = '1'
            os.environ['SDL_VIDEODRIVER'] = 'windib'
            
        else:
            #screen = pygame.display.set_mode(size) 
            screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
        pygame.display.set_caption("The Game.")
        #TEMP
        #pygame.display.set_icon(pygame.image.load(resourcePath+"icon.png"))
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
        ,"time":"time.png" ,"help":"help.png", "helpLong":"helpLong.png", "rankingBlank":"rankingBlank.png"}
        
        #direction image list (4 images)
        dImageList = {"missile":"missile.png", "bWall":"bWall.png"}
        
        #add power ups to image list
        for powerUp in ["Ammo", "Speed"]:
            oImageList["pu"+powerUp] = "pu"+powerUp+".png"
        oImageList["puAmmoImage"] = "puAmmoImage.png"
        
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
        mapFile = open(resourcePath + "mapDataBase.txt")
        addData = False
        for line in mapFile:
            line = line.strip()
            if line == "***":
                if addData:
                    addData = False
                    maps[mapCount] = curMap
                else:
                    addData = True
                    curMap = []
                continue
            elif addData:
                if line in "1234567890":
                    mapCount = int(line)
                else:
                    curMap.append(line) 

    def loadSounds():
        global sounds
        sounds = {}
        soundListWAV = {"smallExplosion":"smallExplosion.wav", "bigExplosion":"bigExplosion.wav", "shoot":"pew.wav", "powerUp":"powerUp.wav"}
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
    loadImages()
    loadMap()
    loadSounds()
    loadFonts()
    loadColours()
    print(sounds)
    

def startGame(resourcePath, mapNum, numPlayer):
    global screen
    global images
    global sounds
    global size
    global fonts
    global colours
    
    #Game Over Function   
    def gameOver(ranking, gameScreen):
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
                    self.font = pygame.font.Font(fonts["roboto"], 15)
                    self.titleText = self.font.render(obj[0], True, colours["black"])
                    self.titleImage = obj[1]
                    self.image = self.titleImage
                    self.rect = self.image.get_rect()
                    self.rect.center = (75*(self.col-1)+30+self.slot.rect.left, self.slot.rect.centery)
                
                #check if mouse collides with image
                def update(self, mousePos):
                    if self.rect.collidepoint(mousePos):
                        self.image = self.titleText
                    else:
                        self.image = self.titleImage
                    self.rect = self.image.get_rect()
                    self.rect.center = (75*(self.col-1)+30+self.slot.rect.left, self.slot.rect.centery)
                    
                    
            #player slots
            class rankingText(pygame.sprite.Sprite):
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
                    self.tankImage = image
                    self.image = self.tankImage
                    self.rect = self.image.get_rect()
                    self.rect.center = (75*(self.col-1)+30+self.slot.rect.left, self.slot.rect.centery)
                    self.font = pygame.font.Font(fonts["roboto"], 20)
                    self.text = self.font.render("Player "+str(self.num), True, colours["light grey"])
              
                #check if mouse collides with image
                def update(self, mousePos):
                    if self.rect.collidepoint(mousePos):
                        self.image = self.text
                    else:
                        self.image = self.tankImage
                    self.rect = self.image.get_rect()
                    self.rect.center = (75*(self.col-1)+30+self.slot.rect.left, self.slot.rect.centery)
                    
            def __init__(self, bgRect, data, place=None):
                global prevSlotYPos
                pygame.sprite.Sprite.__init__(self)
                self.bg = bgRect
                self.spacing = 10
                
                if data["num"] == 0:
                    self.image = images["rankSlotTitle"]
                    self.rect = self.image.get_rect()
                    self.rect.midtop = (self.bg.midtop[0], prevSlotYPos+self.spacing)
                    prevSlotYPos += self.image.get_height()+self.spacing
                    self.data = []
                    self.data.append(("Rank", images["rankingBlank"]))
                    self.data.append(("Tank", images["rankingBlank"]))
                    self.data.append(("Shots Fired", images["shotsFired"]))
                    self.data.append(("Shots Hit", images["shotsHit"]))
                    self.data.append(("Accuracy", images["accuracy"]))
                    self.data.append(("Shots Taken", images["shotsTaken"]))
                    self.data.append(("Net Damage", images["netDamage"]))
                    self.data.append(("Time", images["time"]))
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
                    #net damage
                    self.data.append(str(data["kills"]-data["damage"]))
                    #time survived
                    if type(data["time"]) == float:
                        self.data.append(str(round(data["time"],2)))
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
        
            class helpText(pygame.sprite.Sprite):
                def __init__(self, helpBox, text):
                    self.text = text
                    self.helpBox = helpBox
                    pygame.sprite.Sprite.__init__(self)
                    self.font = pygame.font.Font(fonts["openSans"], 25)
                    self.image = self.font.render(self.text, True, colours["white"])
                    self.rect = self.image.get_rect()
                    self.rect.midleft = (self.helpBox.rect.left+images["help"].get_rect().right+10,
                    self.helpBox.rect.top+images["help"].get_rect().centery)
                       
            def __init__(self, text, bgRect):
                global prevSlotYPos
                pygame.sprite.Sprite.__init__(self)
                self.expanded = False
                self.bgRect = bgRect
                self.image = images["help"]
                self.rect = self.image.get_rect()
                self.rect.topleft = (self.bgRect.left,prevSlotYPos+10)  
                self.text = self.helpText(self, text)
                
            def update(self, mousePos):
                if self.rect.collidepoint(mousePos):
                    self.image = images["helpLong"] 
                    leadrbrdObjGroup.add(self.text)
                else:
                    self.image = images["help"] 
                    leadrbrdObjGroup.remove(self.text)
                self.rect = self.image.get_rect()
                self.rect.topleft = (self.bgRect.left,prevSlotYPos+10)
                
        
        gameOverLB = images["LBbg"]
        gameOverLBRect = gameOverLB.get_rect()
        gameOverLBRect.center = screen.get_rect().center
        
        gameOverBG = pygame.transform.scale(images["GObg"], size)
        gameOverBGRect = gameOverBG.get_rect()
        gameOverBGRect.center = screen.get_rect().center
        
        #rankingFont = pygame.font.Font(fonts["tankFont"],35)
        rankingFont = pygame.font.Font(fonts["bops1"],35)
        rankingSur = rankingFont.render("Rankings", True, colours["light grey"])
        rankingRect = rankingSur.get_rect()
        rankingRect.midtop = (gameOverLBRect.midtop[0], gameOverLBRect.midtop[1]+10)
        rankingTitleBG = images["rankingTitleBG"]
        rankingTitleRect = rankingTitleBG.get_rect()
        rankingTitleRect.center = rankingRect.center
        
        global prevSlotYPos
        prevSlotYPos = rankingRect.bottom
        leadrbrdGroup.add(rankingSlot(gameOverLBRect ,{"num":0}))
        ranking.reverse()
        for place, player in enumerate(ranking):
            leadrbrdGroup.add(rankingSlot(gameOverLBRect, player, place+1))

        rankingsHelpButton = helpButton("Mouse Over Images for Explaination" ,gameOverLBRect)    
        leadrbrdMouseGroup.add(rankingsHelpButton)
        leadrbrdGroup.add(rankingsHelpButton)
            
        showLeaderboard = True
        
        while showLeaderboard:
            #Set up fps rate
            clock.tick(fpsRate)
            
            #fill background
            screen.fill((100,100,100))
            
            for ev in pygame.event.get():
                #Exit Button
                if ev.type == pygame.QUIT:
                    keepGoing = False
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == K_ESCAPE:
                        keepGoing = False
                        break
            
            mousePos = pygame.mouse.get_pos()
            leadrbrdMouseGroup.update(mousePos) 
            
            screen.blit(gameScreen, (0,0))
            screen.blit(gameOverBG, gameOverBGRect)
            screen.blit(gameOverLB, gameOverLBRect)
            screen.blit(rankingTitleBG, rankingTitleRect)
            screen.blit(rankingSur, rankingRect)
            
            leadrbrdGroup.draw(screen)
            leadrbrdObjGroup.draw(screen)
            
            pygame.display.flip()
    
    #Start playing background music
    #TEMP
    pygame.mixer.music.load(resourcePath + "bgMusic.mp3")
    pygame.mixer.music.play(-1)
    
    #Set up framerate
    fpsRate = 60
    clock = pygame.time.Clock()

    #Set up keepGoing flag
    keepGoing = True

    #Setup game screen
    gameScreen = pygame.surface.Surface(size)
    
    class Tank(pygame.sprite.Sprite):      
        def __init__(self, x, y, num, numPlayer, powerUpList):
            self.num = num
            self.tankNum = self.num
            #set up tank settings
            #player:[ammo, life]
            self.settings = {1:[1,1], 2:[6,8], 3:[4,6], 4:[3,5]}
            self.dead = False
            self.face = "R"
            self.totalPlayer = numPlayer
            self.missileRegenTime = 2
            self.missileRegenCount = 0
            self.missileLimit = self.settings[self.totalPlayer][0]
            self.missileLeft = self.missileLimit
            self.moveRate = 3  
            self.defaultMoveRate = self.moveRate
            self.lives = self.settings[self.totalPlayer][1]
            self.imageNum = str(self.tankNum)
            self.powerUpTime = 10
            self.totalShot = 0
            self.hitShot = 0
            self.damage = 0
            self.ghost = False
            self.addedToRankList = False
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
            
            if not self.addedToRankList:
                if self.dead:
                    self.addedToRankList = True
                    playerRank.append({"num":self.num, "shots":self.totalShot, "kills":self.hitShot,
                    "damage":self.damage, "time":(gameTimeCounter/60)})
                else:
                    self.addedToRankList = True
                    playerRank.append({"num":self.num, "shots":self.totalShot, "kills":self.hitShot,
                    "damage":self.damage, "time":"-"})
            
                
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
                if self.powerUpStatus[powerUp] != False:
                    if powerUp == "ammo":
                        if self.powerUpStatus[powerUp] == True:
                            self.powerUpStatus[powerUp] = self.powerUpTime*fpsRate
                            self.missileLeft = -1  
                        elif self.powerUpStatus[powerUp] <= 0:
                            self.missileLeft = self.missileLimit
                            self.powerUpStatus[powerUp] = False
                        else:
                            self.powerUpStatus[powerUp] -= 1  
                    if powerUp == "speed":
                        if self.powerUpStatus[powerUp] == True:
                            self.powerUpStatus[powerUp] = self.powerUpTime*fpsRate
                            self.moveRate = self.defaultMoveRate*2
                        elif self.powerUpStatus[powerUp] <= 0:
                            self.moveRate = self.defaultMoveRate
                            self.powerUpStatus[powerUp] = False
                        else:
                            self.powerUpStatus[powerUp] -= 1
                
           
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
            if pygame.sprite.spritecollide(self, wallGroup, False):
                self.bounce()     
            else:
                self.move(self.missileRate)
            
        def bounce(self):
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
                    
            if pygame.sprite.spritecollide(self, wallGroup, False):
                self.bounce()     
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
        def __init__(self, x, y, type):
            pygame.sprite.Sprite.__init__(self)
            self.type = type
            self.claim = False
            self.x = x
            self.y = getYCord(y)
            self.image = images["pu"+self.type.capitalize()]            
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x,self.y)
        
        def update(self):
            collideTankList = pygame.sprite.spritecollide(self, tankGroup, False)
            if collideTankList:
                sounds["powerUp"].play()
                self.kill()
                for collideTank in collideTankList:
                    collideTank.powerUpStatus[self.type] = True

    class Wall(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = images["wall"]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = getYCord(y)
            
    class boundWall(pygame.sprite.Sprite):
        def __init__(self, x, y, side):
            pygame.sprite.Sprite.__init__(self)
            nonDestroyWallGroup.add(self)
            self.image = images["bWall"+side]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = getYCord(y)
            
    class playerInfo(pygame.sprite.Sprite):
        def __init__(self, tank, playerNum, totalPlayer, height, yPos):
            self.spacing = 10
            self.playerNum = playerNum
            self.yPos = yPos
            self.tank = tank
            self.playerImageWidth = images["tank"+str(self.playerNum)].get_width()
            pygame.sprite.Sprite.__init__(self)
            #Set Player Info Fill Colour & Size
            self.leftover = size[0] - (size[0]//totalPlayer)*totalPlayer
            
            if playerNum < totalPlayer:
                self.image = pygame.Surface((size[0]//totalPlayer, height))
            if playerNum ==  totalPlayer:
                self.image = pygame.Surface((size[0]//totalPlayer+self.leftover, height))
                
            self.rect = self.image.get_rect()

            if self.playerNum == 1:
                self.image.fill((74,160,216))
                self.rect.topleft = (0, yPos)
            if self.playerNum == 2:
                self.image.fill((61,188,22))
                if totalPlayer == 2:
                    self.rect.topright = ((size[0], yPos))
                if totalPlayer >= 3:
                    self.rect.topleft = ((size[0]//totalPlayer, yPos))
            if self.playerNum == 3:
                self.image.fill((198,100,176))
                if totalPlayer == 3:
                    self.rect.topright = ((size[0], yPos))
                if totalPlayer >= 4:
                    self.rect.topleft = ((size[0]//totalPlayer*2, yPos))
            if self.playerNum == 4:
                self.image.fill((200,117,44))
                self.rect.topright = ((size[0], yPos))
                
            playerInfoImageGroup.add(ammoBar(self.tank, playerNum, self))
            playerInfoImageGroup.add(lifeBar(self.tank, playerNum, self))
            playerInfoImageGroup.add(playerImage(self.tank, self))
                
    class playerImage(pygame.sprite.Sprite):
        def __init__(self, tank, playerInfoObj):
            pygame.sprite.Sprite.__init__(self)
            self.tank = tank
            self.tankNum = self.tank.tankNum
            self.playerInfo = playerInfoObj
            self.image = images["tank"+str(self.tankNum)]
            self.rect = self.image.get_rect()
            self.rect.center = (playerInfoObj.rect.center)
        
    
    class ammoBar(pygame.sprite.Sprite):
        def __init__(self, tank, playerNum, playerInfoObj):
            self.width = 25
            pygame.sprite.Sprite.__init__(self)
            self.tank = tank
            self.playerInfo = playerInfoObj
            self.ammoLeft = self.tank.missileLeft
            self.image = images["ammo"].subsurface((0, 0, (self.width*self.ammoLeft), (images["ammo"].get_height())))
            self.rect = self.image.get_rect()
            self.rect.midleft = (playerInfoObj.rect.midleft[0]+self.playerInfo.spacing, playerInfoObj.rect.midleft[1])
        
        def update(self):
            if self.tank.lives > 0:
                self.ammoLeft = self.tank.missileLeft
                if self.ammoLeft >= 0:
                    self.image = images["ammo"].subsurface((0, 0, (self.width*self.ammoLeft), (images["ammo"].get_height())))
                else:
                    self.image = images["puAmmoImage"]
            else:
                if self.tank.ghost:
                    self.image = images["ghost"]
                else:
                    self.image = images["skull"]
                self.rect = self.rect = self.image.get_rect()
                self.rect.midleft = (self.playerInfo.rect.center[0]+self.playerInfo.playerImageWidth//2+
                self.playerInfo.spacing, self.playerInfo.rect.center[1])
           
    
    class lifeBar(pygame.sprite.Sprite):
        def __init__(self, tank, playerNum, playerInfoObj):
            self.width = 30
            self.playerInfo = playerInfoObj
            pygame.sprite.Sprite.__init__(self)
            self.tank = tank
            self.lifeLeft = self.tank.lives
            self.image = images["heart"].subsurface((0, 0, (self.width*self.lifeLeft), (images["heart"].get_height())))
            self.rect = self.image.get_rect()
            self.rect.midright = (playerInfoObj.rect.midright[0]-self.playerInfo.spacing, playerInfoObj.rect.midright[1])
        
        def update(self):
            self.lifeLeft = self.tank.lives
            self.image = images["heart"].subsurface((0, 0, (self.width*self.lifeLeft), (images["heart"].get_height())))
            
            if self.lifeLeft <= 0:
                if self.tank.ghost:
                    self.image = images["ghost"]
                else:
                    self.image = images["skull"]
                self.rect = self.rect = self.image.get_rect()
                self.rect.midright = (self.playerInfo.rect.center[0]-self.playerInfo.playerImageWidth//2-
                self.playerInfo.spacing, self.playerInfo.rect.center[1])
                    
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
    
    allSprites.add(playerInfoGroup)
    allSprites.add(playerInfoGroup)
    allSprites.add(missileGroup)
    allSprites.add(explosionGroup)
    allSprites.add(wallGroup)
    allSprites.add(nonDestroyWallGroup)
    allSprites.add(tankGroup)
    allSprites.add(powerUpGroup)
    
    tankPosList = []
    
    #Power up settings
    powerUpOn = True
    powerUpList = ["ammo", "speed"]
    powerUpFreq = (15,30)
    nextPowerUp = random.randint(powerUpFreq[0]*fpsRate, powerUpFreq[1]*fpsRate)
    powerUpLocList = []
    
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
    for rowNum, row in enumerate(maps[mapNum]):
        for colNum, col in enumerate(row):
            if col == "W":
                if rowNum < size[1]//25-2 and colNum < size[0]//25-2:
                    wallGroup.add(Wall((colNum+1)*25, (rowNum+1)*25))
            if col == "T":
                tankPosList.append(((colNum+1)*25, (rowNum+1)*25))     
            if col == ".":
                if rowNum < size[1]//25-2 and rowNum > 0 and colNum < size[0]//25-2 and colNum > 0:
                    powerUpLocList.append(((colNum+1)*25, (rowNum+1)*25))
    
    #Set up tanks & set up player info bar
    tankDict = {}
    tankMove = {}
    misLimit = 5
    faceList = ["R","D","L","U"]   
    for tankNum in range(1, numPlayer+1):
        tankPos = random.choice(tankPosList)
        tankPosList.remove(tankPos)
        tankDict[tankNum] = Tank(tankPos[0], tankPos[1], tankNum, numPlayer, powerUpList)
        tankMove[tankNum] = {"x":0, "y":0}
        tankGroup.add(tankDict[tankNum])
        playerInfoGroup.add(playerInfo(tankDict[tankNum], tankNum, numPlayer, statusBarHeight, 0))
        
    tankControls = {
    1:{K_w:"U", K_a:"L", K_d:"R", K_s:"D", K_SPACE:"X"}, 
    2:{K_UP:"U", K_LEFT:"L", K_RIGHT:"R", K_DOWN:"D", K_RETURN:"X"},
    3:{K_u:"U", K_h:"L", K_k:"R", K_j:"D", K_PERIOD:"X"},
    4:{K_KP5:"U", K_KP1:"L", K_KP3:"R", K_KP2:"D", K_KP_ENTER:"X"}}
    moveDict = {"U":(0,-1), "D":(0,1), "L":(-1,0), "R":(1,0)}

    #Create explosions
    explosionCount = 0
    
    #Build walls
    bWallWidth = images["bWall"].get_width()
    blockWidth = images["wall"].get_width()
    
    #Time to end game after last tank standing
    gameEndCountdown = 0.5*fpsRate
    
    #Track tank standings
    global playerRank
    playerRank = []
    global gameTimeCounter
    gameTimeCounter = 0
    
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
                                    tankDict[tankNum].face = tankControls[tankNum][key]
                                    tankMove[tankNum]["x"] = moveDict[tankControls[tankNum][key]][0]
                                    tankMove[tankNum]["y"] = moveDict[tankControls[tankNum][key]][1]
                elif ev.type == pygame.KEYUP:
                    for tankNum in tankDict:
                        if ev.key in tankControls[tankNum]:
                            if tankControls[tankNum][ev.key] != "X":
                                tankMove[tankNum]["x"] = 0
                                tankMove[tankNum]["y"] = 0
            
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

            #Test Stuff
            
            #Check if any tanks are alive
            if tankStat.count(False) <= 1:
                gameEndCountdown -= 1
                if gameEndCountdown <= 1:
                    print("GAME OVER")
                    for tank in tankDict:
                        tankDict[tank].addToRankings()
                    gameOver(playerRank, gameScreen)
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
    
#Set Game Settings
mapNum = 2
numPlayer = 2

#Get Path to Working Directory and Resources Directory Path
curPath = os.getcwd()
resourcePath = curPath + "/resources/"
#Set Up Game
setupGame(resourcePath)

#Start Acutal Game
startGame(resourcePath, mapNum, numPlayer)

