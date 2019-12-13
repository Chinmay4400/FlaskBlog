from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class registrationForm(Form):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=6, max = 16)])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), Length(min=6, max = 16), EqualTo('password')])
    submit = SubmitField('Sign Up')

class loginForm(Form):
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=6, max = 16)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')