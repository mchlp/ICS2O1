#importing
import pygame
import sys
import os
import time
from pygame.locals import *
#import platform
import platform

path = "menu\\"
curPath = os.getcwd()

#for TDSB computers
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
pygame.init()
#Set up screens
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tank Wars")
#backgrounds
title = pygame.image.load(path+"tank_title.png").convert_alpha()
inst_title = pygame.image.load(path+"tank_instructions.png").convert_alpha()
back = pygame.image.load(path+"tank_background.jpg").convert()
game_select = pygame.image.load(path+"tank_garage.jpg").convert()
instructions1 = pygame.image.load(path+"tank_blueprint3.jpg").convert()
#set logo
pygame.display.set_icon(pygame.image.load(path+"icon.png"))

#highscore stuff
t_highscores = pygame.image.load(path+"tank_highscore.jpg").convert()
numbers = pygame.image.load(path+"numbers.png").convert_alpha()
highscore_title = pygame.image.load(path+"tank_highscores.png").convert_alpha()
gray1 = pygame.image.load(path+"graybar1.png").convert_alpha()
gray2 = pygame.image.load(path+"graybar2.png").convert_alpha()
#set up music
menu_music = pygame.mixer.music.load(path+'daredevil.wav')
pygame.mixer.music.play(-1)
#instruction images
hearts = pygame.image.load(path+"hearts.png").convert_alpha()
ammo = pygame.image.load(path+"ammo.png").convert_alpha()
powerup = pygame.image.load(path+"powerup5.png").convert_alpha()
metal = pygame.image.load(path+"metalplate.png").convert_alpha()
wasd = pygame.image.load(path+"wasd.png").convert_alpha()
spacebar = pygame.image.load(path+"space.png").convert_alpha()
pause = pygame.image.load(path+"p.png").convert_alpha()
#buttons
b_start = pygame.image.load(path+"button_start.gif").convert()
b_back = pygame.image.load(path+"button_back.gif").convert()
b_inst = pygame.image.load(path+"button_instructions.gif").convert()
b_quit = pygame.image.load(path+"button_quit.gif").convert()
b_start1 = pygame.image.load(path+"button_start (1).gif").convert()
b_back1 = pygame.image.load(path+"button_back (1).gif").convert()
b_inst1 = pygame.image.load(path+"button_instructions (1).gif").convert()
b_quit1 = pygame.image.load(path+"button_quit (1).gif").convert()
b_single = pygame.image.load(path+"button_single.gif").convert()
b_single1 = pygame.image.load(path+"button_single (1).gif").convert()
b_two = pygame.image.load(path+"button_two.gif").convert()
b_two1 = pygame.image.load(path+"button_two (1).gif").convert()
b_right = pygame.image.load(path+"arrow_r.gif").convert()
b_right1 = pygame.image.load(path+"arrow_r (1).gif").convert()
b_left = pygame.image.load(path+"arrow_l.gif").convert()
b_left1 = pygame.image.load(path+"arrow_l (1).gif").convert()
b_high = pygame.image.load(path+"button_highscores.gif").convert_alpha()
b_high1 = pygame.image.load(path+"button_highscores (1).gif").convert_alpha()
#font
bigfont = pygame.font.SysFont("impact", 40)
myfont = pygame.font.SysFont("impact", 30)
smallfont = pygame.font.SysFont("impact", 25)
#text

insts = '''Single Player'''
instm = '''Multi Player'''
insts2 = '''Survive as long as you can'''
insts3 = "against waves of enemy tanks!"
instm2 = '''Destroy your opponents'''
instm3 = '''and be the last one standing!'''
insth = '''Remaining Health'''
insta = '''Remaining Ammo'''
instp = '''Collect various powerups'''
instp2 = '''Discover what they all do!'''
instc = 'Up'
instc2 = 'Left   Down   Right'
instc3 = 'Shoot'
instc4 = 'Controls'
instc5 = 'Pause'

#first page of instructions
#creates a list of everything that needs to be displayed
mess1s = [insts,insts2,insts3,instm,instm2,instm3]
#locations of where i want them to be displayed
mess1centers = [165,200,235,285,320,355]

def mess1():
    for i in range(6): #runs through what i want to be displayed and the locations
        if i == 0 or i == 3: #for 'Single Player' and 'Multi Player'
            blit = bigfont.render(mess1s[i], True, (194,72,39))
        else: #for everything else
            blit = myfont.render(mess1s[i], True, (77,82,86))

        #adds to screen, centers the text    
        rect = blit.get_rect(center=(320,mess1centers[i]))
        screen.blit(blit, rect)

#second page of instructions
mess2s = [instc, instc2, instc3, instc4, instc5]
mess2centers = [(170,165),(100,290), (320,290),175,(460,290)]

def mess2():
    #adds images to screen
    screen.blit(wasd, (110,200))
    screen.blit(spacebar, (285,246))
    screen.blit(pause, (465,246))
    for i in range(5):
        if i == 3:
            blit = bigfont.render(mess2s[i], True, (194,72,39))
            rect = blit.get_rect(center=(320, mess2centers[i]))
            screen.blit(blit, rect)
        else:
            blit = smallfont.render(mess2s[i], True, (77,82,86))
            screen.blit(blit, mess2centers[i])
        

#third page of instructions
mess3s = [instp,instp2,insth,insta]
mess3centers = [170,200,255,315]

def mess3():
    screen.blit(hearts,(130,250))
    screen.blit(ammo, (130,310))
    screen.blit(powerup, (130,178))
    for i in range(4):
        blit = myfont.render(mess3s[i], True,(77,82,86))
        screen.blit(blit,(210,mess3centers[i]))
#set up functions
def add(a,x,y):
    '''adds something to the screen'''
    screen.blit(a,(x,y))
def update():
    '''updates screen'''
    pygame.display.flip()
def button(x,y,l,w):
    '''takes position of button and size of button,
       then checks if the event is in the button'''
    if x+l > pos[0] > x and y+w > pos[1] > y:
        return True
    else:
        return False
def clear():
    '''removes all events so the player can't spam buttons'''
    pygame.event.clear()
    
#game loop
state = 'menu'
clock = pygame.time.Clock()
keepgoing = True
#Loads for the first time
x = 0
#for the instructions screen
y = 0
while keepgoing:
    clock.tick(60)
    if state == 'menu':
        #Loads for the first time
        #every time it switches to another state, x becomes 0
        #every time it returns to menu, x becomes 1
        if x == 0:
            add(back, 0,0)
            add(title, 80, 50)
            add(b_start, 270, 150)
            add(b_inst, 225, 230)
            add(b_high, 229, 310)
            add(b_quit, 270, 390)
            update()
            x = 1
        for ev in pygame.event.get(): #handles game events
            if ev.type == pygame.QUIT: #quits game
                pygame.quit()
                quit()
            pos = pygame.mouse.get_pos() #gets position of mouse
            #if the mouse is over a button, it blits the highlighted
            #version. otherwise, it blits the normal version
            if button(270,150,101,41):
                add(b_start1, 270, 150)
            else:
                add(b_start, 270, 150)
                
            if button(225,230,191,41):
                add(b_inst1, 225, 230)
            else:
                add(b_inst, 225, 230)
                
            if button(229,310,183,41):
                add(b_high1, 229, 310)
            else:
                add(b_high, 229, 310)
                
            if button(270,390,94,41):
                add(b_quit1, 270, 390)
            else:
                add(b_quit, 270, 390)
            update()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                pos = ev.pos
                #changes the stte based which button is pressed
                if button(270,150,101,41):
                    state = 'game_select'
                    #so you can't spam click
                    clear()
                    break
                elif button(225,230,191,41):
                    state = 'inst'
                    clear()
                    break
                elif button(229,310,183,41):
                    state = 'highscores'
                    clear()
                    break
                elif button(270,390,94,41):
                    pygame.quit()
                    quit()
    elif state == 'game_select':
        if x == 1:   #loads for the first time
            add(game_select, 0, 0)
            add(title, 80, 50)
            add(b_single, 219, 150)
            add(b_two, 219, 250)
            add(b_back, 270, 350)
            update()
            clear()
            x = 0
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            #checks if mouse is over a button
            if button(219,150,202,41):
                add(b_single1, 219, 150)
            else:
                add(b_single, 219, 150)
            if button(219,250,204,41):
                add(b_two1, 219, 250)
            else:
                add(b_two, 219, 250)
            if button(270,350,94,41):
                add(b_back1, 270, 350)
            else:
                add(b_back, 270, 350)
            update()
            if ev.type == pygame.QUIT:
                state = 'menu'
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                pos = ev.pos
                if button(270,350,99,41):
                    state = 'menu'
                    clear()
                    break
                elif button(219,150,202,41):
                    state = 'single'
                    clear()
                    break
                elif button(219,250,202,41):
                    state = 'two'
                    clear()
                    break
    elif state == 'inst':
        if x == 1:  #loads for the first time
            add(instructions1,0,0)
            add(inst_title, 45, 20)
            add(b_back, 270, 420)
            screen.blit(metal, (0,95))
            #checks which page of instructions the user is on,
            #then adds the text based on that
            #0 = first page, 1 = second, 2 = third
            #adds arrows accordingly, and appropriate function
            if y == 0:
                mess1()
                add(b_right, 565, 200)
            elif y == 1:
                mess2()
                add(b_right, 565, 200)
                add(b_left, 16, 200)
            elif y == 2:
                mess3()
                add(b_left, 16, 200)
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            #highlights buttons if you mouse over them,
            #and only checks if you're on a page with that particular button
            if y == 0 or y == 1:
                if button(565,200,61,100):
                    add(b_right1, 565, 200)
                else:
                    add(b_right, 565, 200)
            if y == 1 or y == 2:
                if button(16,200,61,100):
                    add(b_left1, 16, 200)
                else:
                    add(b_left, 16, 200)
            if button(270,420,94,41):
                add(b_back1, 270, 420)
            else:
                add(b_back, 270, 420)
            update()
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            #handles arrow key selection for moving from instructions screens
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                pos = ev.pos
                if button(270,420,99,41):
                    x = 0
                    state = 'menu'
                    clear()
                    break
                elif button(565,200,61,100):
                    if y < 2:
                        y+=1
                elif button(16,200,61,100):
                    if y > 0:
                        y-=1
    elif state == 'highscores':

        if x == 1:
            screen.fill((0,0,0))
            screen.blit(t_highscores, (0,0))
            screen.blit(highscore_title, (70, 0))

            highscores = open("singleplayer/single_player/highscores.txt", "r")#opens txt file
            scores = {} #creates a blank dictionary
            for score in highscores: #cycles through everything in txt file
                #separates name from score
                space = score.find(" ") 
                newline = score.find("\n")
                name = score[:space]
                point = int(score[space+1:newline])
                #adds the name and score to the dictionary 'scores'
                scores[point] = name
            #sorts the highscores and stores it in variable 'highs'
            highs = sorted(scores)
            top5 = []
            for place in range(1,6):
                #adds the last 5 from 'highs', which are the highest 5 scores
                top5.append(highs[-(place)])
            add(b_back, 270, 420)
            topnum = 1 #keeps track of the number of highscores displayed
            for top in top5: #for actually displaying the names/scores
                toppos = topnum*65 #separates each name/score by 65
                top_name = scores[top] #gets string of name
                #renders the score and the name
                top_blit = bigfont.render(top_name, True, (250,250,250))
                top_blit2 = bigfont.render(str(top), True, (250,250,250))
                #adds the gray bars
                if topnum%2 == 0:
                    screen.blit(gray1, (0,toppos+20))
                else:
                    screen.blit(gray2, (0,toppos+20))
                #displays score and name
                screen.blit(top_blit, (100,toppos+25))
                screen.blit(top_blit2, (500,toppos+25))
                screen.blit(numbers, (-10,60))
                topnum += 1
            x = 0

        #button handling
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if button(270,420,94,41):
                add(b_back1, 270, 420)
            else:
                add(b_back, 270, 420)
                
            pygame.display.flip()

            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                pos = ev.pos
                if button(270,420,94,41):
                    state = 'menu'
                    clear()
                    break
        
    elif state == 'single':
        pygame.display.quit()
        os.system(curPath+"/singleplayer/Single_Player.py")
        pygame.display.init()
        size = (640, 480)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Tank Wars")
        state = 'menu'
        #put single player here
    elif state == 'two':
        pygame.display.quit()
        os.system(curPath+'/multiplayer/multiplayer.py')
        pygame.display.init()
        size = (640, 480)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Tank Wars")
        state = 'menu'
        #put multi player here
                
