from marshmallow import Schema, fields, validate, validates, ValidationError
import re

class LoginSchema(Schema):
    correo = fields.String(
        required=True,
        validate=validate.Email(error="Debe ingresar un correo válido.")
    )

    contraseña = fields.String(
        required=True,
        load_only=True,
        error_messages={"required": "La contraseña es obligatoria."}
    )

    @validates("contraseña")
    def validar_contraseña(self, data, **kwargs):
        if len(data) < 6:
            raise ValidationError("La contraseña debe tener al menos 6 caracteres.")
        if not re.search(r"[A-Z]", data):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r"\d", data):
            raise ValidationError("La contraseña debe contener al menos un número.")

    
    