from flask import Flask, jsonify, request, Blueprint
from flask_cors import  cross_origin

from controllers.ventacontroller import *

ventas = Blueprint('ventas', __name__)

con_venta = Ventacontroller()

@ventas.route('/consultar_ventas', methods=['GET'])
@cross_origin() 
def consultar_ventas():
    return con_venta.consultar_ventas()


@ventas.route('/insertar_venta', methods=['POST'])
@cross_origin() 
def insertar_venta():
    return con_venta.insertar_venta()


@ventas.route('/consultar_venta_id', methods=['GET'])
@cross_origin() 
def consultar_venta_id():
    return con_venta.consultar_venta_id()