from unittest.mock import patch, MagicMock, PropertyMock

from ..base import BaseTestCase
from twofa.models import User


class ViewsTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.user = User(
            'test@example.com', 'fakepassword', 'test', 33, '611223344', 1234
        )

    def test_sign_up(self):
        # Arrange
        fake_authy_user = MagicMock()
        fake_authy_user.ok.return_value = True
        type(fake_authy_user).id = PropertyMock(return_value=1234)
        fake_client = MagicMock()
        fake_client.users.create.return_value = fake_authy_user

        # Act
        with patch('twofa.utils.get_authy_client', return_value=fake_client):
            resp = self.client.post(
                '/sign-up',
                data={
                    'name': 'test',
                    'email': 'test@example.com',
                    'password': 'fakepassword',
                    'country_code': 33,
                    'phone_number': '611223344',
                },
            )

        # Assert
        fake_client.users.create.assert_called()
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.location, 'http://localhost/account')

        self.assertEqual(self.user.full_name, 'test')
        self.assertEqual(self.user.country_code, 33)
        self.assertEqual(self.user.phone, '611223344')
