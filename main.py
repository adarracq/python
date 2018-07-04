import pygame
import time
import random
from pygame.locals import *
from const.player import Player
from const.boardGame import Boxes
from function.cards import *
from function.init import *
from function.moneyExchanges import *
from function.placement import *
from function.printf import *
from function.pygam import *
from function.turn import *


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

def communityCards(player):
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

                
def chanceCards(player):
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
                communityCards(player)
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


#-------------------------------------------------------------PRINT-----------------------------------------------------------------#



# Affiche etat de la partie 
def printState():
        for i in range(nbPlayers):
                print "Joueur " , tabPlayers[i].name , " est case ", tabPlayers[i].position , " et a ", tabPlayers[i].money, " euros"


#Impression d'une case
def printCase(pos) :
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
                haveProp(pos)
                print "\nPrix : " , Boxes[pos]["price"]
                print "\nTaxe :  " , Boxes[pos]["TaxPrice"][0] , " pour 1 maison"
                print "        " , Boxes[pos]["TaxPrice"][1] , " pour 2 maisons"
                print "        " , Boxes[pos]["TaxPrice"][2] , " pour 3 maisons"
                print "        " , Boxes[pos]["TaxPrice"][3] , "pour 4 maisons"
                print "\nPrix d'une maison : " , Boxes[pos]["homesPrice"]

        if Boxes[pos]["type"] == 2 :
                print "\nBienvenue a " , Boxes[pos]["name"]
                haveProp(pos)
                print "\nPrix : " , Boxes[pos]["price"]
                print "\nTaxe :  25  pour 1"
                print "        50  pour 2"
                print "        100 pour 3"
                print "        200 pour 4"
                
        if Boxes[pos]["type"] == 3 :
                print "\nBienvenue en degrisement..."
                
        if Boxes[pos]["type"] == 4 :
                print "\nBienvenue a la " , Boxes[pos]["name"]
                haveProp(pos)
                print "\nPrix : " , Boxes[pos]["price"]
                print "\nTaxe :  x4 pour une compagnie"
                print "        x10 pour les 2"
                
        if Boxes[pos]["type"] == 5 :
                print "\nBienvenue au " , Boxes[pos]["name"]
                
        if Boxes[pos]["type"] == 6 :
                print "\nCAISSE COMMUNAUTE"
                
        if Boxes[pos]["type"] == 7 :
                print "\nCARTE CHANCE"



#-------------------------------------------------------------INITIALISATION-----------------------------------------------------------------#



# Retour un entier entre au clavier
def inputNumber(message):
        while True:
                try:
                        userInput = int(input(message))       
                except ValueError:
                        print("Veuillez saisir un entier")
                        continue
                else:
                        return userInput 
                        break

# renvoi le proprietaire -1 sinon
def haveProp(pos) :
        prop = Boxes[pos]["proprietaire"]
        if prop == -1 :
                print "\nPas de proprietaire"
        else :
                print "\nAppartient a " , tabPlayers[prop].name
        return prop
 

# Initialise le tableau de joueurs
def initGame():
        i=0
        nbPlayers = inputNumber("Entrez le nombre de joueurs : ")
        for i in range(nbPlayers) :
                name = raw_input("Entrez nom : ")
                tabPlayers.append(Player(name))
                Boxes[0]["players"].append(i)
        return nbPlayers


# Renvoie Vrai si qqun gagne la partie
def win():
        cpt = 0
        winner = -1
        for i in range(nbPlayers) :
                if tabPlayers[i].money > 0 :
                        cpt = cpt + 1
                        winner = i
        if cpt > 1 :
                return False
        else :
                print "Victoire de " , tabPlayers[winner].name
                return True

# Boucle partie
def Game():
        while win()== False :
                for i in range(nbPlayers):
                        if tabPlayers[i].money >= 0 :
                                turn(i)
                        




#-------------------------------------------------------------GAME TURN-----------------------------------------------------------------#



#Simule un lance de de
def throwDice():
        dice = random.randrange(1, 7, 1)
        print "De : " , dice
        return dice

# Deplacement d'un joueur
def move(player):
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
def turn(player):
        print "\n-------------------------------------------"
        printState()
        pos = tabPlayers[player].position
        print "\nTour Joueur ", (player+1), " : ", tabPlayers[player].name
        
        if Boxes[pos]["type"] == 3 :
                if onJail(1) == 0 :
                        if onJail(2) == 0 :
                                if onJail(3) == 1:
                                        score = move(player)
                                        pos = tabPlayers[player].position 
                        else :
                                score = move(player)
                                pos = tabPlayers[player].position 
                else :
                        score = move(player)
                        pos = tabPlayers[player].position 
                                
        else :
                score = move(player)
                pos = tabPlayers[player].position
        printCase(pos)
        if Boxes[pos]["type"] == 0 :
                money = Boxes[pos]["moveMoney"]
                tabPlayers[player].moveMoney(money)

        if Boxes[pos]["type"] == 1 :
                onAPropertie(player)

        if Boxes[pos]["type"] == 2 :
                onAGare(player)

        if Boxes[pos]["type"] == 4 :
                onDistrib(player,score)
                
        if Boxes[pos]["type"] == 6 :
                communityCards(player)
                
        if Boxes[pos]["type"] == 7 :
                chanceCards(player)

        raw_input("\nAppuyez sur entree continuer...")



#-----------------------------------------------------------MONEY EXCHANGE--------------------------------------------------------------#



# Achat d'une propriete
def buyCase(player):
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
def homesTax(player):
        pos = tabPlayers[player].position
        prop = Boxes[pos]["proprietaire"]
        if prop > -1 :
                homes = Boxes[pos]["homes"]
                tax = Boxes[pos]["TaxPrice"][homes]
                tabPlayers[player].moveMoney( -tax )
                tabPlayers[prop].moveMoney( tax )
                print "\n", tabPlayers[player].name, " paye une taxe de ", tax, " a ", tabPlayers[prop].name


# Echange d'argent lors d'une taxe sur une gare
def gareTax(player):
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
def distribTax(player):
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
def putHome(player):
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



#-----------------------------------------------------------PLACEMENT--------------------------------------------------------------#



# Action lorsque un joueur arrive sur une propriete
def onAPropertie(player):
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
                homesTax(player)
        else :
                print "\n 1 Pour acheter"
                print " 2 Pour passer"
                choice = int(input("Votre choix : "))
                if choice == 1 :
                        buyCase(player)


# Action lorsque un joueur arrive sur une gare
def onAGare(player):
        pos = tabPlayers[player].position
        prop = Boxes[pos]["proprietaire"]    
        if prop == player :
                print "Bienvenue chez vous"
        elif prop > -1 :
                tax = gareTax(player)
                tabPlayers[player].moveMoney( -tax )
                tabPlayers[prop].moveMoney( tax )
        else :
                print "\n 1 Pour acheter"
                print " 2 Pour passer"
                choice = int(input("Votre choix : "))
                if choice == 1 :
                        buyCase(player)


# Action lorsque un joueur arrive sur une compagnie de distribution
def onDistrib(player, score):
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
                        buyCase(player)


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



#-----------------------------------------------------------PYGAME--------------------------------------------------------------#



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

#-----------------------------------------------------------INIT GAME--------------------------------------------------------------#                        

# Init partie
tabPlayers = []
tabPion = []
nbPlayers = initGame()

# Lancement partie
Game()




