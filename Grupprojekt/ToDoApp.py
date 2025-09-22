import os
import Ikaros as funk # importerar Ikaros.py filen som "funk" för att kunna använda metoderna jag skapade.
import Love as meny # importerar Love.py filen som "meny" för att kunna använda metoderna Love skapade. 
import Issam as todo # importerar Issam.py filen som "todo" för att kunna använda metoderna Issam skapade.

def meny(): #Skapar meny för användaren 
        while True: 
            print("Välkommen till din to do lista.") 
            print("1. Lägg till något i listan.")
            print("2. Visa lista på allt som ska göras.")
            print("3. Ta bort något från listan.")
            print("4. Spara listan")
            print("5. Ladda upp listan")
            print("6. Avsluta programmet.")
            val = input("Välj ett av alternativen: ") #Ber användaren att välja mellan alternativen

            if val == "1":
                    todo.lägg_till_uppgifter
            elif val == "2":
                    todo.lista_uppgifter
            elif val == "3":
                    todo.ta_bort_uppgift
            elif val == "4":
                    funk.spara
            elif val == "5":
                    funk.ladda
            elif val == "6":
                print("Avslutar programmet")
                exit()
            else: #Säger till om användaren inmatar något val som inte finns
                print("Valet finns inte med i listan. Försök igen")

meny()

if __name__ == "__main__": 
    pass 