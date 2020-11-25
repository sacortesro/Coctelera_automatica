from flask_wtf import FlaskForm
from wtforms import (StringField,
                     TextAreaField,
                     SubmitField,
                     PasswordField,
                     DateField)
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo,
                                Length)

class LogInForm(FlaskForm):
    name = StringField('Name', [
        DataRequired()])
    password = PasswordField('Password',[
        DataRequired()])
    login_bt = SubmitField('Log in')
    
...

class SignupForm(FlaskForm):
    #"""Sign up for a user account."""
    name = StringField('Name', [
        DataRequired()]
    )
    email = StringField('Email', [
        Email(message='Not a valid email address.'),
        DataRequired()]
    )
    password = PasswordField('Password', [
        DataRequired(message="Please enter a password."),
        Length(min=4, message="Password too short")]
    )
    confirmPassword = PasswordField('Confirm password', [
            EqualTo(password, message='Passwords must match.')]
    )
    age = DateField('Your age')
    coctailNum = StringField('Codigo coctelera',[
        DataRequired()]
    )
    coctailNum = StringField('Machine serial',[DataRequired()])
    submit = SubmitField('Sign Up')


