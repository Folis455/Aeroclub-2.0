from app import db
from sqlalchemy import ForeignKey

class Transacciones(db.Model):
    _tablename_ = 'TRANSACCIONES'
    id_transacciones = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    motivo = db.Column(db.Text)

    cuenta_corriente = db.relationship('CuentaCorriente', back_populates='transacciones')

    def _init_(self, monto, fecha, motivo, cuenta_corriente_id):
        self.monto = monto
        self.fecha = fecha
        self.motivo = motivo
        self.cuenta_corriente_id = cuenta_corriente_id