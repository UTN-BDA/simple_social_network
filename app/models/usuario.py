from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    # Atributos 
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nombre: str = db.Column(db.String(80), nullable = False)
    apellido: str = db.Column(db.String(80), nullable = False)
    edad: int = db.Column(db.Integer, nullable = False)
    correo: str = db.Column(db.String(80), nullable = False, unique = True)
    contraseña: str = db.Column(db.String(100), nullable = False, unique = True)

    # Relación N:1 con publicaciones
    publicaciones = db.relationship('Publicacion', uselist=True, back_populates='usuario')