from shop import db
from datetime import datetime


class Register1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200), unique=False)
    country = db.Column(db.String(50), unique=False)
    state = db.Column(db.String(50), unique=False)
    contact = db.Column(db.String(50), unique=False)
    address = db.Column(db.String(50), unique=False)
    zipcode = db.Column(db.String(50), unique=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return'<Register %r>' % self.name


db.create_all()
