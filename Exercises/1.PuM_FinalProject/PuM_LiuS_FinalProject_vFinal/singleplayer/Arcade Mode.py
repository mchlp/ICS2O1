#try:
#Single Player
creator_mode = False   #so you don't die if you're testing something

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
kills = 0
path = "single_player\\"
schoolcomputer = True

def loadimages():
    global images
    images = {}
    images["tank1"] = pygame.image.load(path+"tank1.png").convert_alpha()
    images["missileL"] = pygame.image.load(path+"missile.png").convert_alpha()
    images["ammo"] = pygame.image.load(path+"ammo.png").convert_alpha()
    images["heart"] = pygame.image.load(path+"hearts.png").convert_alpha()
    images["dirt"] = pygame.image.load(path+"dirt.jpg").convert()
    images["enemy1"] = pygame.image.load(path+"tank2L.png").convert_alpha()
    images["missileR"] = pygame.image.load(path+"missileL.png").convert_alpha()
    images["powerup1"] = pygame.image.load(path+"powerup1.jpg").convert()
    images['gray'] = pygame.image.load(path+"gray.png").convert_alpha()
    images['gameover'] = pygame.image.load(path+"gameover.png").convert_alpha()
    images['laser'] = pygame.image.load(path+"laser.png").convert_alpha()
    images['shield'] = pygame.image.load(path+"shield.png").convert_alpha()
    images['namespace'] = pygame.image.load(path+"namespace.png").convert_alpha()
    for i in range(1,6):
        images["redgradient"+str(i)] = pygame.image.load(path+"redgradient"+str(i)+".png").convert_alpha()

    for i in range(1,5):
        images['begin'+str(i)] = pygame.image.load(path+"begin"+str(i)+".png").convert_alpha()
    for i in range(2,6):
        images["powerup"+str(i)] = pygame.image.load(path+"powerup"+str(i)+".png").convert_alpha()
    for explosionImage in range(1, 20):
        images["explosion"+str(explosionImage)] = pygame.image.load(path+"explosions\\explosion" + str(explosionImage) + ".gif").convert_alpha()


loadimages()
explosions = []
sounds = {} 
sounds['explosionsound'] = pygame.mixer.Sound(file=path+"explosionsound.ogg")
sounds['explosionsound'].set_volume(0.5)
sounds['repulsor'] = pygame.mixer.Sound(file=path+"repulsor.ogg")

#set up missiles
missilespeed = 10
e_missilespeed = 10
missiles = []
enemy_missiles = []

#set up tank
x = 10
y = 400
missilecount = 5
missilelimit = 5
missileregen = 10
movespeed = 3
lives = 5
liveslimit = 5
livesregen = 300
missiles = []
tankx = 0
tanky = 0
collide = True
redscreens = []
redcount = 0

#set up enemies
enemies = []
newtank = 20
enemy_missiles = []
enemyspeed = 1
shootrate = 100

#powerups
powerups = []
power_spawn = 300

#font
fontsize = 35
myfont = pygame.font.SysFont("impact", 45)
smallfont = pygame.font.SysFont("impact", 40)
bigfont = pygame.font.SysFont("impact", 70)
finalfont = pygame.font.SysFont("impact", 55)

#set up pause
paused = False
pausemess = bigfont.render("PAUSED", True, (250,250,250))
pauserect = pausemess.get_rect(center=(400,300))

#functions
def begin():
    'beginning animation'
    startscreen = screen.copy()
    for i in range(1,5):
        screen.blit(startscreen, (0,0))
        pygame.display.flip()
        time.sleep(0.5)
        rect = images['begin'+str(i)].get_rect(center=(400,300))
        screen.blit(images["begin"+str(i)], rect)
        pygame.display.flip()
        time.sleep(0.5)
        pygame.event.clear()   #so you can't issue commands in the beginning animation
    if not schoolcomputer:
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
        newmissile = {'x':x+70, 'y':y+20}
        missiles.append(newmissile)
        missilecount -= 1
def updatemissiles():
    'moves missiles'
    for missile in missiles:
        missile['x'] += missilespeed
        if missile['x'] >= 800:
            missiles.remove(missile)
        else:
            screen.blit(images["missileL"], (missile['x'],missile['y']))
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
    for i in range(1, lives+1):
        screen.blit(images["heart"], (i*60 - 50, 5))
    for i in range(1, missilecount+1):
        screen.blit(images["ammo"], (i*60 + 440, 5))
    scoreblit = medfont.render(("Kills: "+str(kills)), True, (255,255,255))
    scorerect = scoreblit.get_rect(center=(400,25))
    if scorerect.x > 380:
        fontsize -= 1
    screen.blit(scoreblit, scorerect)
    if lives <= 0:
        if creator_mode:  #so i don't die when im testing something
            pass
        else:
            print("YOU LOSE")
            gameloop = False
def enemy(newtype):
    'creates a new enemy tank'
    enemyx = 799
    enemyy = random.randint(50, 552)
    newenemy = {'x':enemyx, 'y':enemyy,'type':newtype}
    enemies.append(newenemy)
def updateenemies():
    'moves enemy tanks'
    global lives
    for enemy in enemies:
        if enemy['type'] == "2":
            enemy['x'] -= enemyspeed*2
        else:
            enemy['x'] -= enemyspeed
        if enemy['x'] < 1:
            enemies.remove(enemy)
            redscreen = {'count':redcount}
            redscreens.append(redscreen)
            lives -= 1
        else:
            screen.blit(images["enemy1"], (enemy['x'],enemy['y']))
            if enemy['type'] == '3':
                screen.blit(images['shield'], (enemy['x']-12,enemy['y']-26))

def enemyshoot():
    'adds new missiles based on position of enemy tanks'
    for enemy in enemies:
        newmissile = {'x':enemy['x'], 'y':enemy['y']+20}
        enemy_missiles.append(newmissile)
def checkcollide():
    'checks for collision with tanks and missiles'
    global enemies
    global missiles
    global x
    global y
    global lives
    global explosions
    global kills
    t_rect = pygame.Rect(x,y,75,48)
    for enemy in enemies: #checks if I hit a tank
        e_rect = pygame.Rect(enemy['x'], enemy['y'], 75, 48)
        if e_rect.colliderect(t_rect):
            if collide == True:
                redscreen = {'count':redcount}
                redscreens.append(redscreen)
                lives -= 1
            if enemy['type'] == '3':
                enemy['type'] = '1'
            else:
                expl_rect = pygame.Rect(e_rect.x-37, e_rect.y-24, 75, 48)
                newexplosion = {'num':1,'rect':expl_rect,'counter':1,'music':True}
                kills += 1
                explosions.append(newexplosion)
                enemies.remove(enemy)
        for missile in missiles: #checks if enemy tanks get hit
            m_rect = pygame.Rect(missile['x'], missile['y'], 36, 9)
            if e_rect.colliderect(m_rect):
                try:
                    if enemy['type'] == '3':
                        enemy['type'] = '1'
                    else:
                        expl_rect = pygame.Rect(e_rect.x-37, e_rect.y-24, 75, 48)
                        newexplosion = {'num':1,'rect':expl_rect,'counter':1,'music':True}
                        explosions.append(newexplosion)
                        enemies.remove(enemy)
                        kills += 1
                    missiles.remove(missile)
                except:
                    pass
    for missile in enemy_missiles: #checks if i get hit
        em_rect = pygame.Rect(missile['x'], missile['y'], 36, 9)
        if em_rect.colliderect(t_rect):
            if collide == True:
                redscreen = {'count':redcount}
                redscreens.append(redscreen)
                lives -= 1
                expl_rect = pygame.Rect(t_rect.x-37, t_rect.y-24, 75, 48)
                newexplosion = {'num':1,'rect':expl_rect,'counter':1,'music':True}
                explosions.append(newexplosion)
            enemy_missiles.remove(missile)
        for missile2 in missiles:
            e_rect = pygame.Rect(missile2['x'],missile2['y'], 36,9)
            if e_rect.colliderect(em_rect):
                try:
                    missiles.remove(missile2)
                    enemy_missiles.remove(missile)
                except:
                    pass
                
def pause():
    'pause function'
    global paused
    pygame.mixer.music.pause()
    while paused:
        screen.blit(pausescreen, (0,0))
        screen.blit(images['gray'],(0,0))
        screen.blit(pausemess, pauserect)
        pygame.display.flip()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif ev.type == pygame.KEYUP:
                if ev.key == K_p:
                    paused = False
                    pygame.mixer.music.unpause()
start = 1 #this helps me determine the duration of certain powerups based on gameCount
def powerup():
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
    global kills
    t_rect = pygame.Rect(x, y, 70, 48)
    for power in powerups:
        border = pygame.Rect(power['x'], power['y'], 50, 50)
        if power['num'] == 1: #destroy all tanks
            screen.blit(images['powerup'+str(power['num'])], (power['x'],power['y']))
            pygame.draw.rect(screen, (0,0,0), border, 4)
            if t_rect.colliderect(power['rect']):
                for enemy in enemies:
                    e_rect = pygame.Rect(enemy['x'], enemy['y'], 75, 48)
                    expl_rect = pygame.Rect(e_rect.x-37, e_rect.y-24, 75, 48)
                    newexplosion = {'num':1,'rect':expl_rect,'counter':1, 'music':True}
                    explosions.append(newexplosion)
                    kills += 1
                enemies = []
                powerups.remove(power)

        elif power['num'] == 2: #fire death laser of death
            if power['checker'] == 0:
                screen.blit(images['powerup'+str(power['num'])], (power['x'],power['y']))
                pygame.draw.rect(screen, (0,0,0), border, 4)
                if t_rect.colliderect(power['rect']):
                    sounds['repulsor'].play()
                    start = gameCount
                    missilecount = 5
                    power['checker'] = 1
            else:
                if gameCount > start+10:
                    screen.blit(images['laser'], (x+75, y-76))
                    laser = pygame.Rect(x+75, y-23, 800,97)
                    if gameCount > start+310:
                        start = 1
                        powerups.remove(power)
                    else:
                        for enemy in enemies:
                            e_rect = pygame.Rect(enemy['x'], enemy['y'], 75, 48)
                            if laser.colliderect(e_rect):
                                try:
                                    expl_rect = pygame.Rect(e_rect.x-37, e_rect.y-24, 75, 48)
                                    newexplosion = {'num':1,'rect':expl_rect,'counter':1,'music':True}
                                    explosions.append(newexplosion)
                                    enemies.remove(enemy)
                                    kills += 1
                                except:
                                    pass
                        for missile in enemy_missiles:
                            em_rect = pygame.Rect(missile['x'], missile['y'], 36, 9)
                            if laser.colliderect(em_rect):
                                try:
                                    enemy_missiles.remove(missile)
                                except:
                                    pass

        elif power['num'] == 3: #restore health/ammo
            screen.blit(images['powerup'+str(power['num'])], (power['x'],power['y']))
            pygame.draw.rect(screen, (0,0,0), border, 4)
            if t_rect.colliderect(power['rect']):
                lives = 5
                missilecount = 5
                powerups.remove(power)
        elif power['num'] == 4: #overdrive
            if power['checker'] == 0:
                screen.blit(images['powerup'+str(power['num'])], (power['x'],power['y']))
                pygame.draw.rect(screen, (0,0,0), border, 4)
                if t_rect.colliderect(power['rect']):
                    start = gameCount
                    power['checker'] = 1
            else:
                screen.blit(images['shield'], (t_rect.x-12,t_rect.y-26))
                movespeed = 12
                collide = False
                if gameCount > start+300:
                    movespeed = 3
                    collide = True
                    powerups.remove(power)
        elif power['num'] == 5: #reverse missiles
            screen.blit(images['powerup'+str(power['num'])], (power['x'],power['y']))
            pygame.draw.rect(screen, (0,0,0), border, 4)
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
            sounds['explosionsound'].play()
            explosion['music'] = False
        screen.blit(images[("explosion"+str(explosion['num']))],(explosion['rect']))
        explosion['counter'] += 1
        if explosion['counter']%3 == 0:
            explosion['num'] += 1
        if explosion['num'] == 20:
            explosions.remove(explosion)
def updatered():
    for red in redscreens:
        if red['count'] > 9:
            redscreens.remove(red)
        elif red['count'] <= 5:
           # if red['count'] > 5:
            screen.blit(images['redgradient1'], (0,0))
            red['count'] += 1
        elif red['count'] > 5:
            screen.blit(images['redgradient'+str(red['count']-4)], (0,0))
            if gameCount%5 == 0:
                red['count'] += 1

#actual game loop
gameloop = True
gameCount = 0
while gameloop:
    clock.tick(60)
    gameCount += 1
    screen.blit(images["dirt"], (0,0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_w:
                tanky = -1
            elif ev.key == pygame.K_d:
                tankx = 1
            elif ev.key == pygame.K_s:
                tanky = 1
            elif ev.key == pygame.K_a:
                tankx = -1
            elif ev.key == pygame.K_SPACE:
                shoot()
            elif ev.key == pygame.K_k:
                gameloop = False #for testing
        elif ev.type == pygame.KEYUP:
            if ev.key == pygame.K_a or ev.key == pygame.K_d:
                tankx = 0
            elif ev.key == pygame.K_w or ev.key == pygame.K_s:
                tanky = 0
            elif ev.key == pygame.K_p:
                paused = True
    if 0 < x + tankx*movespeed < 725 and 0 < y + tanky*movespeed < 552:
        x += tankx*movespeed
        y += tanky*movespeed
    tank(x,y)

    #handles various events
    if gameCount%missileregen == 0 and missilecount < missilelimit:
        missilecount += 1
    if gameCount%newtank == 0:
        if gameCount > 9000:
            newtype = random.choice("1123") #probability for each type spawning
        elif gameCount > 3000:
            newtype = random.choice("111123")
        else:
            newtype = "1"
        enemy(newtype)
    if gameCount%livesregen == 0 and lives < liveslimit:
        lives += 1
    if gameCount%shootrate == 0:
        enemyshoot()
    if gameCount%power_spawn == 0:
        validspot = False
        while validspot == False:    #makes sure powerup doesn't spawn on/next to tank
            newpower = {'num':random.randint(1,5), 'x':random.randint(50,650), 'y':random.randint(50, 525),'checker':0}
            newpower['rect'] = pygame.Rect(newpower['x'], newpower['y'], 50,50)
            surround = pygame.Rect(x-50, y-50, 175, 148)
            if not surround.colliderect(newpower['rect']):
                validspot = True
        powerups.append(newpower)
    if gameCount%4000 == 0:  #progressively makes game harder
        shootrate -= 10
        e_missilespeed += 1
        
    #updates for everything
    updatemissiles()
    updateenemies()
    checkcollide()
    powerup()
    updatestatus()
    updateexplosions()
    updatered()
    pygame.display.flip()
    
    if gameloop == False:  #creates a darkened copy of the screen at the end of the game
        screen.blit(images['gray'],(0,0))
        endscreen = screen.copy()
    if paused == True:
        pausescreen = screen.copy()
        pause()
    if gameCount == 1: #plays opening animations
        begin()
name = ""
pygame.mixer.music.stop()
gameover = True
while gameover:
    #text stuff
    screen.blit(endscreen,(0,0))
    finalscore = finalfont.render(("Final Score: "+str(kills)), True, (250,250,250))
    finalrect = finalscore.get_rect(center=(400,200))

    enter = smallfont.render(("Enter Your Name:"), True, (250,250,250))
    enterrect = enter.get_rect(center=(400,290))
    name_blit = myfont.render(name, True, (255,255,255))
    name_rect = name_blit.get_rect(center=(400,350))
    #name_space = pygame.Rect(190,315,420,70)
    #pygame.draw.rect(screen, (50,50,50), name_space)
    screen.blit(images['namespace'], (190,315))
    screen.blit(name_blit, name_rect)
    screen.blit(images['gameover'], (136,70))
    screen.blit(finalscore, finalrect)
    screen.blit(enter, enterrect)
    
    pygame.display.flip()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif ev.type == pygame.KEYDOWN:
            if ev.unicode.isalnum() and len(name) < 16:
                name += ev.unicode
            elif ev.key == K_BACKSPACE:
                name = name[:-1]
            elif ev.key == K_RETURN:
                gameover = False
pygame.quit()
quit()
#except:
#   print("Samuel has messed up. Please contact him and laugh in his face.")
