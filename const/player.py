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