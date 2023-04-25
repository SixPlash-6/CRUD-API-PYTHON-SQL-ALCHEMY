from flask import Flask, jsonify, request, Blueprint
from flask_cors import  cross_origin

from controllers.productocontroller import *

productos = Blueprint('productos', __name__)

con_producto= Productocontroller()

@productos.route('/consultar_productos', methods=['GET'])
@cross_origin() 
def consultar_productos():
    return con_producto.consultar_productos()


@productos.route('/insertar_producto', methods=['POST'])
@cross_origin() 
def insertar_producto():
    return con_producto.insertar_producto()


@productos.route('/consultar_producto_id', methods=['GET'])
@cross_origin() 
def consultar_producto_id():
    return con_producto.consultar_producto_id()