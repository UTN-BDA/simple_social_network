import os
import uuid
from werkzeug.utils import secure_filename
from typing import List

class ImageHandler:
    def _validar_extension(self, imagen):
        # Asegurar nombre seguro
        original_filename = secure_filename(imagen.filename)

        # Extraer extensión
        _, extension = os.path.splitext(original_filename)
        extension = extension.lower()

        # Validar extensiones
        extensiones_validas = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}
        if extension not in extensiones_validas:
            raise ValueError("Extensión de imagen no permitida")
        
        return extension
        
    def perfil(self, imagen):

        extension = self._validar_extension(imagen)
        # Cambiar nombre del archivo y ruta
        nombre_archivo = f"{uuid.uuid4().hex}{extension}"

        # Guardar archivo
        ruta_guardado = os.path.join(os.environ.get('UPLOAD_FOLDER'), nombre_archivo)
        imagen.save(ruta_guardado)

        # Devolver ubicación del archivo
        return nombre_archivo
    
    def publicacion(self, imagenes: List):
        # Manejo de imagenes
        publicaciones = []
        for imagen in imagenes:
            if imagen.filename != "":
                extension = self._validar_extension(imagen)
                nombre_archivo = f"{uuid.uuid4().hex}{extension}"
                ruta_guardado = os.path.join(os.environ.get('POSTS_UPLOAD_FOLDER'), nombre_archivo)
                imagen.save(ruta_guardado)
                publicaciones.append(nombre_archivo)
    
        return publicaciones