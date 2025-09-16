from card import Card
import random 

class Deck:
    
    def __init__(self):
        self.hands = []
        for color in ["H", "R", "S", "K"]:
            for value in range(1, 14):
                self.hands.append(Card(color, value))
    def __str__(self):
        return f"{self.hands}" 
deck = Deck()
cards = deck.hands
print(deck.hands[0])
random.shuffle(cards)
print(deck.hands[0])
