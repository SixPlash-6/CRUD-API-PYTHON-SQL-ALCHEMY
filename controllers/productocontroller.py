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
        new_producto = Producto(
            codigo, nombre, categoria, subcategoria, precio)
        print(new_producto)

        db.session.add(new_producto)
        db.session.commit()
        return jsonify({
            'message': 'Producto registrado con exito ',
            'status': 'ok'
        })

    def consultar_producto_id(self):
        id = request.json["id"]
        c_producto = Producto.query.get(id)
        if not c_producto:
            return jsonify({'message': 'Producto not found'})
        else:
            return jsonify(c_producto.getDatos())

    def editar_producto(self, id):
        c_producto = Producto.query.get(id)
        if not c_producto:
            return jsonify({'message': 'Producto no encontrado'})
        else:
            c_producto.codigo = request.json["codigo"]
            c_producto.nombre = request.json["nombre"]
            c_producto.categoria = request.json["categoria"]
            c_producto.subcategoria = request.json["subcategoria"]
            c_producto.precio = request.json["precio"]

            db.session.commit()
            return jsonify({'message': 'producto ' f"{id}" ' actualizado con exito',
                            "status": "ok"})

    def eliminar_producto(self, id):
        c_Producto = Producto.query.get(id)
        if not c_Producto:
            return jsonify({'message': 'Producto no encontrado'})
        else:
            db.session.delete(c_Producto)
            db.session.commit()
            return jsonify({'message': "Prodcuto " f"{id}" " eliminado con exito",
                            "status": "ok"})
