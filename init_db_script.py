from gestion_montiel import create_app
from gestion_montiel.db_utils import init_db # Importa la función específica

print("Creando contexto de aplicación para inicializar la BD...")
app = create_app()

# Necesitamos un contexto de aplicación para que get_db() funcione correctamente
# y pueda acceder a app.config y al objeto 'g'.
with app.app_context():
    print("Contexto de aplicación creado. Inicializando la base de datos...")
    init_db()

print("Script de inicialización de base de datos completado.")