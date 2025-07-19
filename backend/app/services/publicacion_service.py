from app.repositories import PublicacionRepository
from app.models import Publicacion
from app.services import ImageHandler
from datetime import datetime
from typing import List


publicacion_repository = PublicacionRepository()
image_handler = ImageHandler()

class PublicacionService:

    @staticmethod
    def crear(publicacion: Publicacion, imagenes: List):
        # Agregar fecha actual
        publicacion.fecha = datetime.now() 
        # Manejo de imagenes
        publicacion.imagenes = image_handler.publicacion(imagenes)
        publicacion = PublicacionRepository.crear(publicacion)
        return publicacion
    
    @staticmethod
    def buscar_por_usuario(id_usuario: int):
        publicaciones = PublicacionRepository.buscar_por_usuario(id_usuario)
        return publicaciones

    
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