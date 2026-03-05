from airtng_flask.models import app_db
from airtng_flask.models import bcrypt

db = app_db()
bcrypt = bcrypt()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    area_code = db.Column(db.String, nullable=False)

    reservations = db.relationship("Reservation", back_populates="guest")
    vacation_properties = db.relationship("VacationProperty", back_populates="host")

    def __init__(self, name, email, password, phone_number, area_code):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.phone_number = phone_number
        self.area_code = area_code

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    # Python 3

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<User %r>' % (self.name)
