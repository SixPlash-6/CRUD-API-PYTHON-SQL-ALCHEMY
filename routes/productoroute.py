from flask import Blueprint
from flask_cors import cross_origin

from controllers.productocontroller import Productocontroller

productos = Blueprint('productos', __name__)

con_producto = Productocontroller()

cross_origin()

# Listar todo
productos.route('/consultar_productos',
                methods=['GET'])(con_producto.consultar_productos)
# Buscar producto por id
productos.route('/consultar_producto_id',
                methods=['GET'])(con_producto.consultar_producto_id)
# Insertar producto
productos.route('/insertar_producto',
                methods=['POST'])(con_producto.insertar_producto)
# Editar
productos.route('/editar_producto_id/<id>',
                methods=['PUT'])(con_producto.editar_producto)
# Eliminar
productos.route('/eliminar_producto/<id>',
                methods=['DELETE'])(con_producto.eliminar_producto)
