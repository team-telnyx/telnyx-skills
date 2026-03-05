from airtng_flask.models import app_db

db = app_db()


class VacationProperty(db.Model):
    __tablename__ = "vacation_properties"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)

    host_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    host = db.relationship("User", back_populates="vacation_properties")
    reservations = db.relationship("Reservation", back_populates="vacation_property")

    def __init__(self, description, image_url, host):
        self.description = description
        self.image_url = image_url
        self.host = host

    def __repr__(self):
        return '<VacationProperty {0} {1}>'.format(self.id, self.description)
