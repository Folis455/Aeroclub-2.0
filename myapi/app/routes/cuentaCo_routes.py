from flask import Blueprint, request, jsonify
from app.models.cuenta_corriente import CuentaCorriente
from app.controllers.cuentaCorrienteController import cuentaCorrienteController
from app.controllers.usuarios import UsuariosController
from app.utils.Security import Security

cuenta_corriente_bp = Blueprint('cuenta_corriente', __name__)

@cuenta_corriente_bp.route('/', methods=['GET'])
def obtener_saldo_cuentas():
    
    has_access = Security.verify_token(request.headers)

    if has_access:
        try:
            cuenta_corriente_controller = cuentaCorrienteController()
            saldos = cuenta_corriente_controller.obtener_saldo_cuentas()
            return saldos, 200
        except Exception as ex:
            print(ex)
            return jsonify({'message': 'Ocurrió un error', 'success': False}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401  

@cuenta_corriente_bp.route('/<usuario_id>', methods=['GET'])
def get_cuenta_corriente(usuario_id):

    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            cuenta_corriente = CuentaCorriente.query.filter_by(usuarios_id=usuario_id).first()
            if cuenta_corriente:
                return jsonify({'saldo_cuenta': cuenta_corriente.saldo_cuenta}), 200
            else:
                return jsonify({'message': 'Cuenta corriente no encontrada'}), 404
    
        except Exception as ex:
            print(ex)
            return jsonify({'message': 'Ocurrió un error', 'success': False}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401  

@cuenta_corriente_bp.route('/<usuario_id>', methods=['POST'])
def create_cuenta_corriente(usuario_id):
    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            data = request.get_json()
            cuenta_corriente = CuentaCorriente()
            respuesta = cuenta_corriente.crear_cuenta_corriente(usuario_id, data)

            if respuesta:
                return jsonify({'message': 'Cuenta corriente creada correctamente'}), 201
            else:
                return jsonify({'message': 'Error al crear la cuenta corriente'}), 400

        except Exception as ex:
            print(ex)
            return jsonify({'message': 'Ocurrió un error', 'success': False}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401  
    
@cuenta_corriente_bp.route('/<usuario_id>', methods=['PATCH'])
def update_cuenta_corriente(usuario_id):

    has_access = Security.verify_token(request.headers)
    if has_access:
        try:
            data = request.get_json()
            cuenta_controller = cuentaCorrienteController()
            respuesta = cuenta_controller.actualizar_saldo(usuario_id, data.get('saldo_cuenta'))
            if respuesta == True:
                return jsonify({'mensaje': 'Saldo de la cuenta corriente actualizado correctamente'}), 200
            else:
                return jsonify({'mensaje': 'Cuenta corriente no encontrada'}), 404

        except Exception as ex:
            print(ex)
            return jsonify({'message': 'Ocurrió un error', 'success': False}), 500
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401  
