from flask import Blueprint
from flask_cors import cross_origin

from controllers.clientecontroller import Clientecontroller

clientes = Blueprint('clientes', __name__)

con_cliente = Clientecontroller()


cross_origin()

# Listar todos
clientes.route('/consultar_clientes',
               methods=['GET'])(con_cliente.consultar_clientes)
# Buscar por id
clientes.route('/consultar_cliente_id',
               methods=['GET'])(con_cliente.consultar_cliente_id)
# Buscar por cedula
clientes.route('/consultar_cliente_cedula',
               methods=['GET'])(con_cliente.consultar_cliente_cedula)
# Insertar
clientes.route('/insertar_cliente',
               methods=['POST'])(con_cliente.insertar_cliente)
# # Editar
clientes.route('/editar_cliente_id/<id>',
               methods=['PUT'])(con_cliente.editar_cliente)
# Eliminar
clientes.route('/eliminar_cliente/<id>',
               methods=['DELETE'])(con_cliente.eliminar_cliente)

# clientes.route('/insertar_venta',
#                methods=['POST'])(Clientecontroller.insertar_venta)
