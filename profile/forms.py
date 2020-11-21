from flask_wtf import FlaskForm
from wtforms import (StringField,
                     TextAreaField,
                     SubmitField,
                     PasswordField)
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
    # signup_bt = SubmitField('Sign Up')
    # invitate = SubmitField('Continue as guest')

...

class SignupForm(FlaskForm):
    #"""Sign up for a user account."""
    name = StringField('Name', [
        DataRequired()])
    email = StringField('Email', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    password = PasswordField('Password', [
        DataRequired(message="Please enter a password."),
        Length(min=4, message="Password too short")
    ])
    confirmPassword = PasswordField('Repeat Password', [
            EqualTo(password, message='Passwords must match.')
            ])
    # title = SelectField('Title', [DataRequired()],
    #                     choices=[('Farmer', 'farmer'),
    #                              ('Corrupt Politician', 'politician'),
    #                              ('No-nonsense City Cop', 'cop'),
    #                              ('Professional Rocket League Player', 'rocket'),
    #                              ('Lonely Guy At A Diner', 'lonely'),
    #                              ('Pokemon Trainer', 'pokemon')])
    # website = StringField('Website', validators=[URL()])
    # birthday = DateField('Your Birthday')
    # recaptcha = RecaptchaField()
    submit = SubmitField('Submit')