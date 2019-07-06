import datetime

from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('social.db')

class User(UserMixin ,Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=True)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)