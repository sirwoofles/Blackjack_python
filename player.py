"""
    Player Class
    1. stack
    2. hand

    methods
    1. hit, stand, double, buy insurance 
    2. shows 2 cards

"""

from hand import Hand
from card import Card

class Player(Hand):
    def __init__(self, name:str, stack: int):
        super().__init__()
        self.name = name
        self.stack = stack
        self.bet = 0
        self.has_insurance = 0

    def place_bet(self, amount:int):
        if amount > self.stack:
            raise ValueError("Bet amount exceeds current stack, reduce bet size")
        self.bet = amount
        self.stack -= amount

    def blackjack_win(self):
        self.stack += 2.5*self.bet
        self.bet = 0
        
    def win_bet(self):
        self.stack += 2*self.bet
        self.bet = 0

    def lose_bet(self):
        self.bet = 0

    def push_bet(self):
        self.stack += self.bet
        self.bet = 0

    def double_bet(self):
        if self.bet > self.stack:
            raise ValueError("Not enough stack to double bet")
        self.stack -= self.bet
        self.bet *= 2

    # Yet to implemenet insurance feature
    """
    def buy_insurance(self):
        insurance_cost = 0.5 * self.bet
        if insurance_cost > self.stack:
            raise ValueError("Not enough stack to buy insurance")
        self.stack -= insurance_cost
        self.has_insurance = 1

    def lose_insurance(self):
        self.has_insurance = 0
    
    def win_insurance(self):
        self.push_bet(self)
        self.has_insurance = 0
    """
    
    def hit(self, card:Card):
        self.add_card(card)

    def stand(self):
        pass

    def show_hand(self):
        return f"{self.name}'s hand: {super().__str__()}"

    def __str__(self):
        return f"{self.name}'s hand: {super().__str__()} | Stack: {self.stack} | Bet: {self.bet}"