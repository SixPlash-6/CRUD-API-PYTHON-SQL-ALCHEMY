from flask import jsonify, request
from models.venta import *


class Ventacontroller():

    def consultar_ventas(self):
        if request.method == 'GET':
            ventas = Venta.query.all()
            if not ventas:
                return jsonify({'message': 'no hay ventas'})
            else:
                toVentas = [venta.getDatos() for venta in ventas]
                return jsonify(toVentas)

    def insertar_cliente(self):
        
        idcliente = request.json["idcliente"]
        idproducto = request.json["idproducto"]
        cantidad = request.json["cantidad"]
        total = request.json["total"]
        fehca = request.json["fehca"]    
        new_Venta = Venta(idcliente,idproducto,cantidad,total,fehca)
        db.session.add(new_Venta)
        db.session.commit()
        return jsonify({
                'message':'Venta registrado con exito',
                'status':'ok'
                })
    
    def consultar_venta_id(self):

        id = request.json["id"]
        c_venta = Venta.query.get(id)
        if not c_venta:
            return jsonify({'message': 'Producto not found'})
        else:
            return jsonify(c_venta.getDatos())
            