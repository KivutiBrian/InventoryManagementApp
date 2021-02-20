from main import db
from sqlalchemy import func

class Inventory(db.Model):
    __tablename__ = 'inventories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    itype = db.Column(db.String, nullable=False)
    bp = db.Column(db.Float, nullable=False)
    sp = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())

    stock = db.relationship('Stock', backref='inventory', lazy=True)
    sales = db.relationship('Sales', backref='inventory', lazy=True)