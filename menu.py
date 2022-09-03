from manager import *
import os.path

welcome_message = "Welcome to Password Manager v0.4!"
commands = "\n1: View Saved Passwords\n2: Generate a Password for a site or input your own\n3: Remove a site and its password\n4: Command list"
print(welcome_message)
print(commands)

def cmmd_list():
   print(commands)

def menu():
 user_input = str(input(""))
 options = {
    "1": recall,
    "2": add,
    "3": delete,
    "4": cmmd_list
 } 
 options[user_input]()

if os.path.exists("safe.txt") == False:
   create_default()
else:
   pass

while True:
   try:
    menu()
   except KeyError:
    print("Invalid input")

   
