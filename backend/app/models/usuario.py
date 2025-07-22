from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    # Atributos 
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nombre: str = db.Column(db.String(80), nullable = False)
    apellido: str = db.Column(db.String(80), nullable = False)
    edad: int = db.Column(db.Integer, nullable = False)
    nacimiento: str = db.Column(db.Date, nullable = False)
    correo: str = db.Column(db.String(80), nullable = False, unique = True)
    contraseña: str = db.Column(db.String(200), nullable = False)
    imagen: str = db.Column(db.String(200), nullable = False)

    __table_args__ = (
        db.Index('idx_usuario_correo', 'correo'), 
    )
