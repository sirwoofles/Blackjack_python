class Card:
    'common base class for Cards'

    def __init__(self, suit, face, value, is_ace):
        self.suit = suit
        self.face = face
        self.value = value
        self.is_ace = is_ace

    def getCardValue(self):
        return self.value