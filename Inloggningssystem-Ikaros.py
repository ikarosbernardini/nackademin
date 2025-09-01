konton = {"Ikaros" : "Telia123"} # här skapar jag en dictonary för förbestämt användarnamn och lösenord. 

def inloggnings_system(konton) : # skapar en funktion som ska emot två parametrar, korrekt användarnamn och korrekt lösenord
    felaktiga_försök = 3 # förbestämmer antal felaktiga försök som går att göra vilket jag sätter till : 3
    while felaktiga_försök > 0: # så länge felaktiga försök är större än 0 så får användaren försöka igen
        användarnamn = input("Användarnamn:") # ber användaren skriva in sitt användarnamn
        lösenord = input("Lösenord: ") # ber användaren skriva in sitt lösenord
        if användarnamn in konton and konton[användarnamn] == lösenord : # kollar om användarnamn finns i konton och om lösenordet stämmer
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
def skapa_konto(): # funktion för att skapa nytt konto
    nytt_användarnamn = input("Ange ett nytt användarnamn: ") # skapar en ny variabel med användarens input för att skapa ett nytt konto och lagra uppgifterna.
    nytt_lösenord = input("Ange ett nytt lösenord: ") # samma som ovan fast enbart med lösenord istället.
    konton[nytt_användarnamn] = nytt_lösenord
    print("Konto skapat för användare:", nytt_användarnamn)
def byt_lösenord(konton, användarnamn): # funktion för att byta lösenord
    nuvarande_lösenord = input("Ange ditt nuvarande lösenord: ")
    if konton[användarnamn] == nuvarande_lösenord:
        nytt_lösenord = input("Ange ditt nya lösenord: ")
        konton[användarnamn] = nytt_lösenord
        print("Lösenordet har ändrats.")
        print(f"Ditt nya lösenord är : {nytt_lösenord} ")
    else:
        print("Felaktigt nuvarande lösenord. Lösenordet har inte ändrats.")
#def byt_användare(konton, användarnamn): 


def meny_efter_inloggning(användarnamn): # meny efter inloggning
    while True:
        print(f"\nInloggad som {användarnamn}")
        print("1. Skapa nytt konto") # meny val för att skapa nytt konto, byta lösenord 
        print("2. Byt lösenord")   # meny val för att skapa nytt konto, byta lösenord 
        print("3. Byt användare") # meny val för att byt användare. 
        print("4. Logga ut") #  meny val för logga ut och få möjligheten att logga in igen.
        print("5. Avsluta programmet") # meny val för att stänga ner programmet helt. 
        val = input("Välj ett alternativ: ")
        if val == "1":
            print("Skapar nytt konto...")
            skapa_konto() # anropar funktionen för att skapa nytt konto
        elif val == "2":
            byt_lösenord(konton, användarnamn)         # anropar funktionen för att byta lösenord
        elif val == "3":
            byt_användare(konton, användarnamn)        # anropar funktionen för att byta användare
        elif val == "4":
            print("Du har nu loggat ut ifrån ditt konto och behöver logga in igen för att fortsätta.")
            inloggnings_system(konton)
            
          
        elif val == "5":
            print("Programmet avslutas.")
            break # avslutar programmet
        else:
            print("Ogiltigt val.")
användare = inloggnings_system(konton) # kallar på funktionen som vi skapade ovan.
if användare: # om användare inte är None (dvs inloggningen lyckades) så kallar vi på menyn efter inloggning
    meny_efter_inloggning(användare) # kallar på menyn efter inloggning





# Att göra : 
# Lägg till fler användare med olika användarnamn och lösenord.
# Lägg till en funktion som låter användaren byta lösenord när den är inloggad.
# Lägg till en funktion som låter användaren skapa ett nytt konto med användarnamn och lösenord.
# Ge användaren olika meny val efter inloggning, t.ex. "1. Byt lösenord", "2. Skapa nytt konto", "3. Logga ut".
# Håller på att finslipa menyerna och så man kan skapa flera konton och byta lösenord samt byta användare när man är inloggad.  
