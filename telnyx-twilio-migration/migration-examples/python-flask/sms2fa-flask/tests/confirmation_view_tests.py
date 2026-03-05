from .base import BaseTest
from flask import url_for
from flask.ext.login import current_user
import six
from mock import MagicMock
from sms2fa_flask import views
if six.PY3:
    from urllib.parse import urlparse
else:
    from urlparse import urlparse


class ConfirmationPageTest(BaseTest):

    def test_confirmation_page_fails_for_strangers(self):
        response = self.client.get(url_for('confirmation'))
        self.assertEquals(401, response.status_code)

    def test_confirmation_page_success_for_a_valid_session(self):
        views.send_confirmation_code = MagicMock(return_value='random_code')
        with self.app.test_client() as client:
            with client.session_transaction() as current_session:
                current_session['user_email'] = self.email
            response = client.get(url_for('confirmation'))
            self.assertEquals(200, response.status_code)

    def test_confirmation_page_shows_current_phone(self):
        views.send_confirmation_code = MagicMock(return_value='1234')
        with self.app.test_client() as client:
            with client.session_transaction() as current_session:
                current_session['user_email'] = self.email
            response = client.get(url_for('confirmation'))
        self.assertIn(self.default_user.international_phone_number,
                      response.data.decode('utf8'))

    def test_confirmation_page_authenticates_on_success(self):
        with self.app.test_client() as client:
            with client.session_transaction() as current_session:
                current_session['user_email'] = self.email
                current_session['verification_code'] = '1234'
            client.post(url_for('confirmation'),
                        data={'verification_code': '1234'})
            self.assertTrue(current_user.is_authenticated)

    def test_confirmation_page_doesnt_authenticates_on_failure(self):
        views.send_confirmation_code = MagicMock(return_value='1234')
        with self.app.test_client() as client:
            with client.session_transaction() as current_session:
                current_session['user_email'] = self.email
                current_session['verification_code'] = '1234'
            client.post(url_for('confirmation'),
                        data={'verification_code': 'wrong_one'})
            self.assertFalse(current_user.is_authenticated)

    def test_confirmation_page_redirect_to_secrets_page_on_success(self):
        with self.app.test_client() as client:
            with client.session_transaction() as current_session:
                current_session['user_email'] = self.email
                current_session['verification_code'] = '1234'
            response = client.post(url_for('confirmation'),
                                   data={'verification_code': '1234'})
        expected_path = url_for('secret_page')
        self.assertEquals(302, response.status_code)
        self.assertIn(expected_path, urlparse(response.location).path)
