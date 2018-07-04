import pygame
from pygame.locals import *
import time


def initPion() :
        x = 4 #nbPlayers-1
        if x > 5 :
                x = 5
        for i in range(x):
                name = "j"
                name += str(i)
                pic = name + ".jpg"
                tabPion.append( pygame.image.load(pic).convert_alpha() )
                fenetre.blit(tabPion[i], (700+15*i,700))
                tabPion[i].set_colorkey((255,255,255))
                pygame.display.flip()


def movePion(pion,pos):
        x = 0
        y = 0
        if pos == 0 :
                x = 700 + 15 * pion
                y = 700
        elif pos < 10 and pos > 0:
                x = 700 - 65.5*pos + 15*pion
                y = 700
        elif pos == 10:
                x = 20 + 20*pion
                y = 700
        elif pos < 20 and pos > 10:
                x = 20 + 15*pion
                y = 700  - 65.5*(pos%10)
        elif pos == 20 :
                x = 20 + 20*pion
                y = 20
        elif pos < 30 and pos > 20:
                x = 110 + 65.5*((pos-1)%10) + 15*pion
                y = 20
        elif pos == 30:
                x = 700 + 20*pion
                y = 20
        elif pos < 40 and pos > 30:
                x = 700 + 15*pion
                y = 110 + 65.5*((pos-1)%10)              
        fenetre.blit(tabPion[pion], (x,y))
        pygame.display.flip()


def turnPion(posA, posB, pion): 
        for i in range(posA, (posB+1)):
                time.sleep(0.5)
                fenetre.blit(fond, (0,0)) 
                movePion(pion, i)
        refreshPion()


def refreshPion():
        a=2
        #fenetre.blit(fond, (0,0))
        #for i in range(main.nbPlayers-1):
         #       movePion(i,)

pygame.init()
fenetre = pygame.display.set_mode((800, 800))
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))
tabPion = []
initPion()
turnPion(11,11,1)
turnPion(13,20,1)
turnPion(20,34,1)
turnPion(30,32,1)
pygame.display.flip()




                        
