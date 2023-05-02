from flask import Blueprint
from flask_cors import cross_origin

from controllers.ventacontroller import Ventacontroller

ventas = Blueprint('ventas', __name__)

con_venta = Ventacontroller()

cross_origin()

ventas.route('/consultar_ventas',
             methods=['GET'])(con_venta.consultar_ventas)


ventas.route('/insertar_venta',
             methods=['POST'])(con_venta.insertar_venta)

ventas.route('/consultar_venta_id',
             methods=['GET'])(con_venta.consultar_venta_id)
