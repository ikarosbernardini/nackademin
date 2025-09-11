#file_obj = open('data.txt', 'w', encoding='utf-8') # öppnar filen , skriver jag 'w' så skriver jag skriver jag 'r' så läser jag 
#file_obj.write('Hello, world!\nJag heter Ikaros\nNisse är visst en tomte') # skriver i filen 
#file_obj.close() # stänger filen 

    #  klass = {
    #     "elever": ["Dennis", "Kenta", "Kalle","Nisse"],
    #     "klassrum": 'C401',
    #  }

#print("Elever = " + str(klass))

"""""
elever: list = klass["elever"]
elever.append("Ikaros")    #["name"]

klassrum = klass["klassrum"]

with open('data.txt', 'a', encoding='utf-8') as file_obj:
   file_obj.write('Login uppgifter : Ikaros Bernardini\nPassword : Telia123')
with open('data.txt', encoding='utf-8') as file_obj:  # fördragna sättet 
    for line in file_obj.readlines():
     print('rad: '+line)
"""
with open('helloworld.txt' 'W') as file:
    text = file.write("Hello World")





with open('helloworld.txt') as file:
    
#Alt 1
    text = file.read()
    print(text[0:5])

#Alt 2 
    print(file.read()[0:5])
#Alt 3
    text = file.read()[0:5]
    print(text)
