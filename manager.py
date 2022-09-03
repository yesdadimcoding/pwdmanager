from password_generator import *  

def text_to_dict(file_to_be_converted):                                 ## converts txt file to dictionary
   Dictionary = {}
   file = open(file_to_be_converted,'r+')
   for line in file:
    site, password = line.strip().split(":")
    Dictionary[site] = password
   file.close()
   return Dictionary

def is_random():                                                        ## asks if the user wants to use the password generator or put one in themselves
   a = str(input("1: Generate new password \n2: User Input\n"))
   if a == '1':
      return True
   elif a == '2':
      return False
   else:
      print("Invalid input")
      is_random()

def already_exists(user_input):                                                      ## checks if the site input already exists in the file
   psswrd_dict = text_to_dict("safe.txt")
   if user_input in psswrd_dict:
      return True
   else:
      return False

def dict_to_text(dictionary):                                                                 ## converts dictionary to text file
   file = open("safe.txt","w")
   for items in dictionary:
      file.write(items + ":" + dictionary[items] + "\n")
   file.close()

def overwrite(user_input):                                                                     ## overwrites password
   print("site already exists, would you like to overwrite?")
   file = open("safe.txt","a")
   decision = str(input("1: Yes\n2: No\n"))
   psswrd_dict = text_to_dict("safe.txt")
   if decision == "1":
      if is_random() == True:
         psswrd_dict[user_input] = generate_random_password()
         dict_to_text(psswrd_dict)
      else:
         psswrd_dict[user_input] = str(input("Please input your password: "))
         dict_to_text(psswrd_dict)
   elif decision == "2":
      print("password rewrite cancelled")
   else:
      print("invalid input")
   file.close()

def add():                                                                            ## adds a site and its password to the txt file
 site = str(input("Name of site: "))
 file = open("safe.txt","a")
 if already_exists(site) == False:
   if is_random() == True:
      file.write(site + ":" + generate_random_password() + "\n")
   else:
      file.write(site + ":" + str(input("Please input your password: ")) + "\n")
 else:
   overwrite(site)
 file.close()

def delete():                                                                         ## removes a site and its password from the database
 site = str(input("site to be deleted: "))
 if already_exists(site) == True:
   psswrd_dict = text_to_dict("safe.txt")
   del psswrd_dict[site]
   dict_to_text(psswrd_dict)
   print("site and password removed sucessfully")
 else: 
   print("site does not exist.")

def recall():                                                                          ## recalls a sites password
  site = str(input("Recall password of: "))
  psswrd_dict = text_to_dict("safe.txt")
  if already_exists(site) == True:
   print(psswrd_dict[site])
  else:
   print("site does not exist, would you like to add?")
   decision = str(input("1: Yes\n2: No\n"))
   if decision == "1":
      if is_random() == True:
       psswrd_dict[site] = generate_random_password()
       dict_to_text(psswrd_dict)
      else:
       psswrd_dict[site] = str(input("Please input your password: "))
       dict_to_text(psswrd_dict)
   
def create_default():                                                                      ## create a default profile      
 file = open("safe.txt","w")
 file.write("default:default\n")
 file.close

