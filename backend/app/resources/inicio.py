from flask import Blueprint, jsonify

inicio = Blueprint('inicio', __name__)


@inicio.route('/', methods=['GET'])
def index():
    return "Hola mundo"

# @inicio.route('/prueba', methods=['GET'])
# def prueba():
#     return jsonify({"mensaje": "Hola desde Flask"})