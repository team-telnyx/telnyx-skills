from .base import BaseTest
from flask import url_for, session
from flask.ext.login import current_user
import six
from sms2fa_flask.models import User
if six.PY3:
    from urllib.parse import urlparse
else:
    from urlparse import urlparse


class SignUpTest(BaseTest):
    def setUp(self):
        super(SignUpTest, self).setUp()
        data = {'email': '00@7.com',
                'password': self.password,
                'confirm': self.password,
                'first_name': 'James',
                'last_name': "O'Seven",
                'phone_number': "+5599999007"}
        self.data = data

    def test_sign_up_success_creates_user(self):
        self.client.post(url_for('sign_up'), data=self.data)

        user = User.query.get(self.data['email'])
        self.assertTrue(user)
        self.assertTrue(user.is_password_valid(self.data['password']))
        self.assertEquals(user.phone_number, self.data['phone_number'])

    def test_sign_up_success_redirects_to_confirmation(self):
        response = self.client.post(url_for('sign_up'), data=self.data)

        expected_path = url_for('confirmation')
        self.assertEquals(302, response.status_code)
        self.assertIn(expected_path, urlparse(response.location).path)

    def test_sign_up_success_puts_user_email_in_session(self):
        with self.app.test_client() as client:
            client.post(url_for('sign_up'), data=self.data)
            self.assertEquals(self.data['email'], session.get('user_email'))

    def test_sign_up_success_doesnt_authenticate_user(self):
        with self.app.test_client() as client:
            client.post(url_for('sign_up'), data=self.data)
            self.assertFalse(current_user.is_authenticated)
