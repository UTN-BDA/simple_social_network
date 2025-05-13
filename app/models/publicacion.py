from app import db

class Publicacion(db.Model):
    __tablename__ = 'publicaciones'

    # Atributos 
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    fecha: str = db.Column(db.DateTime, nullable = False)
    contenido: str = db.Column(db.String(100), nullable = False) # ID nosql

    # LLave foránea a usuario
    id_usuario: int = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    # Relación 1:N con usuario
    usuario = db.relationship('Usuario', uselist=False, back_populates='publicaciones')
    