from flask import Blueprint

inicio = Blueprint('inicio', __name__)


@inicio.route('/', methods=['GET'])
def index():
    return "Hola mundo"

