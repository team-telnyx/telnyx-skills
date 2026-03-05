#!/usr/bin/env python
"""Management script for the IVR Phone Tree application."""

import sys
import unittest

from ivr_phone_tree_python import app


def run_tests():
    """Run the unit tests."""
    tests = unittest.TestLoader().discover('.', pattern="*_tests.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if not result.wasSuccessful():
        sys.exit(1)


def run_server():
    """Run the development server."""
    app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        run_tests()
    else:
        run_server()
