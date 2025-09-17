from person import Person as p 

class Studenter:

    studenter = [] 

    def lägg_stud(self,namn: str, klass: str):
        self.studenter.append(p(namn, klass))


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
   
        
           

    def lista_stud(self):
       for elev in self.studenter:
           print(elev.namn, elev.klass)


    def visa_stud(self): 
        pass


if __name__ == "__main__":
    studlista = Studenter()
    studlista.lägg_stud("Kalle", "DevOps" )

    studlista.lista_stud()