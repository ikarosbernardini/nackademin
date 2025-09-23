import hashlib


input_password = input('Type your password: ')

hash_password = hashlib.sha256(input_password.encode()).hexdigest()

print(f'Hashed password : {hash_password}')

