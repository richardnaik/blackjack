import random

class Deck(object):
	#define the deck of cards
	#for our purposes just define an Ace as always being 1 for now
	def __init__(self):
			self.cards = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':1}
	
	#get a random card from the deck, delete it drom the dict, then return it
	def draw(self):
			card_key = random.choice(self.cards.keys())
			card = self.cards[card_key];
			del self.cards[card_key]
			return card
			