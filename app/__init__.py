from flask import Flask

from app.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Creación de app
    app = Flask(__name__)

    # Configuración
    configuration = config['development']
    app.config.from_object(configuration)

    # Iniciamos la base de datos y las migraciones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registro de Blueprints
    from app.resources import inicio, usuario
    
    app.register_blueprint(inicio, url_prefix='/inicio')
    app.register_blueprint(usuario, url_prefix='/usuario')

    # Modelos
    from app.models import Usuario, Amistad, Amistad

    return app

