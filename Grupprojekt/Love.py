import Issam as i
def meny(): #Skapar meny för användaren 
        while True: 
            print("Välkommen till din to do lista.") 
            print("1. Lägg till något i listan.")
            print("2. Visa lista på allt som ska göras.")
            print("3. Ta bort något från listan.")
            print("4. Avsluta programmet.")
            val = input("Välj ett av alternativen: ") #Ber användaren att välja mellan alternativen

            if val == "1":
                    print("test")
            elif val == "2":
                    print("test1")
            elif val == "3":
                    print("test3")
            elif val == "4":
                print("Avslutar programmet")
                exit()
            else: #Säger till om användaren inmatar något val som inte finns
                print("Valet finns inte med i listan. Försök igen")

meny()

if __name__ == "__main__":
        pass