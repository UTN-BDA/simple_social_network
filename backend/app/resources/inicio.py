from flask import Blueprint
from app.services import ResponseBuilder
from app.mapping import ResponseSchema

# Schemas
response_schema = ResponseSchema()

inicio = Blueprint('inicio', __name__)


@inicio.route('/', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    response_builder.add_message("hola mundo").add_status_code(200)
    return response_schema.dump(response_builder.build()),200

