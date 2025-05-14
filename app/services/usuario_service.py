from app.repositories import UsuarioRepository

usuario_repository = UsuarioRepository()

class UsuarioService:
    
    def read(self):
        usuarios = usuario_repository.read()
        return usuarios