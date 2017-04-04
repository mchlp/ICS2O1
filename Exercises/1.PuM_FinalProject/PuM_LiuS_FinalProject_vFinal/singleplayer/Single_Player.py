#Single Player
creator_mode = False  #so you don't die if you're testing something

#importing
import pygame
from pygame.locals import *  
import os
import time
import random
pygame.init()
#set up display, game stuff
size = (800,600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

path = (os.path.dirname(os.path.realpath(__file__)))+"/single_player/" #makes it easier to access resources in a seperate folder
schoolcomputer = False #i occassionally got 'Assertion Failed' on the particular computer i was using
                        #because of an audio file

#set logo
pygame.display.set_icon(pygame.image.load(path+"icon.png"))
def loadstuff():
    'loads images'
    global images
    global sounds
    images = {} #creates a dict for me to store images in
    #a bunch of image loading
    images["tank1"] = pygame.image.load(path+"tank1.png").convert_alpha()
    images["missileL"] = pygame.image.load(path+"missile.png").convert_alpha()
    images["ammo"] = pygame.image.load(path+"ammo.png").convert_alpha()
    images["heart"] = pygame.image.load(path+"hearts.png").convert_alpha()
    images["dirt"] = pygame.image.load(path+"dirt.jpg").convert()
    images["enemy1"] = pygame.image.load(path+"tank2L.png").convert_alpha()
    images['enemy2'] = pygame.image.load(path+"tank4L.png").convert_alpha()
    images["missileR"] = pygame.image.load(path+"missileL.png").convert_alpha()
    images["powerup1"] = pygame.image.load(path+"powerup1.jpg").convert()
    images['gray'] = pygame.image.load(path+"gray.png").convert_alpha()
    images['gameover'] = pygame.image.load(path+"gameover.png").convert_alpha()
    images['laser'] = pygame.image.load(path+"laser.png").convert_alpha()
    images['shield'] = pygame.image.load(path+"shield.png").convert_alpha()
    images['namespace'] = pygame.image.load(path+"namespace.png").convert_alpha()
    
    for i in range(1,6): #gets redgradients for when the screen flashes red
        images["redgradient"+str(i)] = pygame.image.load(path+"redgradient"+str(i)+".png").convert_alpha()

    for i in range(1,5): #gets beginning animation images
        images['begin'+str(i)] = pygame.image.load(path+"begin"+str(i)+".png").convert_alpha()
    for i in range(2,6): #gets powerups
        images["powerup"+str(i)] = pygame.image.load(path+"powerup"+str(i)+".png").convert_alpha()
    for explosionImage in range(1, 20): #gets explosion frames
        images["explosion"+str(explosionImage)] = pygame.image.load(path+"explosions\\explosion" + str(explosionImage) + ".gif").convert_alpha()

    sounds = {}
    sounds['explosionsound'] = pygame.mixer.Sound(file=path+"explosionsound.ogg")
    sounds['explosionsound'].set_volume(0.5)
    sounds['repulsor'] = pygame.mixer.Sound(file=path+"repulsor.ogg")
    sounds['wii'] = pygame.mixer.Sound(file=path+"wiimusic.ogg")

loadstuff()

#for red screen flash
redcount = 0
redscreens = []

#set up missiles
missilespeed = 10 #missiles speeds
e_missilespeed = 10
missiles = [] #lists for storing missiles
enemy_missiles = []

#set up tank
#position of tank
x = 10
y = 301
#these are pretty self explanatory
missilecount = 5
missilelimit = 5
missileregen = 80
movespeed = 3
lives = 5
liveslimit = 5
livesregen = 300
#tank movement
tankx = 0
tanky = 0
collide = True

#set up enemies
enemies = []
newtank = 100 #rate at which new tanks spawn(how many seconds)
enemy_missiles = []
enemyspeed = 1
shootrate = 100 #rate at which they shoot

#powerups
powerups = []
power_spawn = 1500

#font
fontsize = 35
myfont = pygame.font.SysFont("impact", 45)
smallfont = pygame.font.SysFont("impact", 40)
supersmallfont = pygame.font.SysFont("impact", 30)
bigfont = pygame.font.SysFont("impact", 70)
finalfont = pygame.font.SysFont("impact", 55)

#set up pause
paused = False
pausemess = bigfont.render("PAUSED", True, (250,250,250))
pauserect = pausemess.get_rect(center=(400,300))
pausemess2 = supersmallfont.render("Press 'P' to continue", True, (250,250,250))
pauserect2 = pausemess2.get_rect(center=(400,355))

#other
score = 0
explosions = []

#functions
def begin():
    'beginning animation'
    startscreen = screen.copy()
    for i in range(1,5):
        screen.blit(startscreen, (0,0)) #maintains background while animation is playing
        pygame.display.flip()
        time.sleep(0.5)
        rect = images['begin'+str(i)].get_rect(center=(400,300))
        screen.blit(images["begin"+str(i)], rect) #displays animation
        pygame.display.flip()
        time.sleep(0.5)
        pygame.event.clear()   #so you can't issue commands in the beginning animation
    if not schoolcomputer: #loads music
        bgmusic = pygame.mixer.music.load(path+"10800 Malibu Point.mp3")
        pygame.mixer.music.play(-1)

def tank(x, y):
    'moves tank'
    screen.blit(images["tank1"], (x,y))
    
def shoot():
    'shoots'
    global missilecount
    global x
    global y
    if missilecount > 0:
        #adds a new missile to the list 'missiles' with an x and y
        newmissile = {'x':x+70, 'y':y+20}
        missiles.append(newmissile)
        missilecount -= 1 #decreases remaining ammo by 1
def updatemissiles():
    'moves missiles'
    for missile in missiles:
        #changes the x of every missile by the missile speed
        missile['x'] += missilespeed
        if missile['x'] >= 800:
            missiles.remove(missile) #removes if it leaves screen
        else:
            screen.blit(images["missileL"], (missile['x'],missile['y']))
    #this handles the enemy missiles
    for missile in enemy_missiles: 
        missile['x'] -= e_missilespeed
        if missile['x'] < 1:
            enemy_missiles.remove(missile)
        else:
            screen.blit(images["missileR"], (missile['x'], missile['y']))
def updatestatus():
    'updates health bar, ammo bar, score, checks if you died'
    global missilecount
    global lives
    global gameloop
    global fontsize
    medfont = pygame.font.SysFont("impact", fontsize)
    for i in range(1, lives+1): #blits a number of hearts/ammo based on how many u have left
        screen.blit(images["heart"], (i*60 - 50, 5))
    for i in range(1, missilecount+1):
        if i > 5:
            screen.blit(images['ammo'], ((i-5)*60 + 440, 65))
        else:
            screen.blit(images["ammo"], (i*60 + 440, 5))
    #prints the score on to the screen
    scoreblit = medfont.render(("Score: "+str(score)), True, (255,255,255))
    scorerect = scoreblit.get_rect(center=(400,25))
    if scorerect.x > 380:
        fontsize -= 1 #makes sure the 'score' will still fit if it gets really high
    screen.blit(scoreblit, scorerect)
    if lives <= 0:
        if creator_mode:  #so i don't die when im testing something
            pass
        else:
            gameloop = False
def enemy(newtype):
    'creates a new enemy tank'
    enemyx = 799
    enemyy = random.randint(50, 552) #random y
    #creates newenemy with an x, y, type, and how long since it's spawned
    newenemy = {'x':enemyx, 'y':enemyy,'type':newtype,'alive':1}
    enemies.append(newenemy) #adds it to the list of enemies
    
def updateenemies():
    'moves enemy tanks'
    global lives
    global enemies
    for enemy in enemies: #cycles through all enemies
        if enemy['type'] == "2": #type 2 tanks are twice as fast
            enemy['x'] -= enemyspeed*2
        else:
            enemy['x'] -= enemyspeed
        if enemy['x'] < 1: #removes enemy if it gets to the end, you lose a life
            enemies.remove(enemy) 
            #makes the screen flash red
            redscreen = {'count':redcount}
            redscreens.append(redscreen)
            lives -= 1
        else: #blits an image of a tank, depending on the type
            if enemy['type'] == '2':
                screen.blit(images["enemy2"], (enemy['x'],enemy['y']))
            else:
                screen.blit(images["enemy1"], (enemy['x'],enemy['y']))
            if enemy['type'] == '3':
                screen.blit(images['shield'], (enemy['x']-12,enemy['y']-26))
        enemy['alive'] += 1 #increases how long the tank has been alive
        if enemy['alive'] == shootrate:
            #makes the tank shoot every 'shootrate' seconds, then resets
            enemy['alive'] = 1
            #adds a missile to the list 'enemy_missiles'
            newmissile = {'x':enemy['x'], 'y':enemy['y']+20}
            enemy_missiles.append(newmissile)

def checkcollide():
    'checks for collision with tanks and missiles'
    global enemies
    global missiles
    global x
    global y
    global lives
    global score
    global explosions
    t_rect = pygame.Rect(x,y,75,48) #rect of the player tank
    for enemy in enemies: #checks if I hit a tank
        e_rect = pygame.Rect(enemy['x'], enemy['y'], 75, 48)
        #checks if the player tank rect collides with any enemies
        if e_rect.colliderect(t_rect):
            if collide == True: #screen flashes red, you lose a life
                redscreen = {'count':redcount}
                redscreens.append(redscreen)
                lives -= 1
            if enemy['type'] == '3': #if the enemy has a shield, it's removed
                enemy['type'] = '1'
            else: #otherwise, creates an explosion and removes the enemy
                expl_rect = pygame.Rect(e_rect.x-37, e_rect.y-24, 75, 48)
                newexplosion = {'num':1,'rect':expl_rect,'counter':1,'music':True}
                explosions.append(newexplosion)
                enemies.remove(enemy)
        for missile in missiles: #checks if enemy tanks get hit
            m_rect = pygame.Rect(missile['x'], missile['y'], 36, 9)
            if e_rect.colliderect(m_rect):
                try: 
                    if enemy['type'] == '3': #removes any shields
                        enemy['type'] = '1'
                    else: #creates explosion, removes enemy
                        expl_rect = pygame.Rect(e_rect.x-37, e_rect.y-24, 75, 48)
                        newexplosion = {'num':1,'rect':expl_rect,'counter':1,'music':True}
                        explosions.append(newexplosion)
                        score += 10
                        enemies.remove(enemy)
                    #removes missile if it hit something
                    missiles.remove(missile)
                except:
                    pass
    for missile in enemy_missiles: #checks if i get hit
        em_rect = pygame.Rect(missile['x'], missile['y'], 36, 9)
        if em_rect.colliderect(t_rect):
            if collide == True:
                #screen flashes, lose a life, create an explosion
                #remove enemy missile
                redscreen = {'count':redcount}
                redscreens.append(redscreen)
                lives -= 1
                expl_rect = pygame.Rect(t_rect.x-37, t_rect.y-24, 75, 48)
                newexplosion = {'num':1,'rect':expl_rect,'counter':1,'music':True}
                explosions.append(newexplosion)
            enemy_missiles.remove(missile)
def pause():
    'pause function'
    global paused
    pygame.mixer.music.pause() #pauses music
    sounds['wii'].play(-1) #plays pause screen music
    while paused:
        #displays pause screen and pause message
        screen.blit(pausescreen, (0,0))
        screen.blit(images['gray'],(0,0))
        screen.blit(pausemess, pauserect)
        screen.blit(pausemess2, pauserect2)
        pygame.display.flip()
        #checks if 'p' is pressed to unpause the game
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif ev.type == pygame.KEYUP:
                if ev.key == K_p:
                    paused = False
                    sounds['wii'].stop()
                    pygame.mixer.music.unpause()
start = 1 #this helps me determine the duration of certain powerups based on gameCount
def powerup():
    #a bunch of global things
    global powerups
    global start
    global x
    global y
    global enemies
    global enemy_missiles
    global missiles
    global lives
    global movespeed
    global collide
    global missilecount
    t_rect = pygame.Rect(x, y, 70, 48) #player tank hitbox
    for power in powerups: #cycles through powerups
        border = pygame.Rect(power['x'], power['y'], 50, 50)#creates a black border
        if power['num'] == 1: #destroy all tanks
            screen.blit(images['powerup'+str(power['num'])], (power['x'],power['y']))
            pygame.draw.rect(screen, (0,0,0), border, 4)
            #checks if you collide with the powerup
            if t_rect.colliderect(power['rect']): 
                for enemy in enemies: #creates an explosion at every enemy
                    e_rect = pygame.Rect(enemy['x'], enemy['y'], 75, 48)
                    expl_rect = pygame.Rect(e_rect.x-37, e_rect.y-24, 75, 48)
                    newexplosion = {'num':1,'rect':expl_rect,'counter':1, 'music':True}
                    explosions.append(newexplosion)
                enemies = [] #removes all enemies
                powerups.remove(power)#removes the powerup

        elif power['num'] == 2: #fire death laser of death
            #this powerup has two states; when it's inactive
            #and when it's a laser.
            #if inactive, blit the powerup and check for collision
            if power['checker'] == 0: 
                screen.blit(images['powerup'+str(power['num'])], (power['x'],power['y']))
                pygame.draw.rect(screen, (0,0,0), border, 4)
                if t_rect.colliderect(power['rect']):
                    #if collision, activate powerup
                    sounds['repulsor'].play()
                    #stores when the powerup started
                    start = gameCount
                    missilecount = missilelimit
                    power['checker'] = 1
            else: #handles laser mode
                screen.blit(images['laser'], (x+75, y-76))
                laser = pygame.Rect(x+75, y-23, 800,97)
                if gameCount > start+310: #start+310 is duration of powerup
                    #returns start to 1 for future powerups, and removes it
                    start = 1
                    powerups.remove(power)
                else: #cycles through all enemies and missiles
                      #removes them if they come into contact with it
                    for enemy in enemies:
                        e_rect = pygame.Rect(enemy['x'], enemy['y'], 75, 48)
                        if laser.colliderect(e_rect):
                            try:
                                #add explosion, remove enemy
                                expl_rect = pygame.Rect(e_rect.x-37, e_rect.y-24, 75, 48)
                                newexplosion = {'num':1,'rect':expl_rect,'counter':1,'music':True}
                                explosions.append(newexplosion)
                                enemies.remove(enemy)
                            except:
                                pass
                    for missile in enemy_missiles:
                        em_rect = pygame.Rect(missile['x'], missile['y'], 36, 9)
                        if laser.colliderect(em_rect):
                            try:
                                #remove missiles that come into contact
                                enemy_missiles.remove(missile)
                            except:
                                pass

        elif power['num'] == 3: #restore health/ammo
            screen.blit(images['powerup'+str(power['num'])], (power['x'],power['y']))
            pygame.draw.rect(screen, (0,0,0), border, 4)
            #if collided, restore lives and ammo to full, then remove the powerup
            if t_rect.colliderect(power['rect']): 
                lives = liveslimit
                missilecount = missilelimit
                powerups.remove(power)
        elif power['num'] == 4: #overdrive
            #this powerup also has two states
            #it's like the laser but you're indestructible and fast
            if power['checker'] == 0:
                #only blits if you haven't collided with it
                screen.blit(images['powerup'+str(power['num'])], (power['x'],power['y']))
                pygame.draw.rect(screen, (0,0,0), border, 4)
                if t_rect.colliderect(power['rect']):
                    start = gameCount
                    #activates 2nd state if you collide with it
                    power['checker'] = 1
            else:
                #adds a shield around you
                screen.blit(images['shield'], (t_rect.x-12,t_rect.y-26))
                movespeed = 12 #move faster
                collide = False #dont take damage when hit
                if gameCount > start+300: #duration of powerup
                    #returns variables to normal if time is up
                    movespeed = 3
                    collide = True
                    powerups.remove(power)
        elif power['num'] == 5: #reverse missiles
            screen.blit(images['powerup'+str(power['num'])], (power['x'],power['y']))
            pygame.draw.rect(screen, (0,0,0), border, 4)
            #if collided, turn every enemy missile into
            #your own missiles
            if t_rect.colliderect(power['rect']):
                for missile in enemy_missiles:
                    missiles.append(missile)
                enemy_missiles = []
                powerups.remove(power)

def updateexplosions():
    'updates explosions'
    global explosions
    for explosion in explosions:
        if explosion['music']:
            #so you only play the explosion sound once
            sounds['explosionsound'].play()
            explosion['music'] = False
        #explosions have two values; counter and num
        #num represents the frame of the explosion
        #counter represents the duration of the explosion
        screen.blit(images[("explosion"+str(explosion['num']))],(explosion['rect']))
        explosion['counter'] += 1 #increases counter every tick
        if explosion['counter']%3 == 0:
            #every 3 ticks, it updates the frame by increasing num by 1
            explosion['num'] += 1
        if explosion['num'] == 20: #removes at the end of animation
            explosions.remove(explosion)

def updatered():
    'makes the screen flash red'
    for red in redscreens:
        if red['count'] > 9: #removes it at the end
            redscreens.remove(red)
        #if count is <= 5, blit the first frame and increase count by 1
        elif red['count'] <= 5:
            screen.blit(images['redgradient1'], (0,0))
            red['count'] += 1
        #otherwise, gradually make the red flash fade
        #by blitting the next frame
        else:
            screen.blit(images['redgradient'+str(red['count']-4)], (0,0))
            if gameCount%5 == 0:
                #increases count by 1 every 5 ticks
                red['count'] += 1

def updateall():
    'updates all'
    powerup()
    updatemissiles()
    updateenemies()
    checkcollide()
    updatestatus()
    updateexplosions()
    updatered()
    pygame.display.flip()

#actual game loop
gameloop = True
gameCount = 0
while gameloop:
    clock.tick(60)
    gameCount += 1 #for handling events and stuff
    screen.blit(images["dirt"], (0,0))
    for ev in pygame.event.get(): #handles events
        if ev.type == pygame.QUIT: #if they close the window
            pygame.quit()
            quit()
        elif ev.type == pygame.KEYDOWN: #handles controls
            #movement
            if ev.key == pygame.K_w:
                tanky = -1
            elif ev.key == pygame.K_d:
                tankx = 1
            elif ev.key == pygame.K_s:
                tanky = 1
            elif ev.key == pygame.K_a:
                tankx = -1
            #shooting
            elif ev.key == pygame.K_SPACE:
                shoot()
        #if they release a key, it stops the movement
        elif ev.type == pygame.KEYUP:
            if ev.key == pygame.K_a or ev.key == pygame.K_d:
                tankx = 0
            elif ev.key == pygame.K_w or ev.key == pygame.K_s:
                tanky = 0
            #also if they press 'p', it pauses game
            elif ev.key == pygame.K_p:
                paused = True
    #only changes the tank's x and y if doing so wont make you go off the screen
    if 0 < x + tankx*movespeed < 725 and 0 < y + tanky*movespeed < 552:
        x += tankx*movespeed
        y += tanky*movespeed
    tank(x,y)

    #handles various events
    if gameCount%60 == 0: #adds score
        score += 1
    if gameCount%missileregen == 0 and missilecount < missilelimit:
        missilecount += 1 #regenerates missiles
    if gameCount%newtank == 0: #adds new tanks
        if gameCount > 9000: #handles adding fast/shielded tanks after a certain time
            newtype = random.choice("1123") #probability for each type spawning
        elif gameCount > 3000:
            newtype = random.choice("111123")
        else:
            newtype = "1"
        enemy(newtype)
    if gameCount%livesregen == 0 and lives < liveslimit:
        lives += 1 #regenerates lives
    if gameCount%600 == 0 and newtank > 2 and missileregen > 2:  #progressively makes game harder
        if gameCount < 3000:
            #makes missiles regenerate faster but enemy tanks spawn faster
            missileregen -= 2
            newtank -= 3
        else:
            missileregen -= 4
            newtank -= 4
    if gameCount%power_spawn == 0: #adds a powerup
        validspot = False
        while validspot == False:    #makes sure powerup doesn't spawn on/next to tank
            #creates a dict 'newpower' to hold powerup type and location of powerup
            newpower = {'num':random.randint(1,5), 'x':random.randint(50,650), 'y':random.randint(50, 525),'checker':0}
            #adds a rect key to the dictionary
            newpower['rect'] = pygame.Rect(newpower['x'], newpower['y'], 50,50)
            #creates a rect around the tank where powerups can't spawn
            surround = pygame.Rect(x-50, y-50, 175, 148)
            if not surround.colliderect(newpower['rect']):
                validspot = True
        #if validspot is True, it moves on and adds the dict to the list 'powerups'
        powerups.append(newpower)
    if gameCount%4000 == 0:  #progressively makes game harder
        shootrate -= 10
        e_missilespeed += 1
        
    #updates for everything, and flips screen
    updateall()
    
    if gameloop == False:  #creates a darkened copy of the screen at the end of the game
        screen.blit(images['gray'],(0,0))
        endscreen = screen.copy()
    if paused == True:
        pausescreen = screen.copy()
        pause()
    if gameCount == 1: #plays opening animations
        begin()

#handles gameover screen
name = ""
pygame.mixer.music.stop()
gameover = True
while gameover:
    #text stuff
    #rendering text and creating rects so i can center them easily
    finalscore = finalfont.render(("Final Score: "+str(score)), True, (250,250,250))
    finalrect = finalscore.get_rect(center=(400,200))

    enter = smallfont.render(("Enter Your Name:"), True, (250,250,250))
    enterrect = enter.get_rect(center=(400,270))
    name_blit = myfont.render(name, True, (255,255,255))
    name_rect = name_blit.get_rect(center=(400,350))

    #a bunch of blitting
    screen.blit(endscreen,(0,0))
    screen.blit(images['namespace'], (190,315))
    screen.blit(name_blit, name_rect)
    screen.blit(images['gameover'], (136,70))
    screen.blit(finalscore, finalrect)
    screen.blit(enter, enterrect)
    
    pygame.display.flip()

    #for typing in name
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif ev.type == pygame.KEYDOWN:
            #checks if the key pressed is a letter or a number
            #and makes sure name isn't too big
            if ev.unicode.isalnum() and len(name) < 16:
                name += ev.unicode
            #handles removing characters with backspace
            elif ev.key == K_BACKSPACE:
                name = name[:-1]
            #if enter is pressed, the name is saved
            elif ev.key == K_RETURN and len(name) > 0:
                gameover = False
                
#adds the final score to the txt file
print("FINAL SCORE: %s - %i" %(name,score))
highscores = open((path+"highscores.txt"), "a")  #adds score to highscores.txt
highscores.write(name + " " + str(score) + "\n")
highscores.close() #saves the txt file
pygame.quit()
