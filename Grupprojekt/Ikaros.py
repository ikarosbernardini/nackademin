import os

if __name__ == "__main__": # fortfarnade jävligt oklart fan den denna kod gör, men den körs bara om filen körs direkt, "sägs de" 
    
    def spara_funk(filnamn, uppgift):  # sparar uppgiften i en textfil
        with open(filnamn, 'w') as f: # öppnar filen i skrivläge
         f.write(uppgift) # skriver uppgiften i filen

    def läs_funk(filnamn): # läser uppgiften från en textfil
       with open(filnamn, 'r') as f: # öppnar filen i läsläge
            return f.read() # returnerar innehållet i filen
    
    def ta_bort_funk(filnamn): # tar bort en uppgift genom att radera filen
        if os.path.exists(filnamn): # kollar om filen finns
            os.remove(filnamn) # tar bort filen
            print(f"Uppgiften '{filnamn}' har nu tagits bort.") # bekräftar att filen har tagits bort
        else: # om filen inte finns, skrivs detta ut
            print(f"Uppgiften '{filnamn}' hittades inte.") # bekräftar att filen inte hittades
    