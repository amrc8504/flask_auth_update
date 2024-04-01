from . import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(15))
    user_name = db.Column(db.String(20))
    cart = relationship("CartItem", backref="user", cascade="all, delete-orphan")

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(100))  
    name = db.Column(db.String(100))
    description = db.Column(db.String(500))  
    price = db.Column(db.Float) 

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', '{self.price}')"

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    quantity = db.Column(db.Integer, default=1)
    product = relationship("Product")
