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

class ContactBook():
    def __init__(self,username,first_name = ""):
        self.username = username
        self.first_name = first_name

    def find_contact(self):
        print(self.first_name)
        print(self.username)
        selected_row = Contacts.get(Contacts.first_name == self.first_name)
        print(selected_row)

    def find_allcontacts(self):
        print("******************** My Contact Book********************\n")
        for user in Contacts.select().where(Contacts.username == self.username):
            print(f'''
            First Name: {user.first_name}
            Last Name : {user.last_name}
            Phone     : {user.phone}
            Address   : {user.addr_line1} {user.addr_line2} {user.zipcode}
            ''')


main_menu = True
print("Welcome to Contactbook")
while main_menu:

    user_input = input(f'''Choose from one of the following options(type in the serial numbers)
    **********************************
    1. Register
    2. Add Contact
    3. Find Contact 
    4. Display All
    5. Exit
    **********************************
    ''')

    if (int(user_input) == 1):
        
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        username = input("Enter your username: ")
        newuser =  User(first_name, last_name, username)
        newuser.add_user()
        print(f"You have been registered successfully!")

    elif (int(user_input) == 2):

        more = True
        username = input("Enter your username: ")
        while more:
            first_name = input("Enter contact's first name: ")
            last_name = input("Enter contact's last name: ")
            email = input("Enter contact's email address: ")
            phone = input("Enter contact's phone number: ")
            addr_line1 = input("Enter contact's address(line 1):")
            addr_line2 = input("Enter contact's address(line 2):")
            zipcode = input("Enter contact's zip code: ")
            newcontact =  Contact(first_name, last_name, email, phone, addr_line1, addr_line2, zipcode, username)
            newcontact.add_contact()
            print(f"Your contact {first_name} {last_name} has been added successfully!")
            choice = input("Do you want to add more?(y or n)")
            if (choice == "n"):
                more = False

    elif (int(user_input) == 3):

        more = True
        username = input("Enter your username")
        while more:
            first_name = input("Enter contact's first name")
            contact_book = ContactBook(username, first_name)
            contact_book.find_contact()
            choice = input("Do you want to find more?(y or n)")
            if (choice == "n"):
                more = False

    elif(int(user_input) == 4):

        more = True
        username = input("Enter your username")
        while more:
            contact_book = ContactBook(username)
            contact_book.find_allcontacts()
            choice = input("Do you want to display contacts again?(y or n)")
            if (choice == "n"):
                more = False

    else:
        print("Good Bye!")
        main_menu = False

    
    
    


