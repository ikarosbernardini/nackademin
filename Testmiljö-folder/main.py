# addera(tal1, tal2)

def addera(tal1, tal2):
    return tal1 + tal2 


def subtrahera(tal1, tal2):
    return tal1 - tal2


def dividera(tal1, tal2):
    if tal2 == 0:
        return "Kan ej dividera med 0"
    return tal2 / tal2
    


def multiplicera(tal1, tal2):
    return tal1 * tal2




def matte(tal1, tal2):
    
    print("Addera: ",str,addera(tal1, tal2))
    print("Subtrahera: ",str,subtrahera(tal1, tal2))
    print("Dividera: ", str,dividera(tal1, tal2))
    print("Multiplicera: ", str,multiplicera(tal1, tal1))

if __name__ == "__main__":
    matte(30, 39)