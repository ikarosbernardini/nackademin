corret_username = ("Ikaros") # correct login username
correct_password = ("Telia123") # correct login password

print("Please input your username and password.") # tells user to input username and password
password_fails = 3 # number of attempts user has to input correct username and password

while password_fails > 0: # while loop to allow user to try again if they input wrong username or password
    
    username = input("Username: ") # asks user to input username
    password = input("Password: ") # asks user to input password

    if username == corret_username and password == correct_password: # checks if username and password are correct
        print(f"Welcome {username}! You have successfully logged in.") # if correct, user is logged in
        break # breaks the loop
    else: # if incorrect, user is told to try again
        print("Invalid username or password. Please try again.")
        password_fails -= 1 # subtracts 1 from number of attempts left
        if password_fails == 0: # if user has no attempts left, they are told access is denied
            print("Too many failed attempts. Access denied.")
            break # breaks the loop
        else: # if user has attempts left, they are told how many attempts they have left
            print(f"You have {password_fails} attempts left.")