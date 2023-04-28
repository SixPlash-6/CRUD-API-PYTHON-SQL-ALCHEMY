from enum import unique
from utils.db import db


class Producto(db.Model):
    __tablename__ = 'producto'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(20), unique=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    subcategoria = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Integer, nullable=True)
    # venta = db.relationship('Venta', backref='producto', lazy=True)

    def __init__(self, codigo, nombre, categoria, subcategoria, precio):

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.subcategoria = subcategoria
        self.precio = precio

    def getDatos(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'nombre': self.nombre,
            'categoria': self.categoria,
            'subcategoria': self.subcategoria,
            'precio': self.precio
        }
