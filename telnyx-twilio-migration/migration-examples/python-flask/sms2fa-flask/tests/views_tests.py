from .base import BaseTest


class RootTest(BaseTest):

    def test_root(self):
        response = self.client.get('/')
        self.assertEquals(200, response.status_code)
        self.assertIn('can be tricky', response.data.decode('utf8'))

    def test_secret_page_without_auth(self):
        response = self.client.get('/secret-page')
        self.assertEquals(401, response.status_code)
