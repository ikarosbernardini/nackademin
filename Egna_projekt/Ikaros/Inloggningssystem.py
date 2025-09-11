# Detta är ett inloggningsskript som har för tillfället 3 riktiga funktioner. 
# Hittils kan vi : 
# Logga in och få 3 chanser på att lyckas innan programmet kastar ut användaren. 
# få upp en meny med 4 olika val efter lyckad inloggning.
# 1. Skapa en ny användaren i form av att skapa en ny .txt fil som läses in och sparas lokalt på den maskin du kör altenrativt repot vid pushning till git.
# 2. Byta lösenord på befintlig användare genom att ändra existerade fils innehåll.
# 3. Logga ut ifrån inloggningsmenyn för att ge chansen till att logga in som en annan användare.
# 4. Avsluta programmet helt och hållet. 

# Mer funktioner kommer :
# Kunna ta bort användare 
# inloggnings-log
# evenutellt någon form av prompt / gui 
# läsa in uppgifter från mer än bara .txt filen och på mer optimerade sätt. 

# Kvar att göra :
# Kommentera resterande kod.
# Skapa diagram flöde med pseudokod.



import os # importerar os bibloteket

users = "users" # gör en variabel som anger mappen där användarfilerna finns. 
felaktiga_försök = 3 # skapar en global variabel med värdet : 3 för att definera hur många försök användaren blir tilldelad.

def hämta_lösenord(användarnamn): # skapat en metod för att hämta lösenordet från de angivna filnamnet. 
    filväg = os.path.join("users", f"{användarnamn}.txt") # skapar en variabel som läser igenom mapen "users" och letar efter användarnamnet användaren matar in .txt
    print("Försöker läsa från fil:", os.path.join("users", f"{användarnamn}.txt")) # förnuvarnde debugging
    if os.path.exists(filväg): # om filen hittas så läser den in lösenordet och retunerar det.
        print("Filen hittades!")   # bekräftar för mig att filen har hittats vid debugging
        try:  # användar en try - execpt metod för debugging återigen (hade mycket problem med skriptet från början att hitta filen)
            with open(filväg, "r") as fil: 
                lösenord = fil.read().strip()
                print("Läst lösenord:",repr(lösenord))
                return lösenord
        except Exception as e:
            print("Fel vid läsning:",e)
            return None
        
    else: # om filen inte hittas retunerar den "None"
        print("Filen hittades inte.")
        return None
    
def logga_in(): # skapar en inloggings metod som låter användaren ha 3 försök vid inlogg
     # förbestämmer antal felaktiga försök som går att göra vilket jag sätter till : 3
    global felaktiga_försök # kallar på den globala varibalen
    while felaktiga_försök > 0: # så länge felaktiga försök är större än 0 så får användaren försöka igen
        användarnamn = input("Användarnamn:") # ber användaren skriva in sitt användarnamn
        lösenord = input("Lösenord:") # ber användaren skriva in sitt lösenord 
        registerad_användare =  hämta_lösenord(användarnamn) # hämtar lösenordet från "hämta_lösneord() metoden för att jämföra med avnävndarens input
        print("Lösenord i filen:", repr(registerad_användare)) # ignorera denna (användar för debuggning)

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

def skapa_konto(): # skapat en metod för skapa nya användare genom att skapa nya .txt filer med lösenord som innehåll
    nytt_användarnamn = input("Ange ett nytt användarnamn: ") # ber om de nya användarnamnet
    nytt_lösenord = input("Ange ett nytt lösenord: ") # ber om de nya lösenordet.
    filväg = os.path.join("users", f"{nytt_användarnamn}.txt") # här skapar vi en sökväg till där användarens lösenord ska sparas
    # filen får användarens inmatning som namn + .txt efter. 
    # filens innehåll blir de som inmatas i "nytt_lösenord"


    if os.path.exists(filväg): # här stämmer vi av om användaren redan finns eller ej
        print("Användarnamnet finns redan.")
    else: # om inte användaren redan finns så kör vi vidare och skapar en ny fil med den nya  användaren
        with open(filväg, "w") as fil: # användar mig utav open with för att öppna en ny fil i skrivläge som sparas lokalt
            fil.write(nytt_lösenord) # matar in värdet av "nytt_lösenord" i text in i filen vi nu skapar med de nya användarnamnet.
        print("Konto har skapats för användare:", nytt_användarnamn) # bekärftar de nyligen skapade kontot.
def byt_lösenord(användarnamn): # skapat en metod som ändrade lösenord
    filväg = os.path.join("users", f"{användarnamn}.txt") # gör samma sak som innan, letar efter filen om den finns i users mappen.
    if not os.path.exists(filväg): # om inte filen hittas be användaren försöka igen.
        print("Användaren hittades inte, Vänligen försök igen.")
        return
    nuvarande_lösenord = input("Ange ditt nuvarande lösenord:") # bekräftar att användaren kan sitt nuvarande lösenord.
    with open(filväg, "r") as fil: # öpnar filvägen i .txt filen och läser igenom den för korrekt lösenord.
        sparat_lösenord = fil.read().strip()
    if sparat_lösenord == nuvarande_lösenord:
        nytt_lösenord = input("Ange ditt nya lösenord:")
        with open(filväg, "w") as fil:
            fil.write(nytt_lösenord) # overwritar det nya lösenordet och byter ut de mot de gamla. 
            print("Lösenordet har ändrats.") # bekräftar ändrat lösenord. 
    else:
        print("Felaktigt lösenord, lösenordet har inte ändrats.")
def byt_användare():
    print("Du har nu loggat ut,vänligen logga in igen med vald användare.")
    return logga_in()

def meny_efter_inloggning(användarnamn):
    while True:
        print(f"\nInloggad som {användarnamn}")
        print("1. Skapa nytt konto")
        print("2. Byt lösenord")
        print("3. Byt användare")
        print("4. Avsluta programmet")
        val = input("Välj ett alternativ: ")

        if val == "1":  # skapar ett nytt konto i form av ett .txt fil med användarens namn som "namn"
            skapa_konto()
        elif val == "2":
            byt_lösenord(användarnamn)
        elif val == "3": # låter användaren byta inloggad användare. 
            användarnamn = byt_användare()
            if användarnamn:
                continue
            else:
                break
        elif val == "4":  # stänger ner programmet och konfirmerar användarens avslut.
            print("\nProgrammet avslutas.")
            exit()
        else: # hanterar alla andra felaktiga inmatningar. 
            print("Ogiltigt val, försök igen")

användare = logga_in()
if användare:
    meny_efter_inloggning(användare)
