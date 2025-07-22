from app.repositories import PublicacionRepository
from app.models import Publicacion
from app.services import ImageHandler, SeguidorService
from datetime import datetime
from typing import List


publicacion_repository = PublicacionRepository()
image_handler = ImageHandler()
seguidor_service = SeguidorService()

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
    
    @staticmethod
    def ultimas_publicaciones_por_usuario(id_usuario: int):
        publicaciones = PublicacionRepository.ultimas_publicaciones_por_usuario(id_usuario)
        return publicaciones

    @staticmethod
    def nuevas_publicaciones(id_usuario: int):
        seguidos = seguidor_service.seguidos(id_usuario)
        publicaciones = []
        for seguido in seguidos:
            publicaciones.extend(PublicacionService.ultimas_publicaciones_por_usuario(seguido))
        return publicaciones
    
 