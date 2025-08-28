
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

from time import sleep
def show_some_looping():
    the_number: int = 10


while the_number > 1:
    print(f"not yet...{the_number}")
    sleep(1)
    the_number -= 1
    print("Happy New Year!")
 
show_some_looping()