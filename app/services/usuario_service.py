from app.models import Usuario
from app.repositories.usuario_repository import UsuarioRepository


usuario_repository = UsuarioRepository()


class UsuarioService:
    @staticmethod
    def crear(usuario: Usuario) -> Usuario:
        usuario = UsuarioRepository.crear(usuario)
        return usuario

    
    @staticmethod
    def buscar_por_id(id: int) -> Usuario:
        return UsuarioRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar() -> list[Usuario]:
        return UsuarioRepository.buscar()
    
    @staticmethod
    def actualizar(id: int, usuario: Usuario) -> Usuario:
        usuario_existente = UsuarioRepository.buscar_por_id(id)
        if not usuario_existente:
            return None
        usuario_existente.nombre = usuario.nombre
        return usuario_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Usuario:
        usuario = UsuarioRepository.borrar_por_id(id)
        if not usuario:
            return None
        return usuario