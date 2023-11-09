from app import db

class Usuarios(db.Model):
    __tablename__ = 'USUARIOS'
    id_usuarios = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    telefono = db.Column(db.Integer, nullable=False)
    dni = db.Column(db.Integer, nullable=False, unique=True)
    fecha_alta = db.Column(db.Date, nullable=False)
    fecha_baja = db.Column(db.Date, nullable=False)
    direccion = db.Column(db.String(100))
    foto_perfil = db.Column(db.Text)
    estado_hab_des = db.Column(db.Integer, nullable=False)

    roles = db.relationship("Roles", secondary="USUARIOS_tiene_ROLES", back_populates="usuarios")
    cuenta_corriente = db.relationship("CuentaCorriente", back_populates="usuarios")

    def __init__(self, id_usuarios ,nombre, apellido, email, telefono, dni, fecha_alta, fecha_baja, direccion, foto_perfil, estado_hab_des):
        self.id_usuarios = id_usuarios
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.dni = dni
        self.fecha_alta = fecha_alta
        self.fecha_baja = fecha_baja
        self.direccion = direccion
        self.foto_perfil = foto_perfil
        self.estado_hab_des = estado_hab_des

