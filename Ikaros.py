print("Please input your username and password.")
username = input('Username: ')
password = input('Password: ')
if username == 'Ikaros':
    print('Hello, Ikaros')
    if password == 'Telia123':
        print('Access granted.')
    else:
        print('Wrong password.')
        repeat = input('Try again? (yes/no): ')
        if repeat.lower() == 'yes':
            password = input('Enter password: ')
            if password == 'Telia123':
                print('Access granted.')
            else:
                print('Access denied.') 
                