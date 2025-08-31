
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

import random
for i in range(100):  # Perform 100 coin flips.
    if random.randint(0, 1) == 0:
        print('H', end=' ')
    else:
        print('T', end=' ')
print()  # Print one newline at the end.




