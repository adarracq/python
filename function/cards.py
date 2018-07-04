import random
from const.player import Player
from const.boardGame import Boxes
from function.init import *
from function.turn import *
from function.moneyExchange import *
from function.placement import *
from function.printf import *
from function.pygam import *

def communityCards(tabPlayers, nbPlayers, player):
        pos = tabPlayers[player].position
        card = random.randrange(1, 11, 1)
        if card == 1 :
                print "Allez en degrisement..."
                Boxes[pos]["players"].remove(player)
                Boxes[30]["players"].append(player)
                tabPlayers[player].position = 30
        elif card == 2 :
                print "Allez case depart"
                Boxes[pos]["players"].remove(player)
                Boxes[0]["players"].append(player)
                tabPlayers[player].position = 0
        elif card == 3 :
                print "Allez au Bulldog sans passer par la case depart"
                Boxes[pos]["players"].remove(player)
                Boxes[3]["players"].append(player)
                tabPlayers[player].position = 3
        elif card == 4 :
                print "Amende pour ivresse sur la voie publique..."
                tabPlayers[player].moveMoney(-400)
                print "-400 euros"
        elif card == 5 :
                print "Vous remportez le tournoi de Biere Pong !"
                tabPlayers[player].moveMoney(500)
                print "+500 euros"
        elif card == 6 :
                print "RDV au teknival !"
                Boxes[pos]["players"].remove(player)
                Boxes[10]["players"].append(player)
                tabPlayers[player].position = 10
        elif card == 7 :
                print "Vous titubez, reculez de 3 cases !"
                Boxes[pos]["players"].remove(player)
                Boxes[pos-3]["players"].append(player)
                tabPlayers[player].position = pos-3
        elif card == 8 :
                print "Amende pour tapage nocturne..."
                tabPlayers[player].moveMoney(-300)
                print "-300 euros"
        elif card == 9 :
                print "La banque vous verse 200 euros"
                tabPlayers[player].moveMoney(200)
                print "+200 euros"
        elif card == 10 :
                print "RDV a TomorrowLand ! <3"
                Boxes[pos]["players"].remove(player)
                Boxes[37]["players"].append(player)
                tabPlayers[player].position = 37

                
def chanceCards(tabPlayers, nbPlayers, player):
        pos = tabPlayers[player].position
        card = random.randrange(1, 11, 1)
        if card == 1 :
                print "Go en degrisement"
                Boxes[pos]["players"].remove(player)
                Boxes[30]["players"].append(player)
                tabPlayers[player].position = 30
        elif card == 2 :
                print "Vous remboursez vos dettes aux autres joueurs"
                tot = 0
                for i in range(nbPlayers) :
                        if i != player :
                                dette = random.randrange(30, 250, 10)
                                tot = tot + dette
                                tabPlayers[i].moveMoney(dette)
                                print dette, " euros a ", tabPlayers[i].name
                tabPlayers[player].moveMoney(-tot)
        elif card == 3 :
                print "Erreur de la banque en votre faveur !"
                tabPlayers[player].moveMoney(400)
                print "+400 euros"
        elif card == 4 :
                print "C'est votre tournee !"
                tot = -150 * nbPlayers
                tabPlayers[player].moveMoney(tot)
                print "-", tot , " euros"
        elif card == 5 :
                print "Frais d'hospitalisation..."
                print "-300 euros"
                tabPlayers[player].moveMoney(-300)
        elif card == 6 :
                print "Vous tirez une carte communaute"
                communityCards(tabPlayers, nbPlayers, player)
        elif card == 7 :
                print "Coin VIP au Hobo avec bouteilles..."
                print "-300 euros"
                tabPlayers[player].moveMoney(-300)
        elif card == 8 :
                print "Retour case depart"
                Boxes[pos]["players"].remove(player)
                Boxes[0]["players"].append(player)
                tabPlayers[player].position = 0
        elif card == 9 :
                print "Vous achetez une pinte au Marvellous..."
                print "-100 euros"
                tabPlayers[player].moveMoney(-100)
        elif card == 10 :
                print "Frais de doliprane et lysopaine..."
                print "-80 euros"
                tabPlayers[player].moveMoney(-80)   
