"""
    Dealer Class
    1. hand

    methods
    1. hit, stand, double, buy insurance 
    2. shows 2 cards
"""

from hand import Hand
from card import Card, Rank

class Dealer(Hand):
    def __init__(self):
        super().__init__()

    def show_one_card(self):
        # show only one of the dealer's card 
        return f"Dealer's hand: {self.cards[0]}, <HIDDEN CARD>"
    
    def face_up_card_is_face_card(self):
        # Check if the face-up card is a face card (10, Jack, Queen, King)
        return self.cards[0].rank in {Rank.TEN, Rank.JACK, Rank.QUEEN, Rank.KING}
    
    def hit(self, card:Card):
        self.add_card(card)

    def show_hand(self):
        return f"Dealer's hand: {super().__str__()}"

    def __str__(self):
        return f"Dealer's hand: {super().__str__()}"