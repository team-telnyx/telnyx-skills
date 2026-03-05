from flask_testing import TestCase

from airtng_flask import app


class BaseTestCase(TestCase):
    render_templates = False

    def create_app(self):
        return app
