from app import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'

    # Atributos 
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nombres: str = db.Column(db.String(80), nullable = False)
    edad: int = db.Column(db.String(100), nullable = False)


