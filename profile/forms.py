from flask_wtf import FlaskForm
from wtforms import (StringField,
                     TextAreaField,
                     SubmitField,
                     PasswordField,
                     IntegerField)
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LogInForm(FlaskForm):
    name = StringField('Nombre', [
        DataRequired()])
    password = PasswordField('Contraseña',[
        DataRequired()])
    login_bt = SubmitField('Iniciar sesión')
    
...

class SignupForm(FlaskForm):
    #"""Sign up for a user account."""
    name = StringField('Nombre', [
        DataRequired()]
    )
    email = StringField('Correo', [
        Email(message='Not a valid email address.'),
        DataRequired()]
    )
    password = PasswordField('Contraseña', [
        DataRequired(message="Please enter a password."),
        Length(min=4, message="Password too short")]
    )
    
    age = IntegerField('Edad')
    coctailNum = IntegerField('Codigo coctelera',[
        DataRequired()]
    )
    submit = SubmitField('Registrar')


