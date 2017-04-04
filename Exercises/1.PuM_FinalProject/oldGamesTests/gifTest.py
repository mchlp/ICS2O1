import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill((100,100,100))



class Tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("tank1.png").convert_alpha()
        self.rect = self.image.get_rect()

clock = pygame.time.Clock()
tank1 = Tank()
tankImage = pygame.image.load("tank1.png").convert_alpha()
tanksList = pygame.sprite.Group()
tanksList.add(tank1)
tanksList.draw(screen)
bg = pygame.image.load("dirt.jpg").convert_alpha()

dim = tankImage.get_width()

x = 600/2-dim
y = 600/2-dim
movex,movey = 0,0

keepGoing = True
while keepGoing:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            keepGoing = False
        if event.type == KEYDOWN:
            if event.key == K_a:
                movex = -3
            elif event.key == K_d:
                movex = 3
            elif event.key == K_w:
                movey = -3
            elif event.key == K_s:
                movey = 3
        if event.type == KEYUP:
            if event.key == K_a or event.key == K_d:
                movex = 0
            if event.key == K_w or event.key == K_s:
                movey = 0

    x += movex
    y += movey

    tank1.rect.x = x
    tank1.rect.y = y
    
    screen.blit(bg, (0,0))
    tanksList.draw(screen)

    pygame.display.update()
