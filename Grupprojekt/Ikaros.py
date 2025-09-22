import os

def spara(filnamn, uppgifter):  # uppgifter är en lista
    with open(filnamn, 'w') as f:
        for uppgift in uppgifter:
            f.write(uppgift + "\n")
    print("Listan har sparats.")

def ladda(filnamn):
    if not os.path.exists(filnamn):
        print(f"Filen '{filnamn}' hittades inte.")
        return []
    with open(filnamn, 'r') as f:
        return [rad.strip() for rad in f.readlines()]
    
if __name__ == "__main__":
    pass

