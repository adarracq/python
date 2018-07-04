from const.player import Player
from const.boardGame import Boxes
from function.cards import *
from function.turn import *
from function.moneyExchange import *
from function.init import *
from function.printf import *
from function.pygam import *

# Action lorsque un joueur arrive sur une propriete
def onAPropertie(tabPlayers,player):
        pos = tabPlayers[player].position
        prop = Boxes[pos]["proprietaire"]
        if prop == player :
                print " Bienvenue chez vous"
                print " 1 Pour acheter une maison"
                print " 2 Pour passer"
                choice = int(input("Votre choix : "))
                if choice == 1 :
                        putHome(player)
                elif choice != 2 :
                        print " 1 Pour acheter une maison"
                        print " 2 Pour passer"
                        choice = int(input("Votre choix : "))
        elif prop > -1 :
                homesTax(tabPlayers,player)
        else :
                print "\n 1 Pour acheter"
                print " 2 Pour passer"
                choice = int(input("Votre choix : "))
                if choice == 1 :
                        buyCase(tabPlayers,player)


# Action lorsque un joueur arrive sur une gare
def onAGare(tabPlayers,player):
        pos = tabPlayers[player].position
        prop = Boxes[pos]["proprietaire"]    
        if prop == player :
                print "Bienvenue chez vous"
        elif prop > -1 :
                tax = gareTax(tabPlayers,player)
                tabPlayers[player].moveMoney( -tax )
                tabPlayers[prop].moveMoney( tax )
        else :
                print "\n 1 Pour acheter"
                print " 2 Pour passer"
                choice = int(input("Votre choix : "))
                if choice == 1 :
                        buyCase(tabPlayers,player)


# Action lorsque un joueur arrive sur une compagnie de distribution
def onDistrib(tabPlayers,player, score):
        pos = tabPlayers[player].position
        prop = Boxes[pos]["proprietaire"]    
        if prop == player :
                print "Bienvenue chez vous"
        elif prop > -1 :
                tax = distribTax(player) * score
                tabPlayers[player].moveMoney( -tax )
                tabPlayers[prop].moveMoney( tax )
        else :
                print " 1 Pour acheter"
                print " 2 Pour passer"
                choice = int(input("Votre choix : "))
                if choice == 1 :
                        buyCase(tabPlayers,player)


# Action lorsque un joueur arrive en prison
def onJail(nTry):
        print "Ethylo numero : ", nTry
        fDice = throwDice()
        sDice = throwDice()
        if fDice == sDice :
                print "Felicitation vous avez decuve"
                return 1
        else :
                print "Encore saoul, essayez au prochain tour..."
                return 0                   
