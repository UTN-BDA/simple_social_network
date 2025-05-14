from flask import Blueprint
from app.services import UsuarioService


usuario = Blueprint('usuario', __name__)


usuario_service = UsuarioService()

# Obtener lista de usuarios
@usuario.route('/', methods =['GET'])
def index ():
    usuarios = usuario_service.read()
    return usuarios, 200

