from deck import Deck

class BlackJack(object):
	def __init__(self, bet):
			self.bet = bet
			self.player_total = 0
			self.dealer_total = 0
			self.player_stand = False
			self.player_win = False
			self.dealer_win = False
	
	#the game loop
	def play(self):
		#draw the first four cards for the player and dealer
		deck = Deck()
		self.player_total += deck.draw()
		self.dealer_total += deck.draw()
		self.player_total += deck.draw()
		self.dealer_total += deck.draw()
		
		while(self.player_win == False and self.dealer_win == False):
			#Print the totals on each pass
			print 'You have: %d' % self.player_total
			print 'Dealer has: %d' % self.dealer_total
			
			if self.dealer_total == 21 or self.player_total > 21 or (self.player_stand == True and self.dealer_total >= self.player_total):
				self.dealer_win == True
			elif self.dealer_total > 21 or (self.player_stand == True and self.player_total > self.dealer_total):
				print 'xxxxxx'
				self.player_win = True
			else:
				if self.player_stand == False:
					draw = raw_input('Draw another card? Y/N ')
				else:
					draw = 'N'
			
			if draw == 'Y':
				self.player_total += deck.draw()
				#print 'You have: %d' % self.player_total
			elif draw == 'N':
				self.player_stand = True
				while(self.player_total >= self.dealer_total):
					self.dealer_total += deck.draw()
					#print 'Dealer has: %d' % self.dealer_total
			else:
				print 'Error: unrecognized option. Please try again'
		else:
			if self.player_win == True:
				print 'You won! Enjoy your %s dollars!' % self.bet
			elif self.dealer_win == True:
				print 'You lost-your sweet %s dollars are mine! HAHAHAHAHAH!' % self.bet
			else:
				print 'It seems the only winning move is not to play....'