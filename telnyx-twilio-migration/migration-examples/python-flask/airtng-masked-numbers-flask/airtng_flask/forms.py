from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Length, Email, URL


class RegisterForm(FlaskForm):
    name = StringField(
        'Tell us your name:',
        validators=[
            DataRequired(message="Name is required"),
            Length(min=3, message="Name must greater than 3 chars"),
        ],
    )
    email = StringField(
        'Enter your E-mail:',
        validators=[
            DataRequired("E-mail is required"),
            Email(message="Invalid E-mail address"),
        ],
    )
    password = PasswordField(
        'Password:', validators=[DataRequired("Password is required")]
    )
    country_code = StringField(
        'Country Code:',
        validators=[
            DataRequired("Country code is required"),
            Length(
                min=1, max=4, message="Country code must be between 1 and 4 numbers"
            ),
        ],
    )

    phone_number = IntegerField(
        'Phone Number:', validators=[DataRequired("Valid phone number is required")]
    )


class LoginForm(FlaskForm):
    email = StringField(
        'E-mail:',
        validators=[
            DataRequired("E-mail is required"),
            Email(message="Invalid E-mail address"),
        ],
    )
    password = PasswordField(
        'Password:', validators=[DataRequired("Password is required")]
    )


class VacationPropertyForm(FlaskForm):
    description = StringField(
        'Description:', validators=[DataRequired("Description is required")]
    )
    image_url = StringField(
        'Image URL:',
        validators=[
            DataRequired("Image Url required"),
            URL(message="Invalid Image Url"),
        ],
    )


class ReservationForm(FlaskForm):
    message = StringField('Message:', validators=[DataRequired("Message is required")])

    property_id = HiddenField()


class ReservationConfirmationForm(FlaskForm):
    From = StringField('From')
    Body = StringField('Body')


class ExchangeForm(FlaskForm):
    From = StringField('From')
    To = StringField('To')
    Body = StringField('Body')
