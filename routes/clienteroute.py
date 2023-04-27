from flask import Flask, jsonify, request, Blueprint
from flask_cors import cross_origin

from controllers.clientecontroller import *

clientes = Blueprint('clientes', __name__)

con_cliente = Clientecontroller()


@clientes.route('/consultar_clientes', methods=['GET'])
@cross_origin()
def consultar_clientes():
    return con_cliente.consultar_clientes()


@clientes.route('/insertar_venta', methods=['POST'])
@cross_origin()
def insertar_venta():
    return con_cliente.insertar_cliente()


@clientes.route('/consultar_cliente_id', methods=['GET'])
@cross_origin()
def consultar_cliente_id():
    return con_cliente.consultar_cliente_id()


@clientes.route('/consultar_cliente_cedula', methods=['GET'])
@cross_origin()
def consultar_cliente_cedula():
    return con_cliente.consultar_cliente_cedula()


@clientes.route('/eliminar_cliente', methods=['DELETE'])
@cross_origin()
def eliminar_cliente():
    return con_cliente.eliminar_cliente()


@clientes.route('/insertar_cliente', methods=['POST'])
@cross_origin()
def insertar_cliente():
    return con_cliente.insertar_cliente()
