from marshmallow import Schema, fields, validate, validates, ValidationError, post_load
import re
from app.models import Seguidor
class SeguidorSchema(Schema):

    id_seguidor = fields.Integer(required=True)
    id_seguido = fields.Integer(required=True)

    @post_load 
    def crear_Usuario(self, data, **kwargs):
            return Seguidor(**data)

    
    