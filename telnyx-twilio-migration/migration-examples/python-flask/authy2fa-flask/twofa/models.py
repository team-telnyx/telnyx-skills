from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .utils import authy_user_has_app, send_authy_one_touch_request


class User(db.Model):
    """
    Represents a single user in the system.
    """

    __tablename__ = 'users'

    AUTHY_STATUSES = ('unverified', 'onetouch', 'sms', 'token', 'approved', 'denied')

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    full_name = db.Column(db.String(256))
    country_code = db.Column(db.Integer)
    phone = db.Column(db.String(30))
    authy_id = db.Column(db.Integer)
    authy_status = db.Column(db.Enum(*AUTHY_STATUSES, name='authy_statuses'))

    def __init__(
        self,
        email,
        password,
        full_name,
        country_code,
        phone,
        authy_id,
        authy_status='approved',
    ):
        self.email = email
        self.password = password
        self.full_name = full_name
        self.country_code = country_code
        self.phone = phone
        self.authy_id = authy_id
        self.authy_status = authy_status

    def __repr__(self):
        return '<User %r>' % self.email

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @property
    def has_authy_app(self):
        return authy_user_has_app(self.authy_id)

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def send_one_touch_request(self):
        return send_authy_one_touch_request(self.authy_id, self.email)
