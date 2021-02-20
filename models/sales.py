from main import db
from sqlalchemy import func

class Sales(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    inventoryId = db.Column(db.Integer, db.ForeignKey('inventories.id'), nullable=False)