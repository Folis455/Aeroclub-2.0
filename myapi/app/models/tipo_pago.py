from app import db

class TipoPago(db.Model):
    _tablename_ = 'TIPO_PAGO'
    id_tipo_pago = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(45), nullable=False, unique=True)
    observaciones = db.Column(db.Text)

    transacciones = db.relationship('Transacciones', back_populates='tipo_pago')

    def _init_(self, tipo, observaciones=None):
        self.tipo = tipo
        self.observaciones = observaciones