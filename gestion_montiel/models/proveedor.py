# gestion_montiel/models/proveedor.py
import sqlite3 # Importación necesaria para capturar sqlite3.Error
from gestion_montiel.db_utils import get_db # Asumimos que db_utils está en el nivel superior del paquete

def get_all_proveedores(activos_solo=True):
    db = get_db()
    query = "SELECT * FROM proveedor"
    if activos_solo:
        query += " WHERE activo = 1" # SQLite usa 1 para True
    query += " ORDER BY nombre ASC"
    
    proveedores = db.execute(query).fetchall()
    return proveedores

def get_proveedor_by_id(id_proveedor):
    db = get_db()
    proveedor = db.execute(
        "SELECT * FROM proveedor WHERE id = ?", (id_proveedor,)
    ).fetchone()
    return proveedor

def add_proveedor(nombre, contacto_telefono, datos_pago_cuenta, datos_pago_banco, notas_adicionales, activo=1):
    db = get_db()
    try:
        cursor = db.execute(
            "INSERT INTO proveedor (nombre, contacto_telefono, datos_pago_cuenta, datos_pago_banco, notas_adicionales, activo) VALUES (?, ?, ?, ?, ?, ?)",
            (nombre, contacto_telefono, datos_pago_cuenta, datos_pago_banco, notas_adicionales, activo),
        )
        db.commit()
        return cursor.lastrowid # Devuelve el ID del nuevo proveedor
    except sqlite3.Error as e: # Captura errores específicos de SQLite
        db.rollback()
        print(f"Error al añadir proveedor: {e}")
        return None # O lanzar la excepción para manejarla en la ruta

# --- Funciones Pendientes Implementadas ---

def update_proveedor(id_proveedor, nombre, contacto_telefono, datos_pago_cuenta, datos_pago_banco, notas_adicionales, activo):
    """
    Actualiza los datos de un proveedor existente.
    Devuelve True si la actualización fue exitosa, False en caso contrario.
    """
    db = get_db()
    try:
        cursor = db.execute(
            """UPDATE proveedor
               SET nombre = ?, 
                   contacto_telefono = ?, 
                   datos_pago_cuenta = ?, 
                   datos_pago_banco = ?, 
                   notas_adicionales = ?, 
                   activo = ?
               WHERE id = ?""",
            (nombre, contacto_telefono, datos_pago_cuenta, datos_pago_banco, notas_adicionales, activo, id_proveedor)
        )
        db.commit()
        # cursor.rowcount devuelve el número de filas afectadas.
        # Si es > 0, la actualización (probablemente) tuvo éxito.
        return cursor.rowcount > 0 
    except sqlite3.Error as e:
        db.rollback()
        print(f"Error al actualizar proveedor con ID {id_proveedor}: {e}")
        return False

def delete_proveedor(id_proveedor):
    """
    Elimina un proveedor de la base de datos (eliminación física).
    Devuelve True si la eliminación fue exitosa, False en caso contrario.
    """
    db = get_db()
    try:
        cursor = db.execute(
            "DELETE FROM proveedor WHERE id = ?", 
            (id_proveedor,)
        )
        db.commit()
        # cursor.rowcount devuelve el número de filas afectadas.
        # Si es > 0, la eliminación tuvo éxito.
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        db.rollback()
        print(f"Error al eliminar proveedor con ID {id_proveedor}: {e}")
        return False

# --- Alternativa: Desactivar proveedor (Soft Delete) ---
# Si prefieres no eliminar físicamente los proveedores para mantener un historial,
# podrías tener una función para desactivarlos (soft delete).
# def deactivate_proveedor(id_proveedor):
#     """
#     Desactiva un proveedor (soft delete) estableciendo su campo 'activo' a 0.
#     Devuelve True si la desactivación fue exitosa, False en caso contrario.
#     """
#     db = get_db()
#     try:
#         cursor = db.execute(
#             "UPDATE proveedor SET activo = 0 WHERE id = ?",
#             (id_proveedor,)
#         )
#         db.commit()
#         return cursor.rowcount > 0
#     except sqlite3.Error as e:
#         db.rollback()
#         print(f"Error al desactivar proveedor con ID {id_proveedor}: {e}")
#         return False

# --- Fin de Funciones Pendientes ---