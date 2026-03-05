import os
import sys
import unittest


def test():
    """Run the unit tests."""
    os.environ['FLASK_ENV'] = 'testing'
    tests = unittest.TestLoader().discover('.', pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == "__main__":
    test()
