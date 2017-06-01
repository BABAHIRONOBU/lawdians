from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError

from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[InputRequired(), Length(1, 64)])
    password = PasswordField('password', validators=[InputRequired(),
                                                     EqualTo('password2', message='Password must match.')])
    password2 = PasswordField('Confirm password', validators=[InputRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')
