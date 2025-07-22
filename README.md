
# Simple Social Network

Este proyecto tiene como fin el aprendizaje en la implementación de bases de datos tanto SQL como NOSQL. Consistirá en una simple red social donde usuarios podrán hacer amigos y realizar publicaciones.


## Tecnologías

**Python:** lenguaje de programación principal

**Flask:** framework utilizado para el backend.

**React:** framework utilizado para el frontend.

**SQLAlchemy:** ORM (Object-Relational Mapping) para la interacción con la base de datos.

**PostgreSQL:** sistema de gestión de base de datos relacional.

**MongoDB:** base de datos NO relacional.


## Ejecución

Backend:

Para ejecutar este proyecto debe tener instalado Python 3.12.

Una vez clonado el repositorio. Lo primero que deberá hacer es ingresar a la carpeta backend y crear un archivo ".env" siguiendo lo mostrado en el archivo "env_example".

Crear un entorno virtual.
```bash
  python -m venv venv
```

Para activarlo:
```bash
  venv/Scripts/activate
```

Una vez activado, es necesario instalar los paquetes necesarios para el correcto funcionamiento de la aplicación.
```bash
  pip install -r requirements.txt
```

Con los paquetes instalados deberá crear la base de datos relacional utilizando el siguiente comando:
```bash
  flask db upgrade
```

Con todo listo ya podrá iniciar la aplicación con:
```bash
  python app.py
```
Frontend:
Para ejecutar este proyecto debe tener instalado Node.js >= 16.x y npm.

Una vez clonado el repositorio. Lo primero que deberá hacer es ingresar a la carpeta frontend y ejecutar lo siguiente para instalar las dependencias.
```bash
  npm install
```
Con todo listo ya podrá iniciar la aplicación con:
```bash
  npm start
```
## Autores

- [@joaquin_lepez](https://github.com/JoaquinLepez)
- [@agustin_salinas](https://github.com/Salinas5)
- [@emiliano_sorato](https://github.com/emisorato1)

