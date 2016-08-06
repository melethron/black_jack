class Player(object):
	def __init__(self):
		self.money = 100
		self.hand = []
		self.bet = 0

	def __str__(self):
		return "You got %d dollars!" %self.money

	def show_hand(self):
		print "You got %s"%self.hand_sum()

	def take_card(self, deck):
		self.hand.append(deck.pop(0))

	def take_two_cards(self, deck):
		self.take_card(deck)
		self.take_card(deck)

	def answer(self):
		answer = raw_input("Do you want to take a card? y/n ")
		return answer

	def hand_sum(self):
		return sum(self.hand)

	def make_bet(self):
		try:
			self.bet = int(raw_input("What is your bet? "))
			if self.bet > self.money:
				print "You don't have enough money!"
				self.make_bet()
			self.money -= self.bet
		except ValueError:
			self.make_bet()

	def clear_hand(self):
		self.hand = []
