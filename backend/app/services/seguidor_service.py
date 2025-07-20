from app.models import Seguidor, Usuario
from app.repositories import SeguidorRepository
from typing import List


seguidor_repository = SeguidorRepository()


class SeguidorService:

    @staticmethod
    def crear(seguidor: Seguidor):
        return seguidor_repository.crear(seguidor) 
    
    @staticmethod
    def seguidos(id_seguidor: int) -> List[int]:
        seguidos = seguidor_repository.obtener_seguidos_por_usuario(id_seguidor) 
        return seguidos
    # @staticmethod
    # def buscar_por_id(id: int) -> Amistad:
    #     return AmistadRepository.buscar_por_id(id)
    
    # @staticmethod
    # def buscar() -> list[Amistad]:
    #     return AmistadRepository.buscar()
    
    # @staticmethod
    # def actualizar(id: int, amistad: Amistad) -> Amistad:
    #     amistad_existente = AmistadRepository.buscar_por_id(id)
    #     if not amistad_existente:
    #         return None
    #     amistad_existente.nombre = amistad.nombre
    #     return amistad_existente
    

    # @staticmethod
    # def borrar_por_id(id: int) -> Amistad:
    #     amistad = AmistadRepository.borrar_por_id(id)
    #     if not amistad:
    #         return None
    #     return amistad