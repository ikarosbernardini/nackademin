
           with open("timpriser.csv") as file:
               content = (file.readline())
                
               for rad in file:
                   content += rad
               print(content)


# SKapa några rader kod som öppnar en fil i skrivläge. Filen skall heta helloworld.txt"
# Skriv texten  "Hello World!#"

with open('timpriser.csv') as file_obj:
    for line in file_obj.readlines():
        rad = line.split(",")
        tid = rad[3][11:16]
        euro = rad[1]
        sek = rad [0]

        print(f"Klockan {tid} kostar elen {sek} svenska kronor och {euro} euro")