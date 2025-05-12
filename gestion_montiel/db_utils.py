import sqlite3
import os
from flask import g # g es para almacenar la conexión en el contexto de la app/request

# La configuración de DATABASE_PATH ahora vendrá de app.config
# DATABASE_NAME = 'gestion_montiel.db'
# BASE_DIR_PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Sube un nivel desde gestion_montiel/
# DATABASE_PATH = os.path.join(BASE_DIR_PROJECT, DATABASE_NAME)

def get_db():
    # Usamos current_app.config para obtener la ruta de la BD
    # Esto requiere que la app esté configurada antes de llamar a get_db
    # y que estemos dentro de un contexto de aplicación.
    from flask import current_app # Importar aquí para evitar dependencia circular en el arranque
    
    if 'db' not in g:
        db_path = current_app.config['DATABASE_PATH']
        g.db = sqlite3.connect(
            db_path,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row # Para acceder a columnas por nombre
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    # Leer el script SQL para crear las tablas
    # La ruta al schema.sql ahora es relativa al directorio actual de este archivo (db_utils.py)
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    with open(schema_path, 'r') as f:
        db.executescript(f.read())
    print("Tablas de la base de datos inicializadas/recreadas.")

# Función para registrar con la app Flask
def init_app(app):
    app.teardown_appcontext(close_db) # Cierra la BD al final de cada request/contexto
    # Aquí podríamos añadir un comando CLI `flask init-db` si usamos `click`
    # Por ahora, lo haremos con un script separado.