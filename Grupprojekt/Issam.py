
def lägg_till_uppgifter(uppgifter):
    uppgift = input("Ange en uppgift att lägga till: ")
    uppgifter.append("[]" + uppgift)
    return uppgifter

def lista_uppgifter(uppgifter):
    if len(uppgifter) == 0:
        print("Inga uppgifter i listan.")
    else:
        for uppgift in uppgifter:
            print(uppgift)


def markera_klar(uppgifter, index):
    uppgifter[index] = "[X]" + uppgifter[index][4:]
    return uppgifter

def ta_bort_uppgift(uppgifter, index):
    del uppgifter[index]
    return uppgifter


def todo_app():
    uppgifter = []
    uppgifter = lägg_till_uppgifter(uppgifter)
    uppgifter = lägg_till_uppgifter(uppgifter)
    lista_uppgifter(uppgifter)

if __name__ == "__main__":
    todo_app() # kör todo_app funktionen om filen körs direkt