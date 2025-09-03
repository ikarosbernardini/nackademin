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

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
