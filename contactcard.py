from main import *
from peewee import *

class ContactBook:
    def __init__(self, first_name, last_name, username, type):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.type = type

class User(ContactBook):
    def __init__(self, first_name, last_name, username):
        super().__init__(first_name,last_name,username,"user") 

    def add_user(self):
        Users.create(first_name=self.first_name, last_name=self.last_name, username=self.username)

class Contact(ContactBook):
    def __init__(self, first_name, last_name, phone, addr_line1, addr_line2, zipcode, username):
        super().__init__(first_name,last_name,username,"contact") 
        self.phone = phone
        self.addr_line1 = addr_line1
        self.addr_line2 = addr_line2
        self.zipcode = zipcode

    def add_contact(self):
        Contacts.create(first_name = self.first_name, last_name = self.last_name, phone = self.phone, addr_line1 = self.addr_line1, addr_line2 = self.addr_line2, zipcode = self.zipcode, username = self.username)


print("Welcome to Contactbook")
User_Input = input(f'''Choose from one of the following options(type in the numbers)
1. Register
2. Add Contact
3. Find Contact 
4. Display All
''')

if (user_Input == 1):
    first_name = input("Enter your first name")
    last_name = input("Enter your last name")
    username = input("Enter your username")
    newuser =  User(first_name, last_name, username)
    newuser.add_user()
    print(f"You have been registered successfully!")
else if (user_Input == 2):
    username = input("Enter your username")
    first_name = input("Enter contact's first name")
    last_name = input("Enter contact's last name")
    email = input("Enter contact's email address")
    phone = input("Enter contact's phone number")
    addr_line1 = input("Enter contact's address(line 1)")
    addr_line2 = input("Enter contact's address(line 2)")
    zipcode = input("Enter contact's zip code")
else if (user_input == 3):
    username = input("Enter your username")
    
    


