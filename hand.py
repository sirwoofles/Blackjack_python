"""
    Hand Class
    1. at least 2 cards
    
    Methods
    1. Draw card
    2. get value
        a. if ace?
    3. Show Hand
    4. Clear Hand
    5. Print hand value
"""

# hand.py

from card import Card

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def clear_hand(self):
        self.cards.clear()

    def show_hand(self):
        return ', '.join(map(str, self.cards))

    def get_hand_value(self):
        hand_value = 0
        number_of_aces = 0

        for card in self.cards:
            hand_value += card.getCardValue()
            if card.is_Ace():
                number_of_aces += 1
        
        while hand_value > 21 and number_of_aces > 0:
            hand_value -= 10
            number_of_aces -= 1

        return hand_value
    
    def __str__(self):
        return ', '.join(map(str, self.cards)) + f" (Value: {self.get_hand_value()})"
