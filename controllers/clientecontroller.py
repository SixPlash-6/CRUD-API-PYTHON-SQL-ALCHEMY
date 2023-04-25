from flask import jsonify, request
from models.cliente import *


class Clientecontroller():

    def consultar_clientes(self):
        if request.method == 'GET':
            clientes = Cliente.query.all()
            if not clientes:
                return jsonify({'message': 'no hay clientes'})
            else:
                toClientes = [cliente.getDatos() for cliente in clientes]
                return jsonify(toClientes)

    def insertar_cliente(self):
        
        nombre = request.json["nombre"]
        apellido = request.json["apellido"]
        documento = request.json["documento"]
        correo = request.json["correo"]
        telefono = request.json["telefono"]    
        new_cliente = Cliente(id,nombre,apellido,documento,correo,telefono)
        db.session.add(new_cliente)
        db.session.commit()
        return jsonify({
                'message':'Cliente registrado con exito',
                'status':'ok'
                })
    
    def consultar_cliente_id(self):

        id = request.json["id"]
        c_Cliente = Cliente.query.get(id)
        if not c_Cliente:
            return jsonify({'message': 'Cliente not found'})
        else:
            return jsonify(c_Cliente.getDatos())


    def consultar_cliente_cedula(self):

        v_cedula = request.json["documento"]
        print(v_cedula)
        c_Cliente = Cliente.query.filter_by(documento=v_cedula).all()
        if not c_Cliente:
            return jsonify({'message': 'Cliente not found'})
        else:
            toClientes = [cliente.getDatos() for cliente in c_Cliente]
            return jsonify(toClientes)
            


    def editar_cliente(self):
        id = request.json["id"]
        c_cliente = Cliente.query.get(id)
        if not c_cliente:
            return jsonify({'message': 'cliente no encontrado'})
        else:
            c_cliente.nombre = request.json["nombre"]
            c_cliente.apellido = request.json["apellido"]
            c_cliente.documento = request.json["documento"]
            c_cliente.correo = request.json["correo"]
            c_cliente.telefono = request.json["telefono"]

            db.session.commit()
            return jsonify({'message': 'cliente actualizado con exito'})


    def eliminar_cliente(self):
        id = request.json["id"]
        c_Cliente = Cliente.query.get(id)
        if not c_Cliente:
            return jsonify({'message': 'Cliente no encontrado'})
        else:
            db.session.delete(c_Cliente)
            db.session.commit()
            return jsonify({'message': 'Cliente eliminado con exito'})