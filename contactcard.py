from model import *
from peewee import *
       
class User():
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def add_user(self):
        Users.create(first_name=self.first_name, last_name=self.last_name, username=self.username)


class Contact():
    def __init__(self, first_name, last_name, email, phone, address, city, state, zipcode, username):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.username = username

    def add_contact(self):
        Contacts.create(first_name = self.first_name, last_name = self.last_name, email =  self.email, phone = self.phone, address = self.address, city = self.city, state = self.state, zipcode = self.zipcode, username = self.username)
   

class ContactBook():
    def __init__(self,username,first_name = ""):
        self.username = username
        self.first_name = first_name

    def find_contact(self):
        user = Contacts.get(Contacts.first_name == self.first_name)
        print("******************** Contact Details ********************\n")
        print(f'''
            First Name: {user.first_name}
            Last Name : {user.last_name}
            Phone     : {user.phone}
            Address   : {user.address} {user.city} {user.state} {user.zipcode}
            ''')

    def find_allcontacts(self):
        print("******************** My Contact Book********************\n")
        for user in Contacts.select().where(Contacts.username == self.username):
            print(f'''
            First Name: {user.first_name}
            Last Name : {user.last_name}
            Phone     : {user.phone}
            Address   : {user.address} {user.city} {user.state} {user.zipcode}
            ''')
    def update_firstname(self, firstname, new_firstname, username):
            q = (Contacts.update(first_name = new_firstname).where((Contacts.first_name == self.first_name) & (Contacts.username == self.username)))
            q.execute()

    def update_lastname(self, firstname, new_lastname, username):
            q = (Contacts.update(last_name = new_lastname).where((Contacts.first_name == self.first_name) & (Contacts.username == self.username)))
            q.execute()

    def update_email(self, firstname, new_email, username):
            q = (Contacts.update(email = new_email).where((Contacts.first_name == self.first_name) & (Contacts.username == self.username)))
            q.execute()

    def update_phone(self, firstname, new_phone, username):
            q = (Contacts.update(phone = new_phone).where((Contacts.first_name == self.first_name) & (Contacts.username == self.username)))
            q.execute()

    def update_address(self, firstname, new_address, username):
            q = (Contacts.update(address = new_address).where((Contacts.first_name == self.first_name) & (Contacts.username == self.username)))
            q.execute() 

    def update_city(self, firstname, new_city, username):
            q = (Contacts.update(city = new_city).where((Contacts.first_name == self.first_name) & (Contacts.username == self.username)))
            q.execute() 

    def update_state(self, firstname, new_state, username):
            q = (Contacts.update(state = new_state).where((Contacts.first_name == self.first_name) & (Contacts.username == self.username)))
            q.execute()  

    def update_zipcode(self, firstname, new_zipcode, username):
            q = (Contacts.update(zipcode = new_zipcode).where((Contacts.first_name == self.first_name) & (Contacts.username == self.username)))
            q.execute() 

    def delete_contact(self):
            q = (Contacts.delete().where((Contacts.first_name == self.first_name) & (Contacts.username == self.username)))
            q.execute()                
        
main_menu = True
print("Welcome to Contactbook")
while main_menu:

    user_input = input(f'''Choose from one of the following options(type in the serial numbers)
    **********************************
    1. Register
    2. Add Contact
    3. Find Contact 
    4. Update Contact
    5. Delete Contact
    6. Display All
    7. Exit
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
            address = input("Enter contact's address:")
            city = input("Enter contact's city:")
            state = input("Enter contact's state:")
            zipcode = input("Enter contact's zip code:")
            newcontact =  Contact(first_name, last_name, email, phone, address, city, state, zipcode, username)
            newcontact.add_contact()
            print(f"Your contact {first_name} {last_name} has been added successfully!")
            choice = input("Do you want to add more?(y or n)")
            if (choice == "n"):
                more = False

    elif (int(user_input) == 3):

        more = True
        username = input("Enter your username: ")
        while more:
            first_name = input("Enter contact's first name: ")
            contact_book = ContactBook(username, first_name)
            contact_book.find_contact()
            choice = input("Do you want to find more?(y or n): ")
            if (choice == "n"):
                more = False
    elif (int(user_input) == 4):
        more = True
        username = input("Enter your username")
        while more:
            first_name = input("Enter the first name of the contact you would like to update : ")
            contact_book = ContactBook(username, first_name)
            contact_book.find_contact()
            update_choice = input(f'''Fields to be updated(type in the serial numbers)
            **********************************
            1. First Name
            2. Last Name
            3. Email
            4. Phone
            5. Address
            6. City
            7. State
            8. Zip
            **********************************
            ''')
            if (int(update_choice) == 1):
                new_first_name = input("Enter contact's new first name: ")
                contact_book.update_firstname(first_name, new_first_name, username)
            elif (int(update_choice) == 2):
                new_last_name = input("Enter contact's new last name: ")
                contact_book.update_lastname(first_name, new_last_name, username)
            elif (int(update_choice) == 3):
                new_email = input("Enter contact's new email: ")
                contact_book.update_email(first_name, new_email, username)
            elif (int(update_choice) == 4):
                new_phone = input("Enter contact's new phone: ")
                contact_book.update_phone(first_name, new_phone, username)
            elif (int(update_choice) == 5):
                new_address = input("Enter contact's new address: ")
                contact_book.update_address(first_name, new_address, username)
            elif (int(update_choice) == 6):
                new_city = input("Enter contact's new city: ")
                contact_book.update_city(first_name, new_city, username)
            elif (int(update_choice) == 7):
                new_state = input("Enter contact's new state: ")
                contact_book.update_state(first_name, new_state, username)
            elif (int(update_choice) == 8):
                new_zipcode = input("Enter contact's new zipcode: ")
                contact_book.update_zipcode(first_name, new_zipcode, username)

            choice = input("Do you want to update more contacts?(y or n): ")
            if (choice == "n"):
                more = False    

    elif(int(user_input) == 5):
        more = True
        username = input("Enter your username")
        first_name = input("Enter the first name of the contact you would like to delete : ")
        while more:
            contact_book = ContactBook(username, first_name)
            contact_book.delete_contact()
            choice = input("Do you want to delete contact again?(y or n)")
            if (choice == "n"):
                more = False

    elif(int(user_input) == 6):
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

    
    
    


