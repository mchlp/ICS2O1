
#Final Project - Game
#"NAME OF GAME"
#Michael Pu & Samuel Liu
#ICS2O1
#2016/12/06

import pygame
from pygame.locals import *  
import os, time

#SET UP GAME
def runGame(size):

    #FOR TDSB COMPUTERS
    def setupDrivers():
        import platform
        if platform.system() == "Windows":
            os.environ['SDL_VIDEODRIVER'] = 'windib'

    #Set up screen
    def makeScreen(size):
        global screen
        screen = pygame.display.set_mode(size) 
        pygame.display.set_caption("The Game.")
        screen.fill((100,100,100))
        return screen

    #Open Images
    def loadImages(imageList):
        global images
        images = {}
        
        directions = ["U", "D", "L", "R"]
        oImageList = {"bgImage":"dirt.jpg", "explosion":"explosion.png"}
        dImageList = {"tank1":"tank1.png", "missile":"missile.png"}
        
        for loadOImage in oImageList:
            images[loadOImage] = pygame.image.load(oImageList[loadOImage]).convert_alpha()
        for loadDImage in dImageList:
            for direct in directions:
                dot = dImageList[loadDImage].find(".")
                fileName = dImageList[loadDImage][:dot] + direct + dImageList[loadDImage][dot:]
                images[loadDImage+direct] = pygame.image.load(fileName).convert_alpha()
        for explosionImage in range(1, 19+1):
            images["explosion"+str(explosionImage)] = pygame.image.load("explosion (" + str(explosionImage) + ").gif")
            
        #images["bgImage"] = pygame.image.load("dirt.jpg").convert()
        #images["tankImages"] = pygame.image.load("tanks.png").convert()
        #images["tank1"] = pygame.image.load("tank1.png").convert_alpha()
        #images["missile"] = pygame.image.load("missile.png").convert_alpha()

    pygame.init()
    setupDrivers()
    makeScreen(size)
    loadImages([1,2])
    startGame(size)

def startGame(size):
    global screen
    global images
    
    #Set up framerate
    clock = pygame.time.Clock()

    #Set up keepGoing flag
    keepGoing = True

    #Set up tank position
    tank1Pos = [100, 100]
    direction = "stop"
    face = "R"
    faceList = ["R","D","L","U"]

    #Set up tank physics
    moveRate = 3

    #Set up missiles physics
    missileRate = 8
    objectList = [[],[]]
    missileLaunch = {"R":(72, 24), "U":(24,0), "L":(0,24), "D":(24,72)}

    #Update missile function
    def updateMissile(objectList):
        global screen
        global images
        
        misTol = 5
        tankTol = 50
        numExplosionImages = 19
        missileList = objectList[0]
        explosionList = objectList[1]
        newMissileList = list(missileList)
        
        for mis in missileList:
            #print("REMOVE ORIGINAL", mis)
            tempMissileList = list(missileList)
            tempMissileList.remove(mis)
            remove = False
            crash = False
            
            #CHECK FOR MISSILE COLLISION
            for testMis in tempMissileList:
                if (abs(testMis[0]-mis[0]) < misTol) and (abs(testMis[1]-mis[1]) < misTol):
                    crash = True
                    #print("FOUND", testMis, mis)
                    missileList.remove(mis)
                    missileList.remove(testMis)
                    #print("REMOVE OTHER", testMis)
                    
        #CHECK FOR TANK COLLISION
        tempMissileList = list(missileList)
        for testMis in tempMissileList:
            print(testMis, tank1Pos)
            if (abs(testMis[0]-tank1Pos[0]) < tankTol) and (abs(testMis[1]-tank1Pos[1]) < tankTol):
                crash = True
                #print("FOUND TANK", testMis, mis)
                missileList.remove(testMis)
                print("REMOVE OTHER", testMis)
                    
            #IF MISSILE COLLIDES        
            if crash:
                explosionList.append(((mis[0]-100, mis[1]-100), 1))
                remove = True
            
            #IF MISSILE DOES NOT COLLIDE
            if not remove:            
                if mis[2] == "U":
                    mis[1] -= missileRate
                    if mis[1] < 0:
                        mis[2] = "D"
                        #missileList.remove(mis)
                        #remove = True
                elif mis[2] == "D":
                    mis[1] += missileRate
                    if mis[1] > size[1]:
                        mis[2] = "U"
                        #missileList.remove(mis)
                        #remove = True
                elif mis[2] == "L":
                    mis[0] -= missileRate
                    if mis[0] < 0:
                        mis[2] = "R"
                        #missileList.remove(mis)
                        #remove = True
                elif mis[2] == "R":
                    mis[0] += missileRate
                    if mis[0] > size[0]:
                        mis[2] = "L"
                        #missileList.remove(mis)
                        #remove = True

                screen.blit(images["missile"+mis[2]], (mis[0],mis[1]))
        
        tempExplosionList = list(explosionList)   
        
        for num, explsn in enumerate(explosionList): 
            explosionFPS = 2
            if explsn[1] > (numExplosionImages-1)*explosionFPS:
                tempExplosionList.remove(explsn)       
            else:
                screen.blit(images["explosion"+str((explsn[1]//explosionFPS)+1)], explsn[0])
                tempExplosionList[tempExplosionList.index(explsn)] = (explsn[0], explsn[1]+1)
        
        objectList = [missileList, tempExplosionList]
        #print(objectList)

        return objectList       

    #Actual game loop
    try:
        while keepGoing:
            #Set up fps rate
            clock.tick(60)
            
            #Check for events
            for ev in pygame.event.get():
                #If the close button is pressed
                if ev.type == pygame.QUIT:
                    keepGoing = False
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == K_w:   
                        direction="U"
                        face="U"
                    elif ev.key == K_d:  
                        direction="R"
                        face="R"
                    elif ev.key == K_a:   
                        direction="L"
                        face="L"
                    elif ev.key == K_s:   
                        direction="D"
                        face="D"
                    elif ev.key == K_COMMA:
                        directIndex = faceList.index(face)-1
                        if directIndex < 0:
                            directIndex = -1
                        direction = faceList[directIndex]
                    elif ev.key == K_PERIOD:
                        directIndex = faceList.index(face)+1
                        if directIndex >= len(faceList):
                            directIndex = 0
                        direction = faceList[directIndex]
                    elif ev.key == K_SPACE:
                        objectList[0].append([tank1Pos[0]+missileLaunch[face][0], tank1Pos[1]+missileLaunch[face][1], face])
                elif ev.type == pygame.KEYUP:
                    direction="stop"
                    
            #Move tank
            if direction== "U" and tank1Pos[1]>0:
                tank1Pos[1] -= moveRate
            elif direction== "R" and tank1Pos[0]+70<size[0]:
                tank1Pos[0] += moveRate
            elif direction== "L" and tank1Pos[0]>0:
                tank1Pos[0] -= moveRate
            elif direction== "D" and tank1Pos[1]+70<size[1]:
                tank1Pos[1] += moveRate

            #Display Stuff    
            screen.fill((100,100,100))
            screen.blit(images["bgImage"], (0,0))
            objectList = updateMissile(objectList)
            #screen.blit(images["missile"], (100,100))
            screen.blit(images["tank1"+face], tuple(tank1Pos))
                    
            pygame.display.flip()
    finally:
        pygame.quit()

global screen
global images
size = (1000,800)  
runGame(size)
