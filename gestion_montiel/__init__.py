# gestion_montiel/__init__.py
from flask import Flask, render_template
from config import Config
from . import db_utils
# --- Nueva Importación ---
from gestion_montiel.routes.pollo_vivo import bp_pollo_vivo # Importar el blueprint

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db_utils.init_app(app)

    # --- Registrar el Blueprint ---
    app.register_blueprint(bp_pollo_vivo, url_prefix='/gestion') # URL base para todas las rutas de este blueprint

    @app.route('/')
    def index():
        try:
            return render_template('index.html', title='Página de Inicio')
        except Exception as e:
            print(f"********** ERROR AL RENDERIZAR PLANTILLA: {e} **********")
            return "Error al cargar la plantilla. Revisa la consola del servidor."

    return app