import pygame
import time
import random
from pygame.locals import *
from const.player import Player
from const.boardGame import Boxes
from function.cards import chanceCards
from function.cards import communityCards
from function.init import *
from function.cards import *
from function.turn import *
from function.moneyExchange import *
from function.placement import *
from function.printf import *
from function.pygam import *

# type :
# 0 gagne/perd de l'argent
# 1 batiment
# 2 gare
# 3 prison
# 4 compagnie distrib
# 5 rien
# 6 caisse communautaire
# 7 chance


#-------------------------------------------------------------CARDS-----------------------------------------------------------------#


#-------------------------------------------------------------PRINT-----------------------------------------------------------------#


#-------------------------------------------------------------INITIALISATION-----------------------------------------------------------------#


#-------------------------------------------------------------GAME TURN-----------------------------------------------------------------#


#-----------------------------------------------------------MONEY EXCHANGE--------------------------------------------------------------#


#-----------------------------------------------------------PLACEMENT--------------------------------------------------------------#


#-----------------------------------------------------------PYGAME--------------------------------------------------------------#


#-----------------------------------------------------------INIT GAME--------------------------------------------------------------#                        

# Init partie
tabPlayers = []
tabPion = []
nbPlayers = initGame(tabPlayers)

# Lancement partie
Game(tabPlayers, nbPlayers)




