from app import db


class Seguidor(db.Model):
    __tablename__ = 'seguidores'

    # Llave primaria compuesta por dos llaves foráneas
    id_seguidor: int = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)
    id_seguido: int = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)

    # Restricción que evita que ambos ids sean idénticos
    __table_args__ = (
        db.CheckConstraint('id_seguidor != id_seguido', name='check_usuarios_diferentes'),
    )