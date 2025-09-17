#   Skapa en klass för personer: Person,
#   Attribut: name: str, class: str, days_present: int, grade: int,
#  Metoder:,
#  init()  # initiera alla attribut, lägg till minst "name",
# present()   # Öka days_present med 1,
# set_grade() # sätta betyg till något mellan 1-5,
# if name == "main":
# Skapa ett objekt
# Gör print-satser för att visa funktionernas retur


class Person:

    namn = ""
    klass = ""
    närvaro = 0
    betyg = 0

    def __init__(self, namn: str, klass: str, närvaro: int = 0, betyg: int = 0):
        self.namn = namn
        self.klass = klass
        self.närvaro = närvaro
        self.betyg = betyg

    def antal_närv(self):
        self.närvaro += 1

    def sätt_betyg(self, nytt_betyg: int):
        try:
            if nytt_betyg in range(1, 6):
                self.betyg = nytt_betyg
            else:
                print("Felaktig inmatning")
        except:
            ValueError

    def __str__(self):
        return f"{self.namn} \n {self.klass} \n {self.närvaro} \n {self.betyg}"

if __name__ == "__main__":
    Kalle = Person(namn=" Kalle", klass="DevOps", närvaro=40, betyg=3)
    print(Kalle)
    Kalle.antal_närv()
    print(Kalle.närvaro)
