"""
    Deck
    1. 1 deck comprise of 52 cards, of each rank and suit
    2. methods:  shuffle 
"""
from .card import Card, Rank, Suit
import random

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]

    def shuffle(self):
        random.shuffle(self.cards)