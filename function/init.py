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
                        

