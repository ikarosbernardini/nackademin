import os # importerar os bibloteket

users = "users" # gör en variabel för mappen "users" 
felaktiga_försök = 3 

def hämta_lösenord(användarnamn): # skapat en metod för att hämta lösenordet från de angivna filnamnet. 
    filväg = os.path.join("users", f"{användarnamn}.txt")
    print("Försöker läsa från fil:", os.path.join("users", f"{användarnamn}.txt"))
    if os.path.exists(filväg):
        print("Filen hittades!")
        try:
            with open(filväg, "r") as fil:
                lösenord = fil.read().strip()
                print("Läst lösenord:",repr(lösenord))
                return lösenord
        except Exception as e:
            print("Fel vid läsning:",e)
            return None
        
        
    else:
        print("Filen hittades inte.")
        return None

    
def logga_in():
     # förbestämmer antal felaktiga försök som går att göra vilket jag sätter till : 3
    global felaktiga_försök 
    while felaktiga_försök > 0: # så länge felaktiga försök är större än 0 så får användaren försöka igen
        användarnamn = input("Användarnamn:") # ber användaren skriva in sitt användarnamn
        lösenord = input("Lösenord:") # ber användaren skriva in sitt lösenord 
        registerad_användare =  hämta_lösenord(användarnamn)
        print("Lösenord i filen:", repr(registerad_användare))

        if registerad_användare and lösenord == registerad_användare: # kollar om användarnamn finns i konton och om lösenordet stämmer
            print("Välkommen", användarnamn, ":) Du har nu loggat in.") # Välkomnar användaren vid korrekt inloggingsuppgifter.
            return användarnamn # returnerar användarnamnet så vi kan använda det senare
        else:
            felaktiga_försök -= 1 # om användarnamn eller lösenord är felaktigt så minskar vi antalet försök med 1
            if felaktiga_försök == 0: # om felaktiga försök är 0 så skriver vi ut en text och avslutar programmet
                print("För många felaktiga försök. Programmet avslutas.")
                break 
                return None
            else: # annars skriver vi ut en text med antal försök kvar och loopen fortsätter
                print("Felaktigt användarnamn eller lösenord. Du har", felaktiga_försök, "försök kvar, Försök igen.")
logga_in()
        





