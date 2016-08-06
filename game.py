import sys
from dealer import Dealer
from player import Player
from random import shuffle


def create_deck():
	deck = []
	deck.append(10)
	deck *= 4
	for i in range(2, 10):
		deck.append(i)
	deck.append(11)
	deck *= 16
	shuffle(deck)
	return deck

def setup():
	deck = create_deck()
	player = Player()
	dealer = Dealer()
	return deck, player, dealer

def game(deck, player, dealer):
	print "-"*20
	print player
	player.make_bet()
	dealer.take_two_cards(deck)
	player.take_two_cards(deck)
	dealer.show_first_card()
	player.show_hand()

	answer = player.answer()
	while answer == 'y':
		player.take_card(deck)
		if sum(player.hand) > 21:
			print "You got %s. That is too much!"%sum(player.hand)
			win = False
			break
		player.show_hand()
		answer = player.answer()

	if sum(player.hand) < 22:
		dealer.show_hand()
		while sum(dealer.hand) < 17:
			dealer.take_card(deck)
			dealer.show_hand()
			if sum(dealer.hand) > 21:
				#dealer.show_hand()
				print "Dealer loose"
				win = True
				break

	try:
		if win:
			player.money += player.bet*2
	except NameError:
		if sum(player.hand) > sum(dealer.hand):
			player.money += player.bet*2
			print "Congratulations! You won!"
		elif sum(player.hand) == sum(dealer.hand):
			player.money += player.bet
		else:
			print "Sorry, you lost."

	player.hand = []
	dealer.hand = []
	if len(deck) < 10:
		deck = create_deck()
	print player
	if player.money < 1:
		print "You lost all of your money."
		print "Goodbye!"
		sys.exit()
	play_answer = raw_input("Another round? y/n ")
def main():
	play_answer = raw_input("Do you want to play BlackJack? y/n ")
	deck, player, dealer = setup()
	while play_answer == 'y':
		game(deck, player, dealer)
	else:
		sys.exit()

if __name__ == "__main__":
	main()


















