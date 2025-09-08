combination = "Alice" * 42

print(combination)

# Det går inte att skriva + mellan sträng och integer
# print("Alice" + 42)  # Detta ger fel, utan man får konvertera 42 till sträng först eller så funkar att göra * som ovan

spam = 40
eggs = 2

spam = spam + 2

print(spam)

# Genom att skriva spam = 40 och sedan spam = spam + 2 så har vi ändrat värdet på spam från 40 till 42
# Variabelnamn får inte innehålla mellanslag, bindestreck eller specialtecken som $ eller '.
# De får inte börja med en siffra, men det går bra att börja med ett understreck (_).
# Exempel på giltiga namn: current_balance, account4, _42, TOTAL_SUM
# Exempel på ogiltiga namn: current-balance, current balance, 4account, TOTAL$SUM, 'hello'

print("Hello, World!")
print("What is your name?")
my_name = input()
print("Hello, " + my_name + "!")
print("The length of your name is:")
print(len(my_name))
print("What is your age?")
my_age = input()
print("Your name is " + my_name + " and your age is " + my_age + " and your age is " + str(int(my_age) + 1) + " in about one year.")

#

my_name = input('>')

# Denna funktion läser in en rad text från användaren och returnerar den som en sträng. Även om användaren skriver in en siffra, så kommer den att returneras som en sträng.


