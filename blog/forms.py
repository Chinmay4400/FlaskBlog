from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User

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

    def validate_username(self, username):
        
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is not available. Please try again.')
            
    def validate_email(self, email):
        
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('This email is already associated with an account. Please try again.')


class loginForm(Form):
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired(), Length(min=6, max = 16)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def validate_email(self, email):
        
        email = User.query.filter_by(email=email.data).first()
        if not email:
            raise ValidationError('This email is not in the database. Please sign up first.')