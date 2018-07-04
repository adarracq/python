from const.player import Player
from const.boardGame import Boxes
from function.cards import *
from function.turn import *
from function.moneyExchange import *
from function.placement import *
from function.init import haveProp
from function.pygam import *

# Affiche etat de la partie 
def printState(tabPlayers, nbPlayers):
        for i in range(nbPlayers):
                print "Joueur " , tabPlayers[i].name , " est case ", tabPlayers[i].position , " et a ", tabPlayers[i].money, " euros"


#Impression d'une case
def printCase(tabPlayers,pos) :
        print "\n-------------------------------------------"
        print "Vous etes pos " , pos #rajouter les autres joueurs
        if Boxes[pos]["type"] == 0 :
                print "\n" , Boxes[pos]["name"]
                if Boxes[pos]["moveMoney"] <100 :
                        print "\n Vous perdez " , Boxes[pos]["moveMoney"]
                else :
                        print "\n Vous gagnez " , Boxes[pos]["moveMoney"]

        if Boxes[pos]["type"] == 1 :
                print "\n" + Boxes[pos]["name"]
                haveProp(tabPlayers,pos)
                print "\nPrix : " , Boxes[pos]["price"]
                print "\nTaxe :  " , Boxes[pos]["TaxPrice"][0] , " pour 1 maison"
                print "        " , Boxes[pos]["TaxPrice"][1] , " pour 2 maisons"
                print "        " , Boxes[pos]["TaxPrice"][2] , " pour 3 maisons"
                print "        " , Boxes[pos]["TaxPrice"][3] , "pour 4 maisons"
                print "\nPrix d'une maison : " , Boxes[pos]["homesPrice"]

        if Boxes[pos]["type"] == 2 :
                print "\nBienvenue a " , Boxes[pos]["name"]
                haveProp(tabPlayers,pos)
                print "\nPrix : " , Boxes[pos]["price"]
                print "\nTaxe :  25  pour 1"
                print "        50  pour 2"
                print "        100 pour 3"
                print "        200 pour 4"
                
        if Boxes[pos]["type"] == 3 :
                print "\nBienvenue en degrisement..."
                
        if Boxes[pos]["type"] == 4 :
                print "\nBienvenue a la " , Boxes[pos]["name"]
                haveProp(tabPlayers, pos)
                print "\nPrix : " , Boxes[pos]["price"]
                print "\nTaxe :  x4 pour une compagnie"
                print "        x10 pour les 2"
                
        if Boxes[pos]["type"] == 5 :
                print "\nBienvenue au " , Boxes[pos]["name"]
                
        if Boxes[pos]["type"] == 6 :
                print "\nCAISSE COMMUNAUTE"
                
        if Boxes[pos]["type"] == 7 :
                print "\nCARTE CHANCE"
