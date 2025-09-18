from person import Person as p 
import json
class Studenter:

    studenter = []  
     

    def lägg_stud(self,namn: str, klass: str):
        self.studenter.append(p(namn, klass))
        print(f"{namn} lades till i listan")


    def ta_bort_stud(self , namn: str):

        hittade = False
        x = 0 
        for student in self.studenter:
            if student.namn == namn:
                self.studenter.pop(x)
                print(f"{student.namn} togs bort från listan")
                hittade = True
                break
            x += 1  
        if not hittade:
            print("Hittade ingen med det namnet")
   
    def läs_in(self):
        try:
            with open("klass_lista.json", "r") as f:
                data = json.load(f)
                for item in data:
                    self.studenter.append(p(item["namn"], item["klass"], item["närvaro"], item["betyg"]))
                print("Studenter inlästa från klass_lista.json")
        except FileNotFoundError:
            print("Ingen sparad fil hittades, startar med tom lista.")
        except json.JSONDecodeError:
            print("Fel vid läsning av filen, startar med tom lista.")
        except Exception as e:
            print("Ett oväntat fel inträffade:", e)


    def spara(self):

        json_dict = []
        for student in self.studenter:
            json_dict.append(student.dict())

        #print(json_dict)

        with open("klass_lista.json", "w") as f:
            f.write(json.dumps(json_dict))
            print("Studenter sparade i klass_lista.json")     
           

    def lista_stud(self):
       for elev in self.studenter:
           print(elev.namn, elev.klass)


    def visa_stud(self, namn:str): 
        
        hittade = False
        for elev in self.studenter:
            if elev.namn == namn:
                print(elev)
                hittade = True
                break
        if not hittade:
            print("Hittade ingen med det namnet")

   
        
       


if __name__ == "__main__":
    #stud = Studenter()
    #stud.lägg_stud("Kalle", "DevOps" )
    #stud.lägg_stud("Nila", "DevOps")
    #stud.lägg_stud("Nisse", "DevOps")
    #stud.ta_bort_stud("Nila")
    #stud.visa_stud("Kalle")
          
    