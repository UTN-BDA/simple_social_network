from dotenv import load_dotenv
from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass
        

class DevelopmentConfig(Config):
    # Configuración de App
    DEBUG = True

    # Configuración de PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de carpetas
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    POSTS_UPLOAD_FOLDER = os.environ.get('POSTS_UPLOAD_FOLDER')

    # Configuración de MongoDB
    MONGO_URI = os.environ.get('MONGO_URI')


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

