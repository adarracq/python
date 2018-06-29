import pygame
from pygame.locals import *
import time

pygame.init()


fenetre = pygame.display.set_mode((800, 800))


fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))



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


def turn(posA, posB, pion): 
        for i in range(posA, posB+1):
                time.sleep(0.5)
                fenetre.blit(fond, (0,0)) 
                movePion(pion, i)


def refreshPion():
        fenetre.blit(fond, (0,0))
        #for i in range(nbPlayers-1):
                #movePion(tabPion[i],tabPlayers[i].position)

tabPion = []
initPion()
movePion(0,25)
turn(0,39,1)
pygame.display.flip()



continuer = 1

#Boucle infinie
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0
			
