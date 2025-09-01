
# import time

# def run():
  #  rain = input("Regnar det? ")
  #  if rain.lower() == "nej":
 #       print("Gå ut")
#    elif rain.lower() == "ja":
#        paraply = input("Har du ett paraply? ")
#        if paraply.lower() == "ja":
#            print("Gå ut")
#        elif paraply.lower() == "nej":
  #          print("Stanna inne och vänta lite")
  #          time.sleep(5)
  #          run()
 # if __name__ == "__main__":
   # run()

#   name = input("Vad heter du? ")
#   age = int(input("Hur gammal är du? ")) 

#   if name == "Ikaros":
#   print("Hej " + name + "!")
#   else:
#       print("Hej okänd person")
#   if age < 12:
#       print("Du har inte Ikaros!")

     #      from time import sleep
     #     def show_some_looping():
     #          the_number = 10
     #          for i in range(10,0):
     #              print(f"not yet...{i}")
     #           the_number -= 1
     #          print("Happy New Year!")
     #      
     #      show_some_looping()

#   for i in range (1, 11):
#       print(i)

#   samladebetyg: int = 0

    # Ikaros
#   def betyg(ip, gp):
#       indivduell_poäng = ip
#       gruppoäng = gp
#       samladebetyg = indivduell_poäng + gruppoäng
#       return samladebetyg

    # Ikaros
#   elever = ["Ikaros", "Lowe"]

#   for elev in elever:
  #     print(f"{elev} har totalt {betyg(34, 23)} poäng")


  #     def hello(namn):
   #        input("Vad heter du? ")
    #       return

     #  hälsningsfras = hello("Ikaros")
     #  print(hälsningsfras)

     #   import random
     #   for i in range(100):  # Perform 100 coin flips.
    #    if random.randint(0, 1) == 0:
    #        print('H', end=' ')
     #   else:
    #        print('T', end=' ')
    #    print()  # Print one newline at the end.

#    animals: list = ["cat", "mouse", "cow", "dog", "horse"]
##   for animal in animals:
   #     print(f"{animal} at index {animals.index(animal)}")
#

   #   """"  animals = ["cat", "dog", "horse", "cat", "horse"]
   #     new_animals = ""
   #     for animal in animals:
    #        new_animals = new_animals, animal
   #         print(new_animals) """"

#    """"animals = ["cat", "dog", "horse", "cat", "horse"]
   # animals.append("mouse")
#   animals.remove("cat")
  #  print("cat" in animals)
  #  print("house" in animals)

    #    print("cat" not in animals)
     #   print() """""""""""


    #    animals = ["cat", "dog", "horse", ["dahlia", "daisy"]]

    #    animals.append("mouse")
    #    animals.remove("dog")
     #   animals.insert(1, "spider")
     #   animals[1] = "teddybear"

# animals[3]

# print(animals[3][0])

    #    dagar = ["Mån","Tis","Ons","Tors","Fre"]
     #   dagar.sort()
     #   print(dagar)

    #schema = [1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]

    #print(schema)

     #   def matte(tal1, tal2):
    #            return tal1+tal2, tal1-tal2, tal1/tal2

     #   print(matte(23,32))



   # def lista_djur():
   #     return ["horse","cat","dog"], "Dennis"
   # print(lista_djur()[0])

     #   adress = {"namn":"Dennis","efternamn":"Rudin"}
     #   print(adress)
      #  print(list(adress.keys()))
      #  print(adress.values())
      #  print(adress["namn"])
adress = [
    {"namn":"Dennis","efternamn":"Rudin"},
    {"namn":"Nina","efternamn":"Rudin"},
    {"namn":"Juha","efternamn":"Rudin"},
    {"namn":"Kalle","efternamn":"Rudin"}
]

print(adress[0].get("nisse"))

for person in adress:
    print("Namn:", person["namn"])
    print("Efternamn:",person["efternamn"])
   # print(person)
