from enum import Enum

class Suit(Enum):
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    CLUBS = 'Clubs'
    SPADES = 'Spades'

class Rank(Enum):
    TWO = ('2', 2)
    THREE = ('3', 3)
    FOUR = ('4', 4)
    FIVE = ('5', 5)
    SIX = ('6', 6)
    SEVEN = ('7', 7)
    EIGHT = ('8', 8)
    NINE = ('9', 9)
    TEN = ('10', 10)
    JACK = ('J', 10)
    QUEEN = ('Q', 10)
    KING = ('K', 10)
    ACE = ('A', 11)

    def __init__(self, face, value):
        self._face = face
        self._value = value

    @property
    def face(self):
        return self._face

    @property
    def value(self):
        return self._value

class Card:
    'common base class for Cards'

    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank

    def getCardValue(self):
        return self.rank.value

    def is_Ace(self):
        return self.rank == Rank.ACE

    def __str__(self):
        return f"{self.rank.face} of {self.suit.value}"