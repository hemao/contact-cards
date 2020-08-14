from main import *
from peewee import *
       

class User():
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def add_user(self):
        Users.create(first_name=self.first_name, last_name=self.last_name, username=self.username)


class Contact():
    def __init__(self, first_name, last_name, email, phone, addr_line1, addr_line2, zipcode, username):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.addr_line1 = addr_line1
        self.addr_line2 = addr_line2
        self.zipcode = zipcode
        self.username = username

    def add_contact(self):
        Contacts.create(first_name = self.first_name, last_name = self.last_name, email =  self.email, phone = self.phone, addr_line1 = self.addr_line1, addr_line2 = self.addr_line2, zipcode = self.zipcode, username = self.username)




print("Welcome to Contactbook")
user_input = input(f'''Choose from one of the following options(type in the numbers)
1. Register
2. Add Contact
3. Find Contact 
4. Display All
''')
print(user_input)
if (int(user_input) == 1):
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    username = input("Enter your username: ")
    newuser =  User(first_name, last_name, username)
    newuser.add_user()
    print(f"You have been registered successfully!")
elif (int(user_input) == 2):
    username = input("Enter your username: ")
    first_name = input("Enter contact's first name: ")
    last_name = input("Enter contact's last name: ")
    email = input("Enter contact's email address: ")
    phone = input("Enter contact's phone number: ")
    addr_line1 = input("Enter contact's address(line 1): ")
    addr_line2 = input("Enter contact's address(line 2): ")
    zipcode = input("Enter contact's zip code: ")
    newcontact =  Contact(first_name, last_name, email, phone, addr_line1, addr_line2, zipcode, username)
    newcontact.add_contact()
    print(f"Your contact {first_name} {last_name} has been added successfully!")
elif (int(user_input) == 3):
    username = input("Enter your username")
    first_name = input("Enter contact's first name")
    last_name = input("Enter contact's last name")
    
elif(int(user_input) == 4):
    print("display all data")
else:
    print("No matching input")
    
    
    


