#Ceate a function to that generate randam password
#Option : use parameter for for no of character in password


import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_length = int(input("enter the sixe of passwards  :"))
password = generate_random_password(password_length)
print(f"Generated password: {password}")
