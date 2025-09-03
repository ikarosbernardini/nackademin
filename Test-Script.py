   # def count(): # skapar en funktion som är menad för att räkna från 1-10 med en for loop. 
   #     for i in range(1, 11): # för varje index i "range" ska den printa ut siffrona 1 upp till 10 
   #         print(i) # printar ut index
    #    count() # anropar funktionen count 

       #     def count(max_limit):
        #        for i in range(max_limit):
       #             print(i)
        #    count(max_limit=101)

""" 
def add(a, b):
return a + b

result = add(5, 3)
print(result) 

print("I eat {} alot of burritos".format(result))"""
"""
spam = 1 

def hälsa(spam: int):
    if spam == 1:
        print("Hello!")
    elif spam == 2:
        print("Howdy")
    else:
        print("Greetings!")

hälsa(spam)


try: # fungerar som try.parse eller try.catch C# 


except SystemError:

    pass


try:
"""
import pyperclip

text = pyperclip.paste()  # Get the text off the clipboard.
alt_text = ''  # This string holds the alternating case.
make_uppercase = False
for character in text:
    # Go through each character and add it to alt_text:
    if make_uppercase:
        alt_text += character.upper()
    else:
        alt_text += character.lower()

    # Set make_uppercase to its opposite value:
    make_uppercase = not make_uppercase
pyperclip.copy(alt_text)  # Put the result on the clipboard.
print(alt_text)  # Print the result on the screen too.