"""
    Dealer Class
    1. hand

    methods
    1. hit, stand, double, buy insurance 
    2. shows 2 cards
"""

from hand import Hand

class Player(Hand):
    def __init__(self, name:str, stack: int):
        super().__init__()
        self.name = name
        self.stack = stack
        self.bet = 0

    def place_bet(self, amount:int):
        if amount > self.stack:
            raise ValueError("Bet amount exceeds current stack, reduce bet size")
        self.bet = amount
        self.stack -= amount

    def win_bet(self):
        self.stack += 2*self.bet
        self.bet = 0

    def lose_bet(self):
        self.bet = 0

    def push_bet(self):
        self.stack += self.bet
        self.bet = 0

    def double_bet(self):
        self.bet *= 2
        self.stack -= self.bet

    def __str__(self):
        return f"{self.name}'s hand: {super().__str__()} | Stack: {self.stack} | Bet: {self.bet}"