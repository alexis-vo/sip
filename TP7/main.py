from enum import Enum, StrEnum
import random 

# class Suit(Enum):
#     SPADE = 1
#     HEART = 2
#     DIAMOND = 3
#     CLUB = 4

Suit = StrEnum('Suit', [('SPADE', '♠'), ('HEART', '♥'), ('DIAMOND', '♦'), ('CLUB', '♣')])

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

    def __str__(self):
        if self._hidden == True: # alternative : if self._hidden
            return "[██]"
        # elif self._suit == 
        if self._order == 1:
            return "[A" + self._suit + "]"
        if self._order <= 10:
            return "[" + str(self._order) + self._suit + "]"
        return "[" + ["J", "Q", "K"][self._order - 11] + self._suit + "]"

    def __eq__(self, other):
        return self._suit == other._suit and self._order == other._order

class Deck:
    def __init__(self):
        self._cards = []
        for suit in Suit:
            for value in range(7, 14):
                self._cards.append(Card(suit,value))
            self._cards.append(Card(suit, 1))
        random.shuffle(self._cards)

    def __str__(self):
        res = ""
        for card in self._cards:
            res += str(card)
        return res
        # alternative pro: "".join([str(c) for c in self._cards])

    def pop(self):
        if len(self._cards) == 0: return None
        return self._cards.pop()

class Stack:
    def __init__(self, deck):
        self._cards = []
        for i in range(4):
            self._cards.append(deck.pop())
            if i < 3:
                self._cards[-1].hide()

    def __str__(self):
        return "".join([str(c) for c in self._cards])

    def __len__(self):
        return len(self._cards)

    def pop(self):
        if len(self._cards) == 0: return None
        card = self._cards.pop()
        if len(self) > 0:
            self._cards[-1].reveal()
        return card

    def top(self): # erreur dans l'énoncé on ne nous dit pas de créer top()
        if len(self._cards) == 0:
            return None
        return self._cards[-1]

class Game:
    def __init__(self):
        self._stacks = []
        deck = Deck()
        for n in range(8):
            self._stacks.append(Stack(deck))

    def __str__(self):
        res = ""
        for i in range (len(self._stacks)):
            res += f"{i}: {self._stacks[i]}\n"
        return res
    
    def is_clearable(self, i, j):
        if len(self._stacks[i]) == 0 or len(self._stacks[j]) == 0: return False
        return (self._stacks[i].top().order) == (self._stacks[j].top().order)

    def clear(self, i, j):
        if self.is_clearable(i, j):
            self._stacks[i].pop()
            self._stacks[j].pop()
            return True
        return False

    def is_over(self):
        for i in range (8):
            for j in range (i+1, 8):
                if self.is_clearable(i,j):
                    return False
        return True

    def is_cleared(self):
        for s in self._stacks:
            if len(s) != 0:
                return False
        return True 
        # return sum([len(s) for s in self._stacks]) == 0

# if __name__ == "main":
#     print(Suit.SPADE)
#     print(Suit.SPADE == Suit.HEART)

def main():
    g = Game()
    while not g.is_over():
        print(g)
        try:
            i, j = map(int, input().split())
            if 0 <= i < 8 and  0 <= j < 8:
                if not g.clear(i, j):
                    print(f"Cannot removed cards from stacks {i} and {j}")
            else:
                print("Invalid stack number")
        except ValueError:
            print("Input two indexes")
    print(g)
    if g.is_cleared():
        print("You win!")
    else:
        print("You lose!")

main()