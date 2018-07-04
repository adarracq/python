from const.player import Player
from const.boardGame import Boxes
from function.cards import *
from function.init import *
from function.moneyExchange import *
from function.placement import *
from function.printf import *
from function.pygam import *

#Simule un lance de de
def throwDice():
        dice = random.randrange(1, 7, 1)
        print "De : " , dice
        return dice

# Deplacement d'un joueur
def move(tabPlayers,player):
        raw_input("Appuyez sur entree pour lancer les des")
        pos = tabPlayers[player].position
        fDice = throwDice()
        sDice = throwDice()
        score = fDice + sDice
        nPos = pos + score
        #turnPion(pos, nPos, player)
        if nPos > 39:
                nPos = nPos % 40
                tabPlayers[player].moveMoney(200)
        Boxes[pos]["players"].remove(player)
        Boxes[nPos]["players"].append(player)
        tabPlayers[player].movePosition(score)
        return score

# Action lorsque un joueur arrive sur une case              
def turn(tabPlayers,nbPlayers,player):
        print "\n-------------------------------------------"
        printState(tabPlayers, nbPlayers)
        pos = tabPlayers[player].position
        print "\nTour Joueur ", (player+1), " : ", tabPlayers[player].name
        
        if Boxes[pos]["type"] == 3 :
                if onJail(1) == 0 :
                        if onJail(2) == 0 :
                                onJail(3)
        else :
                score = move(tabPlayers,player)
                pos = tabPlayers[player].position
        printCase(tabPlayers,pos)
        if Boxes[pos]["type"] == 0 :
                money = Boxes[pos]["moveMoney"]
                tabPlayers[player].moveMoney(money)

        if Boxes[pos]["type"] == 1 :
                onAPropertie(tabPlayers,player)

        if Boxes[pos]["type"] == 2 :
                onAGare(tabPlayers,player)

        if Boxes[pos]["type"] == 4 :
                onDistrib(tabPlayers,player,score)
                
        if Boxes[pos]["type"] == 6 :
                communityCards(tabPlayers, nbPlayers, player)
                
        if Boxes[pos]["type"] == 7 :
                chanceCards(tabPlayers, nbPlayers, player)

        raw_input("\nAppuyez sur entree continuer...")
