# Script para crear la estructura inicial del proyecto Flask 'gestion-montiel'
# Ejecutar en la raíz de la carpeta del proyecto (ej: ./gestion-montiel/)

Write-Host "Creando estructura para gestion-montiel..."

# --- Paquete Principal ---
New-Item -ItemType Directory -Path "gestion_montiel"
New-Item -ItemType File -Path "gestion_montiel/__init__.py"
New-Item -ItemType File -Path "gestion_montiel/forms.py" -ErrorAction SilentlyContinue # Opcional
New-Item -ItemType File -Path "gestion_montiel/utils.py" -ErrorAction SilentlyContinue # Opcional

# --- Rutas (Blueprints) ---
New-Item -ItemType Directory -Path "gestion_montiel/routes"
New-Item -ItemType File -Path "gestion_montiel/routes/__init__.py"
New-Item -ItemType File -Path "gestion_montiel/routes/pollo_vivo.py"
New-Item -ItemType File -Path "gestion_montiel/routes/productos.py" # Placeholder futuro

# --- Modelos (Base de Datos) ---
New-Item -ItemType Directory -Path "gestion_montiel/models"
New-Item -ItemType File -Path "gestion_montiel/models/__init__.py"
New-Item -ItemType File -Path "gestion_montiel/models/proveedor.py"
New-Item -ItemType File -Path "gestion_montiel/models/lote_pollo_vivo.py"

# --- Archivos Estáticos ---
New-Item -ItemType Directory -Path "gestion_montiel/static"
New-Item -ItemType Directory -Path "gestion_montiel/static/css"
New-Item -ItemType File -Path "gestion_montiel/static/css/styles.css"
New-Item -ItemType Directory -Path "gestion_montiel/static/js"
New-Item -ItemType File -Path "gestion_montiel/static/js/script.js"
New-Item -ItemType Directory -Path "gestion_montiel/static/img"

# --- Plantillas (Templates) ---
New-Item -ItemType Directory -Path "gestion_montiel/templates"
New-Item -ItemType File -Path "gestion_montiel/templates/base.html"
New-Item -ItemType File -Path "gestion_montiel/templates/index.html"
New-Item -ItemType File -Path "gestion_montiel/templates/404.html" -ErrorAction SilentlyContinue
New-Item -ItemType File -Path "gestion_montiel/templates/500.html" -ErrorAction SilentlyContinue

# --- Plantillas Módulo Pollo Vivo ---
New-Item -ItemType Directory -Path "gestion_montiel/templates/pollo_vivo"
New-Item -ItemType File -Path "gestion_montiel/templates/pollo_vivo/registrar_proveedor.html"
New-Item -ItemType File -Path "gestion_montiel/templates/pollo_vivo/listar_proveedores.html"
New-Item -ItemType File -Path "gestion_montiel/templates/pollo_vivo/registrar_lote.html"
New-Item -ItemType File -Path "gestion_montiel/templates/pollo_vivo/listar_lotes.html"
New-Item -ItemType File -Path "gestion_montiel/templates/pollo_vivo/_formulario_lote.html" -ErrorAction SilentlyContinue

# --- Plantillas Módulo Productos (Placeholder) ---
New-Item -ItemType Directory -Path "gestion_montiel/templates/productos" -ErrorAction SilentlyContinue

# --- Archivos Raíz ---
New-Item -ItemType File -Path "app.py"
New-Item -ItemType File -Path "config.py"
New-Item -ItemType File -Path "requirements.txt" # Crear vacío, luego llenar con pip freeze
New-Item -ItemType File -Path ".gitignore"
New-Item -ItemType File -Path "README.md"

Write-Host "Estructura creada exitosamente."
Write-Host "Recuerda crear tu entorno virtual ('python -m venv venv') y activarlo."
Write-Host "Edita '.gitignore' y 'README.md' según tus necesidades."
Write-Host "Instala Flask ('pip install Flask') y actualiza 'requirements.txt'."