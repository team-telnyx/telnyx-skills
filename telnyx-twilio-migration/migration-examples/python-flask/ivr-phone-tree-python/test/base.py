from ivr_phone_tree_python import app, configure_app
from flask_testing import TestCase


class BaseTestCase(TestCase):
    render_templates = False

    def create_app(self):
        configure_app(app, 'test')
        return app
