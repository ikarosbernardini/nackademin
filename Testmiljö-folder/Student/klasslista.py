from studenter import Studenter 
import json 
import os
s = Studenter()
s.läs_in()

def meny():
        print("1. Lägg till Elev") 
        print("2. Ta bort Elev")
        print("3. Lista Elev")
        print("4. Ta närvaro")
        print("5. Sätt betyg på Elev")
        print("6. Sök på Elev")
        print("7. Spara och avsluta")

def klasslista(): 

   
    while True: 
        meny()
     

        val = input("Välj ett alternativ: ") 
        if val == "1":  
           namn = input("Vad heter elev:\n")
           klass = input("Vilken klass går elev i:\n")
           s.lägg_stud(namn, klass)
           print(f"{namn} lades till i listan")
           
        

           
        elif val == "2":
            namn = input("Välj elev:\n")
            s.ta_bort_stud(namn)
            print(f"{namn} togs bort från listan")
            
        
        elif val == "3":  
            s.lista_stud()
            
            
        elif val == "4": 
            namn = input("Vad heter elev:\n")
            x = 0 
            for student in s.studenter:
                if student.namn == namn:
                   
                    student.antal_närv()
                    print(f"{student.namn} är närvarande. Antal närvaro är nu {student.närvaro}")
                    x += 1
                    break
        elif val == "5":
            namn = input("Vad heter elev:\n")
            x = 0 
            for student in s.studenter:
                if student.namn == namn:
                    nytt_betyg = int(input("Ange betyg mellan 1-5:\n"))
                    student.sätt_betyg(nytt_betyg)
                    print(f"{student.namn} har nu betyget {student.betyg}")
                    x += 1
                    break

            
            
        elif val == "6":
            namn = input (">")
            s.visa_stud(namn)
        elif val == "7":
            s.spara()
            break    

        else: 
            print("Ogiltigt val, försök igen")
        
        

klasslista()          
                