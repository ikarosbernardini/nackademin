korrekt_användarnamn = ("Ikaros") # korrect inloggnings användarnamn  
korrekt_lösenord = ("Telia123") # korrect inloggnings lösenord

def login_system(korrekt_användarnamn, korrekt_lösenord): # skapar en funktion för ett inloggningssystem
    felaktiga_försök = 3 # förbestämmer antal felaktiga försök som går att göra
    while felaktiga_försök > 0: # så länge felaktiga försök är större än 0
        användarnamn = input("Användarnamn:") # ber användaren skriva in sitt användarnamn
        lösenord = input("Lösenord: ") # ber användaren skriva in sitt lösenord
        if användarnamn == korrekt_användarnamn and lösenord == korrekt_lösenord: # om användarnamn och lösenord är korrekt så skriver vi ut en text och hoppar ur loopen.
            print("Välkommen", användarnamn, ":) Du har nu loggat in.") # Välkomnar användaren
            break
        else:
            felaktiga_försök -= 1 # om användarnamn eller lösenord är felaktigt så minskar vi antalet försök med 1
            if felaktiga_försök == 0: # om felaktiga försök är 0 så skriver vi ut en text och avslutar programmet
                print("För många felaktiga försök. Ditt program avslutas.")
            else: # annars skriver vi ut en text med antal försök kvar och loopen fortsätter
                print("Du har", felaktiga_försök, "försök kvar. Försök igen.") 
login_system(korrekt_användarnamn, korrekt_lösenord) # kallar på funktionen