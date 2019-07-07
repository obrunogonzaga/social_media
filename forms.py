from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                                Length, EqualTo)

from models import User

def name_exists(form, field):
    if User.select().where(User.username == field.data).existis():
        raise ValidationError('User with that name already exists')

def email_exists(form, field):
    if User.select().where(User.email == field.data).existis():
        raise ValidationError('User with that email already exists')

class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(),
        Regexp(r'ˆ[a-zA-Z0-9_]+$',
        message=("Username should be one word, letters, "
                 "numbers, and underscore only.")),
        name_exists]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Passwords must match')
        ]
    )
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()]
    )