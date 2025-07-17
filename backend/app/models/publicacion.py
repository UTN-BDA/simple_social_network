from dataclasses import dataclass, field
from typing import List

@dataclass
class Publicacion:

    _id: str = None
    id_usuario: str = None
    fecha: str = None
    imagen: List = field(default_factory=list)
    texto: str = None
    