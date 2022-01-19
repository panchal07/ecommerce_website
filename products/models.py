from shop import db
from datetime import datetime

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

def __repr__(self):
    return '<brand %r>' % self.name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)

def __repr__(self):
    return '<category %r>' % self.name


class Addproduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    colors = db.Column(db.Text, nullable=False)
    discription = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),
        nullable=False)
    brand = db.relationship('Brand',
        backref=db.backref('brands', lazy=True))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
        nullable=False)
    category = db.relationship('Category',
        backref=db.backref('posts', lazy=True))

    image_1 = db.Column(db.String(150), nullable=False, default='image1.jpg')
    image_2 = db.Column(db.String(150), nullable=False, default='image2.jpg')
    image_3 = db.Column(db.String(150), nullable=False, default='image3.jpg')

    def __repr__(self):
        return '<Addproducts %r>' % self.name



db.create_all()