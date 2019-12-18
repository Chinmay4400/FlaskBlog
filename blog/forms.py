from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blog.models import User
from flask_login import current_user

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
    

class UpdateAccountForm(Form):
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data !=  current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is not available. Please try again.')
            
    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('This email is already associated with an account. Please try again.')
        
    
class PostForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')