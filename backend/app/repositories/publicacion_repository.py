from app import db
from app.models import Amistad

class PublicacionRepository:

    @staticmethod
    def crear(publicacion):
        db.session.add(publicacion)
        db.session.commit()


    @staticmethod
    def buscar():
        publicaciones = db.session.query(Amistad).all()
        return publicaciones
    


    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Amistad).filter_by(id=id).first()


    @staticmethod
    def actualizar(publicacion) -> Amistad:
        publicacion_existente = db.session.merge(publicacion)
        if not publicacion_existente:
            return None
        return publicacion_existente
    

    @staticmethod
    def borrar_por_id(id: int) -> Amistad:
        publicacion = db.session.query(Amistad).filter_by(id=id).first()
        if not publicacion:
            return None
        db.session.delete(publicacion)
        db.session.commit()
        return publicacion

