"""
    Dealer Class
    1. hand

    methods
    1. hit, stand, double, buy insurance 
    2. shows 2 cards
"""

from hand import Hand
#from card import Card

class Dealer(Hand):
    def __init__(self):
        super().__init__()

    def show_one_card(self):
        # show only one of the dealer's card 
        return str(self.cards[0] + ', <HIDDEN CARD')

    def __str__(self):
        return f"{self.name}'s hand: {super().__str__()} | Stack: {self.stack} | Bet: {self.bet}"