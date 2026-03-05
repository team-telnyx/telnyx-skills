from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, TelField, EmailField
from wtforms.validators import DataRequired
import phonenumbers


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class SignUpForm(FlaskForm):
    first_name = StringField('first name', validators=[DataRequired()])
    last_name = StringField('last name', validators=[DataRequired()])
    phone_number = TelField('phone number', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', [validators.DataRequired(),
                             validators.EqualTo('confirm',
                             message='Passwords must match')])
    confirm = PasswordField('confirm password', [validators.DataRequired()])

    def validate_phone_number(self, field):
        error_message = "Invalid phone number. Example: +353857688030"
        try:
            data = phonenumbers.parse(field.data)
        except:
            raise validators.ValidationError(error_message)
        if not phonenumbers.is_possible_number(data):
            raise validators.ValidationError(error_message)

    @property
    def as_dict(self):
        data = self.data
        del data['confirm']
        return data
