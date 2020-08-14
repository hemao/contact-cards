from peewee import *
print("Hello")
#setup the database connection
db = PostgresqlDatabase('contactcard', user='postgres', password='',
                        host='localhost', port=5432)



#define a BaseModel class that sets the database connection
class BaseModel(Model):
    class Meta:
        database = db

#define users model and have it inherit from the BaseModel class
class Users(BaseModel):
    first_name = CharField()
    last_name = CharField()
    username = CharField(primary_key=True)

#define contacts model and have it inherit from the BaseModel class
class Contacts(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone = CharField()
    addr_line1 = CharField()
    addr_line2 = CharField()
    zipcode = IntegerField()
    username = CharField()

db.connect()

db.create_tables([Users, Contacts])

#user = Users(first_name='Hema1', last_name='Omprakash1', username='hemao1' )
#user.save()
#Users.create(first_name='Hema1', last_name='Omprakash1', username='hemao1')
#selected_row = Users.get(Users.first_name == 'Hema1')
#print(selected_row.last_name)

# class ContactBook:
#     def __init__(self, first_name, last_name, username, type):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username
#         self.type = type

# class user(ContactBook):
#     def __init__(self, first_name, last_name, username):
#         super().__init__(first_name,last_name,username,"user") 

#     def add_user(self):
#         Users.create(first_name=self.first_name, last_name=self.last_name, username=self.username)

# class contact(ContactBook):
#     def __init__(self, first_name, last_name, phone, addr_line1, addr_line2, zipcode, username):
#         super().__init__(first_name,last_name,username,"contact") 
#         self.phone = phone
#         self.addr_line1 = addr_line1
#         self.addr_line2 = addr_line2
#         self.zipcode = zipcode

#     def add_contact(self):
#         Contacts.create(first_name = self.first_name, last_name = self.last_name, phone = self.phone, addr_line1 = self.addr_line1, addr_line2 = self.addr_line2, zipcode = self.zipcode, username = self.username)


# print("Welcome to Contactbook")
# User_Input = print(f'''Select from one of the following options
# 1. Register
# 2. Add Contact
# 3. Find Contact 
# 4. Display All
# ''')



