from twofa import db
from twofa.models import User

from ..base import BaseTestCase


class ViewsTestCase(BaseTestCase):
    def test_home(self):
        # Act
        resp = self.client.get('/')

        # Assert
        self.assertEqual(resp.status_code, 200)

    def test_account_as_anonymous(self):
        # Act
        resp = self.client.get('/account')

        # Assert
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.location, 'http://localhost/login')

    def test_account_as_logged_in(self):
        # Arrange
        user = User(
            'example@example.com',
            'fakepassword',
            'Alice',
            33,
            600112233,
            123,
            authy_status='unverified',
        )
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        with self.client.session_transaction() as sess:
            sess['user_id'] = user.id

        # Act
        resp = self.client.get('/account')

        # Assert
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.location, 'http://localhost/login')

    def test_account_as_verified(self):
        # Arrange
        user = User(
            'example@example.com',
            'fakepassword',
            'Alice',
            33,
            600112233,
            123,
            authy_status='approved',
        )
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        with self.client.session_transaction() as sess:
            sess['user_id'] = user.id

        # Act
        resp = self.client.get('/account')

        # Assert
        self.assertEqual(resp.status_code, 200)
