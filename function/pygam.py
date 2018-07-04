from const.player import Player
from const.boardGame import Boxes
from function.cards import *
from function.turn import *
from function.moneyExchange import *
from function.placement import *
from function.printf import *
from function.init import *
# Initialise les pions
def initPion() :
        x = nbPlayers
        if x > 5 :
                x = 5
        for i in range(x):
                name = "j"
                name += str(i)
                path = "picture/" + name + ".jpg"
                tabPion.append( pygame.image.load(path).convert_alpha() )
                fenetre.blit(tabPion[i], (700+15*i,700))
                tabPion[i].set_colorkey((255,255,255))
                pygame.display.flip()


# Mouvement d'un pion
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

# Mouvemements d'un pion lors d'un tour
def turnPion(posA, posB, pion): 
        for i in range(posA, (posB+1)):
                time.sleep(0.5)
                fenetre.blit(fond, (0,0)) 
                movePion(pion, i)
        refreshPion()

# Rafraichi plateau
def refreshPion():
        fenetre.blit(fond, (0,0))
        for i in range(nbPlayers):
                movePion(i,tabPlayers[i].position)


def pygame() :
        pygame.init()
        fenetre = pygame.display.set_mode((800, 800))
        fond = pygame.image.load("picture/background.jpg").convert()
        fenetre.blit(fond, (0,0))
        initPion()
        run = 1
        while run:
                for event in pygame.event.get():
                        if event.type == QUIT:
                                run = 0
                                pygame.quit()
                                break