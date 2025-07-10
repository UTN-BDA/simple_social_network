from app.models import Usuario
from app.repositories import UsuarioRepository
from app.services import Hash

usuario_repository = UsuarioRepository()
hash_service = Hash()

class UsuarioService:
    @staticmethod
    def crear(usuario: Usuario) -> Usuario:
        hash_contraseña = hash_service.generar_contraseña(usuario.contraseña)
        usuario.contraseña = hash_contraseña
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
    
    @staticmethod
    def buscar_por_correo(correo: str) -> Usuario:
        return UsuarioRepository.buscar_por_correo(correo)


    @staticmethod
    def verificar_usuario(correo: str, contraseña: str):
        usuario = UsuarioRepository.buscar_por_correo(correo)
        if usuario:
            if hash_service.verificar_contraseña(hash=usuario.contraseña, contraseña=contraseña):
                return {
                    "success": True,
                    "data": usuario,
                    "message": "Inicio de sesión exitoso"
                }
            else:
                return {
                    "success": False,
                    "data": None,
                    "message": "La contraseña es inválida"
                }
        else:
            return {
                "success": False,
                "data": None,
                "message": "No se encontró un usuario asociado al correo"
            }
        