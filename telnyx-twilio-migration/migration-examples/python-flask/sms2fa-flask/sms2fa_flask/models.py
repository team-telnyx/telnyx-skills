from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import phonenumbers
from passlib.hash import bcrypt
from phonenumbers import PhoneNumberFormat
db = SQLAlchemy()


class User(db.Model, UserMixin):

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone_number = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)

    @classmethod
    def save_from_dict(cls, data):
        user = User(**data)
        user.set_password(data['password'])
        user.active = False
        db.save(user)
        return user

    def is_password_valid(self, given_password):
        return bcrypt.verify(given_password, self.password)

    def set_password(self, new_password):
        self.password = bcrypt.encrypt(new_password)

    @property
    def international_phone_number(self):
        parsed_number = phonenumbers.parse(self.phone_number)
        return phonenumbers.format_number(parsed_number,
                                          PhoneNumberFormat.INTERNATIONAL)

    # The methods below are required by flask-login
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email
