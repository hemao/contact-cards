from peewee import *

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

