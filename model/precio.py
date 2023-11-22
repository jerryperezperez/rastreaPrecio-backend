# from app import db
from sqlalchemy import ForeignKey
from config import db


class Precio(db.Model):
    __tablename__ = "precio"
    id = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, ForeignKey("articulo.id"))
    fecha = db.Column(db.Date, nullable=False)
    precio = db.Column(db.Double, nullable=False)
