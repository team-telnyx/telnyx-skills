from flask import Flask
from flask_bootstrap import Bootstrap

from .config import config_classes
from .database import db, migrate

app = Flask(__name__, instance_relative_config=True)
# load the instance config, if it exists, when not testing
env = app.config.get("ENV")
app.config.from_object(config_classes[env])

Bootstrap(app)

db.init_app(app)
migrate.init_app(app, db)

import twofa.models  # noqa E402

from .auth import auth as auth_blueprint  # noqa E402
from .main import main as main_blueprint  # noqa E402

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
