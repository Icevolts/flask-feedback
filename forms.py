from wtforms import StringField,PasswordField
from wtforms.validators import InputRequired,Length,Email
from flask_wtf import FlaskForm

class RegisterForm(FlaskForm):
    '''Form for creating new user'''
    username = StringField('Username', validators=[InputRequired(),Length(max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8)])
    email = StringField('Email', validators=[InputRequired(),Email(),Length(max=50)])
    first_name = StringField('First Name', validators=[InputRequired(),Length(max=30)])
    last_name = StringField('Last Name', validators=[InputRequired(),Length(max=30)])

class LoginForm(FlaskForm):
    '''Form for logging in existing user'''
    username = StringField('Username', validators=[InputRequired(),Length(max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8)])

class FeedbackForm(FlaskForm):
    '''Form for adding feedback'''
    title = StringField('Title',validators=[InputRequired(),Length(max=100)])
    content = StringField('Content',validators=[InputRequired()])

class DeleteForm(FlaskForm):
    '''Blank form for removing feedback or user'''
    