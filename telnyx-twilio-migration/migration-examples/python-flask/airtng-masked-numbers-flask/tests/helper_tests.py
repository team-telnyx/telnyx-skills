import unittest
from airtng_flask.view_helpers import redirect_to, view
from tests.base import BaseTestCase
from flask import redirect, url_for, render_template


class ViewHelperTests(BaseTestCase):
    def test_redirect_to_redirects_to_same_location_of_redirect(self):
        # assert
        assert redirect_to('home').location == redirect(url_for('home')).location

    # Ensures 'view' renders the same template that 'render_template'
    def test_view_renders_the_same_template_as_render_template(self):
        # assert
        assert view('home') == render_template('home.html')


if __name__ == '__main__':
    unittest.main()
