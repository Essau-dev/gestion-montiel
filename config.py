import os

# Obtener la ruta base del proyecto
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una-clave-secreta-muy-dificil-de-adivinar-cambiar-luego'
    DATABASE_NAME = 'gestion_montiel.db'
    DATABASE_PATH = os.path.join(BASE_DIR, DATABASE_NAME) # Ruta a la BD en la raíz del proyecto
    
    # Para SQLite, la URI es un poco diferente si no usamos SQLAlchemy directamente
    # No la necesitaremos si manejamos la conexión directamente con sqlite3,
    # pero la dejo por si se usa un ORM después.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + DATABASE_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Solo relevante para SQLAlchemy