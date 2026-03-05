from xmlunittest import XmlTestCase
from sms2fa_flask.models import User
from passlib.hash import bcrypt


class BaseTest(XmlTestCase):

    def setUp(self):
        from sms2fa_flask import app, db
        self.app = app
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.db = db
        self.client = self.app.test_client()
        User.query.delete()
        self.email = 'example@example.com'
        self.password = '1234'
        pwd_hash = bcrypt.encrypt(self.password)
        self.default_user = User(email=self.email,
                                 phone_number='+555155555555',
                                 password=pwd_hash)
        db.save(self.default_user)
