from player import Player


class Dealer(Player):
	def __init__(self):
		self.hand = []

	def show_first_card(self):
		print "Dealer shows %d"%self.hand[0]

	def show_hand(self):
		print "Dealer shows %s"%sum(self.hand)
