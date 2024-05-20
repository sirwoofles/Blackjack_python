"""
    Shoe
    1. 1 shoe comprise of a few decks
    2. methods:  deal_card,  
"""
import random
from .deck import Deck

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
        if len(self) == 0:
            print("shoe is empty, reset shoe...")
            return 
        return self.cards.pop()