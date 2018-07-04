from const.player import Player
from const.boardGame import Boxes
from function.cards import *
from function.turn import *
from function.init import *
from function.placement import *
from function.printf import *
from function.pygam import *

# Achat d'une propriete
def buyCase(tabPlayers,player):
        pos = tabPlayers[player].position
        prop = Boxes[pos]["proprietaire"]
        if prop != -1 :
                print "\nImpossible : appartient deja a " , tabPlayers[player].name
        elif tabPlayers[player].money < Boxes[pos]["price"] :
                print "\nImpossible : Vous n'avez que ", tabPlayers[player].money
        else :
                print "\nFelicitation vous venez d'acheter " + Boxes[pos]["name"]
                Boxes[pos]["proprietaire"] = player
                tabPlayers[player].money = tabPlayers[player].money - Boxes[pos]["price"]


# Echange d'argent lors d'une taxe sur une propriete
def homesTax(tabPlayers,player):
        pos = tabPlayers[player].position
        prop = Boxes[pos]["proprietaire"]
        if prop > -1 :
                homes = Boxes[pos]["homes"]
                tax = Boxes[pos]["TaxPrice"][homes]
                tabPlayers[player].moveMoney( -tax )
                tabPlayers[prop].moveMoney( tax )
                print "\n", tabPlayers[player].name, " paye une taxe de ", tax, " a ", tabPlayers[prop].name


# Echange d'argent lors d'une taxe sur une gare
def gareTax(tabPlayers,player):
        pos = tabPlayers[player].position
        prop = Boxes[pos]["proprietaire"]
        cpt = 0
        if Boxes[5]["proprietaire"] == prop :
                cpt += 1
        if Boxes[15]["proprietaire"] == prop :
                cpt += 1
        if Boxes[25]["proprietaire"] == prop :
                cpt += 1
        if Boxes[35]["proprietaire"] == prop :
                cpt += 1
        if cpt == 1 :
                print "\n", tabPlayers[player].name, " paye une taxe de ", 25, " a ", tabPlayers[prop].name 
                return 25
        elif cpt == 2 :
                print "\n", tabPlayers[player].name, " paye une taxe de ", 50, " a ", tabPlayers[prop].name
                return 50
        elif cpt == 3 :
                print "\n", tabPlayers[player].name, " paye une taxe de ", 100, " a ", tabPlayers[prop].name
                return 100
        elif cpt == 4 :
                print "\n", tabPlayers[player].name, " paye une taxe de ", 200, " a ", tabPlayers[prop].name
                return 200
        else :
                return 0


# Echange d'argent lors d'une taxe sur une compagnie de distribution
def distribTax(tabPlayers,player):
        pos = tabPlayers[player].position
        prop = Boxes[pos]["proprietaire"]
        cpt = 0
        if Boxes[12]["proprietaire"] == prop :
                cpt += 1
        if Boxes[28]["proprietaire"] == prop :
                cpt += 1
        if cpt == 1 :
                print "\n", tabPlayers[player].name, " paye une taxe de 4x son score a ", tabPlayers[prop].name
                return 4
        elif cpt == 2 :
                print "\n", tabPlayers[player].name, " paye une taxe de 10x son score a ", tabPlayers[prop].name
                return 10
        else :
                return 0

# Action lors de la pose d'une maison
def putHome(tabPlayers,player):
        pos = tabPlayers[player].position
        prop = Boxes[pos]["proprietaire"]
        if prop == player :
                if Boxes[pos]["homes"] < 5 :
                        Boxes[pos]["homes"] = Boxes[pos]["homes"] + 1
                        price = Boxes[pos]["homesPrice"]
                        tabPlayers[player].moveMoney( -price )
                        print tabPlayers[player].name, " achete une maison a ", price
                else :
                        print "Deja max de maisons"
