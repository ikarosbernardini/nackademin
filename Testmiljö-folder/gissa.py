import random

def gissa():
    try:
        antal = 1
        goal = random.randint(1, 100)
        guess = None 
        while guess != goal:
            guess = int(input("Gissa ett slumpmässigt tal från 1-100: "))
            if guess == goal:
                    print(f"{goal} var rätt svar! du hade {antal} gissningar")
            elif guess > goal:
                    print("för högt, gissa lägre")
                    antal += 1
            elif guess < goal:
                    print("för lågt, gissa högre")
                    antal += 1 
    except Exception as e:
          print("Vänligen ange siffror") 
          gissa()

if __name__ == "__main__":
      gissa()
