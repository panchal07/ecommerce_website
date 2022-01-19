from shop import db

class User1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    profile = db.Column(db.String(120), unique=False, nullable=False, default='img.jpg')

    def __repr__(self):
        return '<User1 %r>' % self.username


db.create_all()
