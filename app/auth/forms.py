from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Email(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')

class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Email(), Length(1, 64)])
    username = StringField('Username', validators=[Required(), Length(1, 64),
                                                   Regexp('^[a-zA-Z][a-zA-Z0-9_.]*$', 0,
                                                          'Username must have only letters,'
                                                          'numbers, dots or underscores')])
    password = PasswordField('Password',
                             validators=[Required(), EqualTo('password2', message='Password must match.')])
    password2 =PasswordField('Confirm password',
                             validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class ChangePasswordForm(Form):
    old_password = PasswordField('Old password', validators=[Required()])
    password = PasswordField('New password', validators=[
        Required(), EqualTo('password2', message='Password must match')])
    password2 = PasswordField('Confirm New Password', validators=[Required()])
    submit = SubmitField('Update Password')

class PasswordResetRequestForm(Form):
    email = StringField('Email', validators=[Required(),
                                             Email(), Length(1, 64)])
    submit = SubmitField('Reset Password')

class PasswordResetForm(Form):
    email = StringField('Email', validators=[Required(),
                                             Email(), Length(1, 64)])
    password = PasswordField('New Password', validators=[
        Required(), EqualTo('password2', message='Password must match')])
    password2 = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Reset Password')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Unknown Email Address')

class ChangeEmailForm(Form):
    email = StringField('New email', validators=[
        Required(), Email(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

