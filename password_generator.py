import string
import random
import pyperclip

## characters to generate a password from
alphabets = list(string.ascii_letters)
numbers = list(string.digits)
special_characters = list("!@#$%^&*()")


def generate_random_password():
    ## length of password from the user
    length = int(input("Password length: "))

    ## number of each character type
    alphabet_count = random.choice([*range(1, length - 2, 1)]) 
    numbers_count = random.choice([*range(length - alphabet_count)])
    special_characters_count = length - numbers_count - alphabet_count

    ## initializing password
    password = []

    ## picking random alphabets 
    for i in range(alphabet_count):
     password.append(random.choice(alphabets))

    ## picking random numbers
    for i in range(numbers_count):
     password.append(random.choice(numbers))

    ## picking random special characters 
    for i in range(special_characters_count):
     password.append(random.choice(special_characters))

    ## shuffle resultant password
    random.shuffle(password)

    ##  converting the list to string 
    ##  join password
    password = "".join(password)
    return password