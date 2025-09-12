import os

if __name__ == "__main__": # fortfarnade jävligt oklart fan den denna kod gör, men den körs bara om filen körs direkt, "sägs de" 
    
    def spara_funk(filnamn, uppgift):  # sparar uppgiften i en textfil
        with open(filnamn, 'w') as f: # öppnar filen i skrivläge
         f.write(uppgift) # skriver uppgiften i filen

    def ladda_funk(filnamn): # laddar uppgiften från en textfil
        if not os.path.exists(filnamn): # kollar om filen finns
            print(f"Filen '{filnamn}' hittades inte.") # om filen inte finns, skrivs detta ut
            return None
        with open(filnamn, 'r') as f: # öppnar filen i läsläge
            return f.read() # returnerar innehållet i filen
    
    