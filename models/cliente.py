from enum import unique
from utils.db import db


class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    documento = db.Column(db.String(20), unique=True, nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(20), nullable=True)
    venta = db.relationship('Venta', backref='cliente', lazy=True)

    def __init__(self, id, nombre, apellido, documento, correo, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.correo = correo
        self.telefono = telefono

    def getDatos(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'documento': self.documento,
            'correo': self.correo,
            'telefono': self.telefono
        }
