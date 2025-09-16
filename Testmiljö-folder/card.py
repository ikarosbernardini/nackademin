# Skapa en klass för ett spelkort
# Minsta antal attribut är color och value
# __init__ skall lägga värdena i 'color' & 'value'
#
import random

class Card:
    """
    Färger: Hjärter = H , Rutter = R, Spader = S, Klöver = K
    Värden:
    """

    color = ""
    value = 0
    face = color + str(value)

    def __init__(self, color: str, value: int = 13):
        if value <= 13 and value >= 1:
            self.value = value

        if value in range(1, 14) and ["H", "R", "S", "K"]:
            self.value = value
            self.color = color 
        else: 
            self.value = 0
            self.color = "U" 

        if self.color == 1: 
            self.color = "H"
        elif self.color == 2:
            self.color = "R"
        elif self.color == 3:
            self.color = "S"
        elif self.color == 4:
            self.color = "K"

        self.face = self.color + str(self.value)

    def __str__(self):
        return f"{self.color}{self.value}"

        
    # skall lägga variablenera i self-variablerna
    # kolla att value är mellan 1-13
    # kolla att color är "H", "R", "S", "K",
    # Om inte så print att det blev fel.
