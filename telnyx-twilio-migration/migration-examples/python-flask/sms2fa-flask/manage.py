from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_migrate import upgrade as upgrade_database
from sms2fa_flask import db, prepare_app

app = prepare_app(environment='development')
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import sys
    import unittest
    prepare_app(environment='test')
    upgrade_database()
    tests = unittest.TestLoader().discover('.', pattern="*_tests.py")
    test_result = unittest.TextTestRunner(verbosity=2).run(tests)

    if not test_result.wasSuccessful():
        sys.exit(1)


@manager.command
def dbseed():
    pass

if __name__ == "__main__":
    manager.run()
