from enum import Enum, StrEnum
 
class Suit(Enum):
    SPADE = 1
    HEART = 2
    DIAMOND = 3
    CLUB = 4

class Card:
    def __init__(self, suit, order):
        self._suit = suit
        self._order = order
        self._hidden = False

    @property
    def suit(self):
        return self._suit

    @property
    def order(self):
        return self._order

    def reveal(self):
        self._hidden = False

    def hide(self):
        self._hidden = True



if __name__ == "main":
    Suit = StrEnum('Suit', [('SPADE', '♠'), ('HEART', '♥'), ('DIAMOND', '♦'), ('CLUB', '♣')])

    print(Suit.SPADE)
    print(Suit.SPADE == Suit.HEART)

