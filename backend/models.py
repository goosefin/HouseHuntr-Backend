from multiprocessing.dummy import Array
from peewee import *

from flask_login import UserMixin

DATABASE = SqliteDatabase('apartments.sqlite')

class User(UserMixin,Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE

class Apartment(Model):
    # address = CharField() not NULL
    bedrooms = IntegerField()
    price = IntegerField()
    pets = BooleanField()
    # amenities = Array()
    link = CharField()
    scheduled_showing = BooleanField()
    scheduled_showing_time = CharField()
    seen = BooleanField()
    applied = BooleanField()
    user = ForeignKeyField(User, backref='apartments')

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User,Apartment], safe=True)
    print('Connected to database')
    DATABASE.close()
