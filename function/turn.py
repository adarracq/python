
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
                                onJail(3)
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
