from enum import unique
from utils.db import db


class Venta(db.Model):
    __tablename__ = 'venta'
    id = db.Column(db.Integer, primary_key=True)
    idcliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    idproducto = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    cantidad = db.Column(db.Integer, unique=True,nullable=False)
    total = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.TIMESTAMP, nullable=True)
    
  

    def __init__(self,  idcliente, idproducto, cantidad, total, fecha):
        self.idcliente = idcliente
        self.idproducto = idproducto
        self.cantidad = cantidad
        self.total = total
        self.fecha = fecha
        

    def getDatos(self):
        return {
            'id': self.id,
            'idcliente': self.idcliente,
            'idproducto': self.idproducto,
            'cantidad': self.cantidad,
            'total': self.total,
            'fecha': self.fecha
        }