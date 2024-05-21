"""
    Hand Class
    1. at least 2 cards
    
    Methods
    1. Draw card
    2. get value
        a. if ace?
    3. clear Hand
    4. print hand value
"""

from card import Card

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, c):
        self.cards.append(c)

    def clear_hand(self):
        self.cards.clear()

    def get_hand_value(self):
        hand_value = 0
        number_of_aces = 0
        has_ace = False

        for c in self.cards:
            hand_value += c.getCardValue()
            if c.is_Ace == True:
                number_of_aces += 1
                has_ace = True
        
        while hand_value > 21 and number_of_aces >0:
            hand_value -= 10
            number_of_aces -= 1

        return hand_value
    
    def __str__(self):
        return ', '.join(map(str, self.cards)) + f" (Value: {self.get_hand_value()})"
