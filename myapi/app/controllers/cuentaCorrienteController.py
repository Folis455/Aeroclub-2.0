from app.models.cuenta_corriente import CuentaCorriente
from app import db
from flask import jsonify

# Una Cuenta Corriente no se deberá deshabilitar, a su vez tampoco se podrá crear, se inicializará con el valor de una transacción...

class cuentaCorrienteController:

    def _init_(self):
        pass
    
    def obtener_saldo_cuentas(cls):
        cuentas_corrientes = CuentaCorriente.query.all()
        saldos_usuarios = [{'usuario_id': cuenta.usuarios_id, 'saldo_cuenta': cuenta.saldo_cuenta} for cuenta in cuentas_corrientes]
        return jsonify(saldos_usuarios)

    def obtener_saldo(self, usuario_id):
            cuenta_corriente = CuentaCorriente.query.filter_by(usuarios_id=usuario_id).first()
            if cuenta_corriente:
                return cuenta_corriente.saldo_cuenta, True
            return False

    def actualizar_saldo(self, usuario_id, nuevo_saldo):
            cuenta_corriente = CuentaCorriente.query.filter_by(usuarios_id=usuario_id).first()
            if cuenta_corriente:
                cuenta_corriente.saldo_cuenta = nuevo_saldo
                db.session.commit()
                return True
            return False