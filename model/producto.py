# from app import db
from config import db


class Articulo(db.Model):
    __tablename__ = "articulo"
    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(500), nullable=False, unique=True)
    url = db.Column(db.String(800), nullable=False, unique=True)
    store = db.Column(db.String(255), nullable=False)
    precios = db.relationship('Precio', backref='articulo', lazy=True)
