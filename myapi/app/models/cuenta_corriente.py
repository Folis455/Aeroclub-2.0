from app import db
from sqlalchemy import ForeignKey

class CuentaCorriente(db.Model):
    _tablename_ = 'CUENTA_CORRIENTE'
    id_cuenta_corriente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    saldo_cuenta = db.Column(db.Float, nullable=False)
    usuarios_id = db.Column(db.Integer, ForeignKey('USUARIOS.id_usuarios'), nullable=False)
    # movimientos_id = db.Column(db.Integer, ForeignKey('Transacciones.id_transacciones'))

    usuarios = db.relationship('Usuarios', back_populates='cuenta_corriente')


    def _init_(self, saldo_cuenta, usuarios_id, movimientos_id=None):
        self.saldo_cuenta = saldo_cuenta
        self.usuarios_id = usuarios_id
        self.movimientos_id = movimientos_id
