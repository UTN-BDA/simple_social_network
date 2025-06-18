from app.models import Amistad
from app.repositories.amistad_respository import AmistadRepository


amistad_repository = AmistadRepository()


class AmistadService:

    @staticmethod
    def crear(amistad : Amistad):
        AmistadRepository.crear(amistad)

    
    @staticmethod
    def buscar_por_id(id: int) -> Amistad:
        return AmistadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar() -> list[Amistad]:
        return AmistadRepository.buscar()
    
    @staticmethod
    def actualizar(id: int, amistad: Amistad) -> Amistad:
        amistad_existente = AmistadRepository.buscar_por_id(id)
        if not amistad_existente:
            return None
        amistad_existente.nombre = amistad.nombre
        return amistad_existente
    

    @staticmethod
    def borrar_por_id(id: int) -> Amistad:
        amistad = AmistadRepository.borrar_por_id(id)
        if not amistad:
            return None
        return amistad