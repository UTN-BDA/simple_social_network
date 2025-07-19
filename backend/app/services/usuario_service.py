from app.models import Usuario
from app.repositories import UsuarioRepository
from app.services import Hash, ImageHandler
from datetime import date

usuario_repository = UsuarioRepository()
hash_service = Hash()
image_handler = ImageHandler()

class UsuarioService:
    @staticmethod
    def crear(usuario: Usuario, imagen) -> Usuario:
        # Hashear contraseña
        hash_contraseña = hash_service.generar_contraseña(usuario.contraseña)
        usuario.contraseña = hash_contraseña

        # Transformar fecha de nacimiento en edad
        hoy = date.today()
        nacimiento = usuario.nacimiento
        edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
        usuario.edad = edad

        # Manejo de imagenes
        usuario.imagen = image_handler.perfil(imagen)

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
    def verificar_usuario(correo: str, contraseña: str) -> Usuario:
        usuario = UsuarioRepository.buscar_por_correo(correo)
        if usuario:
            if hash_service.verificar_contraseña(hash=usuario.contraseña, contraseña=contraseña):
                return usuario
            else:
                return None
        else:
            return None
        