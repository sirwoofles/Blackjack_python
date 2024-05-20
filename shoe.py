"""
    Shoe
    1. 1 shoe comprise of a few decks
    2. methods:  deal_card,  
"""

# To add: if len of shoe is 0, cannot pop cards, must figure a logic to restart the game/ re-fill the shoe

import random
from deck import Deck

class Shoe:
    def __init__(self, number_of_decks: int):
        self.cards = []
        for i in range(number_of_decks):
            deck = Deck()
            self.cards.extend(deck.cards)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()