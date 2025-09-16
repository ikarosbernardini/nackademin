
import random
# Objekt - Objektet
# Klass - Ritning
# Instans - Kopior/varianter av objektet
# self. - talar om att var/funk tillhör ett objekt
class Dice:
    """
    Det här är en klass som skapar en tärning
    """
    
    material = "plastic" 
    shape = "cube"
    color = "black and white"
    numbers = [1, 2, 3, 4, 5, 6]
    weight = 5 # grams
    sides = 6
    def __init__(self, sides: int=6):
        self.sides = sides
    def __str__(self):
        return str(self.roll())

    def roll(self) -> int:
        return random.randint(1, self.sides)
    def spin(self):
        pass
