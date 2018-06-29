import random
import pygame

# type :
# 0 gagne/perd de l'argent
# 1 batiment
# 2 gare
# 3 prison
# 4 compagnie distrib
# 5 rien
# 6 caisse communautaire
# 7 chance

class Player :
	def __init__(self, name):
		self.name = name
		self.position = 0
		self.money = 1500

	def movePosition(self, add):
		self.position = (self.position + add) % 40
		print "\n", self.name , " avance de " , add , "jusqu'a la case " , self.position

	def moveMoney(self, money):
		self.money += money



Cases = [
		{"pos" : 0,  "type" : 0, "players":[], "name" : "Depart", "moveMoney" : 200 },
		{"pos" : 1,  "type" : 1, "players":[], "name" : "Dolphin", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 100, "TaxPrice":[10,70,200,550,750] },
		{"pos" : 2,  "type" : 6, "players":[] },
		{"pos" : 3,  "type" : 1, "players":[], "name" : "BullDog", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 100, "TaxPrice":[10,50,150,450,550] },
		{"pos" : 4,  "type" : 0, "players":[], "name" : "Taxe 1", "moveMoney" : -200 },
		{"pos" : 5,  "type" : 2, "players":[], "name" : "", "proprietaire" : -1, "price" : 200 },
		{"pos" : 6,  "type" : 1, "players":[], "name" : "Chez Tonton", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 100, "TaxPrice":[12,60,180,500,700] },
		{"pos" : 7,  "type" : 7, "players":[] },
		{"pos" : 8,  "type" : 1, "players":[], "name" : "Shangai", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 9,  "type" : 1, "players":[], "name" : "Coup d'etat", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 10, "type" : 5, "players":[], "name" : "Teknival" },
		{"pos" : 11, "type" : 1, "players":[], "name" : "Concrete", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 12, "type" : 4, "players":[], "name" : "Compagnie de distribution d'alcool", "proprietaire" : -1, "price" : 150, "TaxPrice":[50,100] },
		{"pos" : 13, "type" : 1, "players":[], "name" : "Wanderlust", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 14, "type" : 1, "players":[], "name" : "Glazart", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 15, "type" : 2, "players":[], "name" : "", "proprietaire" : -1, "price" : 200 },	
		{"pos" : 16, "type" : 1, "players":[], "name" : "ElectroBeach", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 17, "type" : 6, "players":[] },
		{"pos" : 18, "type" : 1, "players":[], "name" : "Solidays", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 19, "type" : 1, "players":[], "name" : "Lollapalooza", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 20, "type" : 5, "players":[], "name" : "Quarantaine" },
		{"pos" : 21, "type" : 1, "players":[], "name" : "Feria de Bayonne", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 22, "type" : 7, "players":[] },
		{"pos" : 23, "type" : 1, "players":[], "name" : "Feria de Dax", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 24, "type" : 1, "players":[], "name" : "Feria de Pampelune", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 25, "type" : 2, "players":[], "name" : "", "proprietaire" : -1, "price" : 200 },
		{"pos" : 26, "type" : 1, "players":[], "name" : "Sziget", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 27, "type" : 1, "players":[], "name" : "WCD", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 28, "type" : 4, "players":[], "name" : "Compagnie de distribution des drogues", "proprietaire" : -1, "price" : 150, "TaxPrice":[50,100] },
		{"pos" : 29, "type" : 1, "players":[], "name" : "UMF Croatie", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 30, "type" : 3, "players":[], "name" : "Degrisement" },
		{"pos" : 31, "type" : 1, "players":[], "name" : "Electric Zoo", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 32, "type" : 1, "players":[], "name" : "UMF Miami", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 33, "type" : 6, "players":[] },
		{"pos" : 34, "type" : 1, "players":[], "name" : "Burning Man", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 35, "type" : 2, "players":[], "name" : "", "proprietaire" : -1, "price" : 200 },
		{"pos" : 36, "type" : 7, "players":[] },
		{"pos" : 37, "type" : 1, "players":[], "name" : "TomorrowLand", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] },
		{"pos" : 38, "type" : 0, "players":[], "name" : "Taxe 2", "moveMoney" : -300 },
		{"pos" : 39, "type" : 1, "players":[], "name" : "ESGI AfterWork", "proprietaire" : -1, "price" : 150, "homes": 0, "homesPrice": 50, "TaxPrice":[20,30,50,100] }
                ]


#Impression d'une case
def printCase(pos) :
        print "\n-------------------------------------------"
        print "Vous etes pos " , pos #rajouter les autres joueurs
        if Cases[pos]["type"] == 0 :
                print "\n" , Cases[pos]["name"]
                if Cases[pos]["moveMoney"] <100 :
                        print "\n Vous perdez " , Cases[pos]["moveMoney"]
                else :
                        print "\n Vous gagnez " , Cases[pos]["moveMoney"]

        if Cases[pos]["type"] == 1 :
                print "\n" + Cases[pos]["name"]
                haveProp(pos)
                print "\nPrix : " , Cases[pos]["price"]
                print "\nTaxe :  " , Cases[pos]["TaxPrice"][0] , " pour 1 maison"
                print "        " , Cases[pos]["TaxPrice"][1] , " pour 2 maisons"
                print "        " , Cases[pos]["TaxPrice"][2] , " pour 3 maisons"
                print "        " , Cases[pos]["TaxPrice"][3] , "pour 4 maisons"
                print "\nPrix d'une maison : " , Cases[pos]["homesPrice"]

        if Cases[pos]["type"] == 2 :
                print "\nBienvenue a " , Cases[pos]["name"]
                haveProp(pos)
                print "\nPrix : " , Cases[pos]["price"]
                print "\nTaxe :  25  pour 1"
                print "        50  pour 2"
                print "        100 pour 3"
                print "        200 pour 4"
                
        if Cases[pos]["type"] == 3 :
                print "\nBienvenue en dégrisement..."
                
        if Cases[pos]["type"] == 4 :
                print "\nBienvenue a la " , Cases[pos]["name"]
                haveProp(pos)
                print "\nPrix : " , Cases[pos]["price"]
                print "\nTaxe :  x4 pour une compagnie"
                print "        x10 pour les 2"
                
        if Cases[pos]["type"] == 5 :
                print "\nBienvenue au " , Cases[pos]["name"]
                
        if Cases[pos]["type"] == 6 :
                print "\nCAISSE COMMUNAUTE"
                
        if Cases[pos]["type"] == 7 :
                print "\nCARTE CHANCE"

# renvoi le proprietaire -1 sinon
def haveProp(pos) :
        prop = Cases[pos]["proprietaire"]
        if prop == -1 :
                print "\nPas de proprietaire"
        else :
                print "\nAppartient a " , tabPlayers[prop].name
        return prop

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
                
#initialise le tableau de joueurs
def initGame():
        i=0
        nbPlayers = inputNumber("Entrez le nombre de joueurs : ")
        for i in range(nbPlayers) :
                name = raw_input("Entrez nom : ")
                tabPlayers.append(Player(name))
                Cases[0]["players"].append(i)
        return nbPlayers



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

def throwDice():
        dice = random.randrange(1, 7, 1)
        print "Dé : " , dice
        return dice

def buyCase(player):
        pos = tabPlayers[player].position
        prop = Cases[pos]["proprietaire"]
        if prop != -1 :
                print "\nImpossible : appartient deja a " , tabPlayers[player].name
        elif tabPlayers[player].money < Cases[pos]["price"] :
                print "\nImpossible : Vous n'avez que ", tabPlayers[player].money
        else :
                print "\nFelicitation vous venez d'acheter " + Cases[pos]["name"]
                Cases[pos]["proprietaire"] = player
                tabPlayers[player].money = tabPlayers[player].money - Cases[pos]["price"]


def move(player):
        raw_input("Appuyez sur entree pour lancer les dés")
        pos = tabPlayers[player].position
        fDice = throwDice()
        sDice = throwDice()
        score = fDice + sDice
        nPos = pos + score
        if nPos > 39:
                nPos = nPos % 40
                tabPlayers[player].moveMoney(200)
        Cases[pos]["players"].remove(player)
        Cases[nPos]["players"].append(player)
        tabPlayers[player].movePosition(score)
        return score

def printState():
        for i in range(nbPlayers):
                print "Joueur " , tabPlayers[i].name , " est case ", tabPlayers[i].position , " et a ", tabPlayers[i].money, " euros"

def homesTax(player):
        pos = tabPlayers[player].position
        prop = Cases[pos]["proprietaire"]
        if prop > -1 :
                homes = Cases[pos]["homes"]
                tax = Cases[pos]["TaxPrice"][homes]
                tabPlayers[player].moveMoney( -tax )
                tabPlayers[prop].moveMoney( tax )
                print "\n", tabPlayers[player].name, " paye une taxe de ", tax, " a ", tabPlayers[prop].name

def gareTax(player):
        pos = tabPlayers[player].position
        prop = Cases[pos]["proprietaire"]
        cpt = 0
        if Cases[5]["proprietaire"] == prop :
                cpt += 1
        if Cases[15]["proprietaire"] == prop :
                cpt += 1
        if Cases[25]["proprietaire"] == prop :
                cpt += 1
        if Cases[35]["proprietaire"] == prop :
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

def distribTax(player):
        pos = tabPlayers[player].position
        prop = Cases[pos]["proprietaire"]
        cpt = 0
        if Cases[12]["proprietaire"] == prop :
                cpt += 1
        if Cases[28]["proprietaire"] == prop :
                cpt += 1
        if cpt == 1 :
                print "\n", tabPlayers[player].name, " paye une taxe de 4x son score a ", tabPlayers[prop].name
                return 4
        elif cpt == 2 :
                print "\n", tabPlayers[player].name, " paye une taxe de 10x son score a ", tabPlayers[prop].name
                return 10
        else :
                return 0

def putHome(player):
        pos = tabPlayers[player].position
        prop = Cases[pos]["proprietaire"]
        if prop == player :
                if Cases[pos]["homes"] < 5 :
                        Cases[pos]["homes"] = Cases[pos]["homes"] + 1
                        price = Cases[pos]["homesPrice"]
                        tabPlayers[player].moveMoney( -price )
                        print tabPlayers[player].name, " achete une maison a ", price
                else :
                        print "Deja max de maisons"


def onAPropertie(player):
        pos = tabPlayers[player].position
        prop = Cases[pos]["proprietaire"]
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


def onAGare(player):
        pos = tabPlayers[player].position
        prop = Cases[pos]["proprietaire"]    
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

def onDistrib(player, score):
        pos = tabPlayers[player].position
        prop = Cases[pos]["proprietaire"]    
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

def onJail():
        fDice = throwDice()
        sDice = throwDice()
        if fDice == sDice :
                print "Felicitation vous avez décuvé"
                return 1
        else :
                print "Encore saoul, essayez au prochain tour..."
                return 0


def communityCards(player):
        pos = tabPlayers[player].position
        card = random.randrange(1, 11, 1)
        if card == 1 :
                print "Allez en degrisement..."
                Cases[pos]["players"].remove(player)
                Cases[30]["players"].append(player)
                tabPlayers[player].position = 30
        elif card == 2 :
                print "Allez case départ"
                Cases[pos]["players"].remove(player)
                Cases[0]["players"].append(player)
                tabPlayers[player].position = 0
        elif card == 3 :
                print "Allez au Bulldog sans passer par la case départ"
                Cases[pos]["players"].remove(player)
                Cases[3]["players"].append(player)
                tabPlayers[player].position = 3
        elif card == 4 :
                print "Amende pour ivresse sur la voie publique..."
                tabPlayers[player].moveMoney(-400)
                print "-400 euros"
        elif card == 5 :
                print "Vous remportez le tournoi de Bière Pong !"
                tabPlayers[player].moveMoney(500)
                print "+500 euros"
        elif card == 6 :
                print "RDV au teknival !"
                Cases[pos]["players"].remove(player)
                Cases[10]["players"].append(player)
                tabPlayers[player].position = 10
        elif card == 7 :
                print "Vous titubez, reculez de 3 cases !"
                Cases[pos]["players"].remove(player)
                Cases[pos-3]["players"].append(player)
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
                Cases[pos]["players"].remove(player)
                Cases[37]["players"].append(player)
                tabPlayers[player].position = 37

                
def chanceCards(player):
        pos = tabPlayers[player].position
        card = random.randrange(1, 11, 1)
        if card == 1 :
                print "Go en degrisement"
                Cases[pos]["players"].remove(player)
                Cases[30]["players"].append(player)
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
                tabPlayers[player].moveMoney(300)
        elif card == 6 :
                print "Vous tirez une carte communauté"
                communityCards(player)
        elif card == 7 :
                print "Coin VIP au Hobo avec bouteilles..."
                print "-300 euros"
                tabPlayers[player].moveMoney(300)
        elif card == 8 :
                print "Retour case départ"
                Cases[pos]["players"].remove(player)
                Cases[0]["players"].append(player)
                tabPlayers[player].position = 0
        elif card == 9 :
                print "Vous achetez une pinte au Marvellous..."
                print "-100 euros"
                tabPlayers[player].moveMoney(100)
        elif card == 10 :
                print "Frais de doliprane et lysopaine..."
                print "-80 euros"
                tabPlayers[player].moveMoney(80)                      



               
def turn(player):
        print "\n-------------------------------------------"
        printState()
        pos = tabPlayers[player].position
        print "\nTour Joueur ", (player+1), " : ", tabPlayers[player].name
        
        if Cases[pos]["type"] == 3 :
                onJail()
        else :
                score = move(player)
                pos = tabPlayers[player].position
        printCase(pos)
        if Cases[pos]["type"] == 0 :
                money = Cases[pos]["moveMoney"]
                tabPlayers[player].moveMoney(money)

        if Cases[pos]["type"] == 1 :
                onAPropertie(player)

        if Cases[pos]["type"] == 2 :
                onAGare(player)

        if Cases[pos]["type"] == 4 :
                onDistrib(player,score)
                
        if Cases[pos]["type"] == 6 :
                communityCards(player)
                
        if Cases[pos]["type"] == 7 :
                chanceCards(player)

        raw_input("\nAppuyez sur entree continuer...")
        
                        

def Game():
        while win()== False :
                for i in range(nbPlayers):
                        turn(i)
tabPlayers = []
nbPlayers = initGame()
Game()

