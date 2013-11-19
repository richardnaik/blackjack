import deck

class BlackJack(object):
	def __init__(self, bet):
        self.bet = bet
		self.player_total = 0
		self.dealer_total = 0
		self.player_win = False
		self.dealer_win = True
	
	#the game loop
	def play(self):
		#draw the first four cards for the player and dealer
		deck = new Deck()
		self.player_total += deck.draw()
		self.dealer_total += deck.draw()
		self.player_total += deck.draw()
		self.dealer_total += deck.draw()
		
		while(self.player_win == False && self.dealer_win == False):
			if self.player_total == 21
			draw = raw_input('Draw another card? Y/N ')
			
			if draw == 'Y':
				self.player_total += deck.draw()
				self.dealer_total += deck.draw()
			elif draw == 'N':
				#dealer draws until he beats player or busts
		else:
			if self.player_win == True:
				print 'You won! Enjoy your %f dollars!' % bet
			elif self.dealer_win == True:
				print 'You lost-your sweet %f dollars are mine! HAHAHAHAHAH!' % bet
			else:
				print 'It seems the only winning move is not to play....'