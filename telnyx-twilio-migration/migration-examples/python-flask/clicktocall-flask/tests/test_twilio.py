import unittest

# Import the clicktocall module
try:
    from clicktocall.app import app as application
except ImportError:
    # Handle import issues during test discovery
    import sys
    sys.path.insert(0, '/home/telnyx-user/twilio-test-repos/clicktocall-flask')
    from clicktocall.app import app as application


def create_app():
    """Create a test app with mock config."""
    application.config['TELNYX_API_KEY'] = 'KEYexample'
    application.config['TELNYX_CALLER_ID'] = '+15558675309'
    application.config['TELNYX_CONNECTION_ID'] = 'conn-example'
    return application


class TeXMLTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()


class ClickToCallTests(TeXMLTest):
    def test_index(self):
        response = self.app.get('/')
        self.assertIn(response.status_code, [200, 302])

    def test_landing(self):
        response = self.app.get('/landing.html')
        self.assertIn(response.status_code, [200, 302])

    def test_outbound_texml(self):
        response = self.app.post('/outbound')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'</Response>', response.data)
        self.assertIn(b'text/xml', response.content_type.lower())


class NoCredentialsTests(unittest.TestCase):
    def setUp(self):
        app = create_app()
        if 'TELNYX_API_KEY' in app.config:
            del(app.config['TELNYX_API_KEY'])
        self.app = app.test_client()

    def test_call_without_telnyx_credentials(self):
        response = self.app.post('/call',
                                 data={'phoneNumber': '+15556667777'})

        # Should return 400 when credentials are missing
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
