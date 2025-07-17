from app.repositories import PublicacionRepository
from app.models import Publicacion
from datetime import datetime


publicacion_repository = PublicacionRepository()


class PublicacionService:

    @staticmethod
    def crear(publicacion: Publicacion):
        # Agregar fecha actual
        publicacion.fecha = datetime.now()
        publicacion = PublicacionRepository.crear(publicacion)
        return publicacion

    
    # @staticmethod
    # def buscar_por_id(id: int) -> Publicacion:
    #     return PublicacionRepository.buscar_por_id(id)
    
    # @staticmethod
    # def buscar() -> list[Publicacion]:
    #     return PublicacionRepository.buscar()
    
    # @staticmethod
    # def actualizar(id: int, publicacion: Publicacion) -> Publicacion:
    #     publicacion_existente = PublicacionRepository.buscar_por_id(id)
    #     if not publicacion_existente:
    #         return None
    #     publicacion_existente.nombre = publicacion.nombre
    #     return publicacion_existente
    

    # @staticmethod
    # def borrar_por_id(id: int) -> Publicacion:
    #     publicacion = PublicacionRepository.borrar_por_id(id)
    #     if not publicacion:
    #         return None
    #     return publicacion