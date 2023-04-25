from flask import jsonify, request
from models.producto import *


class Productocontroller():

    def consultar_productos(self):
        if request.method == 'GET':
            productos = Producto.query.all()
            if not productos:
                return jsonify({'message': 'no hay productos'})
            else:
                toProductos = [producto.getDatos() for producto in productos]
                return jsonify(toProductos)

    def insertar_producto(self):
        
        codigo = request.json["codigo"]
        nombre = request.json["nombre"]
        categoria = request.json["categoria"]
        subcategoria = request.json["subcategoria"]
        precio = request.json["precio"] 
        new_producto = Producto(codigo,nombre,categoria,subcategoria,precio)
        print(new_producto)

        db.session.add(new_producto)
        db.session.commit()
        return jsonify({
                'message':'Producto registrado con exito ',
                'status':'ok'
                })
    
    def consultar_producto_id(self):

        id = request.json["id"]
        c_producto = Producto.query.get(id)
        if not c_producto:
            return jsonify({'message': 'Producto not found'})
        else:
            return jsonify(c_producto.getDatos())