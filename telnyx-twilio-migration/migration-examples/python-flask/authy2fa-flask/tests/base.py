from unittest import TestCase

from twofa import app, db


class BaseTestCase(TestCase):
    render_templates = False

    def setUp(self):
        self.client = app.test_client()
        app.app_context().push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
