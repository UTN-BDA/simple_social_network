from app import db
from app.models import Amistad

class AmistadRepository:
    

    @staticmethod
    def crear(amistad):
        db.session.add(amistad)
        db.session.commit()


    @staticmethod
    def buscar():
        amistades = db.session.query(Amistad).all()
        return amistades
    


    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Amistad).filter_by(id=id).first()


    @staticmethod
    def actualizar(amistad) -> Amistad:
        amistad_existente = db.session.merge(amistad)
        if not amistad_existente:
            return None
        return amistad_existente
    

    @staticmethod
    def borrar_por_id(id: int) -> Amistad:
        amistad = db.session.query(Amistad).filter_by(id=id).first()
        if not amistad:
            return None
        db.session.delete(amistad)
        db.session.commit()
        return amistad

