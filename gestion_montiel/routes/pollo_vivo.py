# gestion_montiel/routes/pollo_vivo.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
# Importamos las funciones del modelo de proveedor
from gestion_montiel.models import proveedor as proveedor_model

# Creamos un Blueprint. 'pollo_vivo' es el nombre del blueprint.
bp_pollo_vivo = Blueprint('pollo_vivo', __name__, template_folder='../templates/pollo_vivo')

@bp_pollo_vivo.route('/proveedores')
def listar_proveedores():
    """Muestra la lista de todos los proveedores."""
    try:
        proveedores = proveedor_model.get_all_proveedores()
        return render_template('listar_proveedores.html', proveedores=proveedores, title="Proveedores de Pollo Vivo")
    except Exception as e:
        flash(f"Error al cargar la lista de proveedores: {e}", 'error')
        # Es buena práctica mostrar la página igualmente, aunque sea vacía, para no romper la navegación.
        return render_template('listar_proveedores.html', proveedores=[], title="Proveedores de Pollo Vivo")

@bp_pollo_vivo.route('/proveedores/nuevo', methods=['GET', 'POST'])
def registrar_proveedor():
    """Muestra el formulario para registrar un nuevo proveedor y maneja el envío."""
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        contacto_telefono = request.form.get('contacto_telefono', '').strip()
        datos_pago_cuenta = request.form.get('datos_pago_cuenta', '').strip()
        datos_pago_banco = request.form.get('datos_pago_banco', '').strip()
        notas_adicionales = request.form.get('notas_adicionales', '').strip()
        activo = 1 if request.form.get('activo') else 0

        if not nombre:
            flash('El nombre del proveedor es obligatorio.', 'warning')
            # Volvemos a renderizar el formulario con los datos ya introducidos
            return render_template('registrar_proveedor.html', title="Registrar Proveedor", form_data=request.form)
        
        try:
            proveedor_id = proveedor_model.add_proveedor(
                nombre, 
                contacto_telefono, 
                datos_pago_cuenta, 
                datos_pago_banco, 
                notas_adicionales, 
                activo
            )
            if proveedor_id:
                flash(f'Proveedor "{nombre}" registrado con éxito (ID: {proveedor_id}).', 'success')
                return redirect(url_for('pollo_vivo.listar_proveedores'))
            else:
                # Esto podría ocurrir si add_proveedor retorna None/False por alguna validación interna o error no esperado
                flash('Error al registrar el proveedor. No se pudo guardar en la base de datos.', 'error')
        except Exception as e:
            flash(f'Error excepcional al registrar el proveedor: {e}', 'error')
        
        # Si llegamos aquí, algo falló después de la validación inicial o en el try-except
        return render_template('registrar_proveedor.html', title="Registrar Proveedor", form_data=request.form)

    # Para peticiones GET
    return render_template('registrar_proveedor.html', title="Registrar Proveedor")

@bp_pollo_vivo.route('/proveedores/ver/<int:id_proveedor>')
def ver_proveedor(id_proveedor):
    """Muestra los detalles de un proveedor específico."""
    try:
        proveedor = proveedor_model.get_proveedor_by_id(id_proveedor)
        if not proveedor:
            flash(f'Proveedor con ID {id_proveedor} no encontrado.', 'warning')
            return redirect(url_for('pollo_vivo.listar_proveedores'))
        return render_template('ver_proveedor.html', proveedor=proveedor, title=f"Detalle de {proveedor.get('nombre', 'Proveedor')}")
    except Exception as e:
        flash(f"Error al cargar detalles del proveedor: {e}", 'error')
        return redirect(url_for('pollo_vivo.listar_proveedores'))


@bp_pollo_vivo.route('/proveedores/editar/<int:id_proveedor>', methods=['GET', 'POST'])
def editar_proveedor(id_proveedor):
    """Muestra el formulario para editar un proveedor existente y maneja el envío."""
    # Intentamos obtener el proveedor primero para GET y para POST (antes de actualizar)
    try:
        proveedor_actual = proveedor_model.get_proveedor_by_id(id_proveedor)
    except Exception as e:
        flash(f"Error al buscar el proveedor para editar: {e}", 'error')
        return redirect(url_for('pollo_vivo.listar_proveedores'))

    if not proveedor_actual:
        flash(f'Proveedor con ID {id_proveedor} no encontrado.', 'warning')
        return redirect(url_for('pollo_vivo.listar_proveedores'))

    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        contacto_telefono = request.form.get('contacto_telefono', '').strip()
        datos_pago_cuenta = request.form.get('datos_pago_cuenta', '').strip()
        datos_pago_banco = request.form.get('datos_pago_banco', '').strip()
        notas_adicionales = request.form.get('notas_adicionales', '').strip()
        activo = 1 if request.form.get('activo') else 0

        if not nombre:
            flash('El nombre del proveedor es obligatorio.', 'warning')
            # Pasamos los datos del formulario (request.form) y el proveedor original para el título, etc.
            return render_template('editar_proveedor.html', title=f"Editar Proveedor: {proveedor_actual.get('nombre')}", proveedor=request.form, id_proveedor=id_proveedor)

        try:
            # Asumimos que update_proveedor devuelve el número de filas afectadas o un booleano
            actualizado = proveedor_model.update_proveedor(
                id_proveedor,
                nombre, 
                contacto_telefono, 
                datos_pago_cuenta, 
                datos_pago_banco, 
                notas_adicionales, 
                activo
            )
            if actualizado: # O if actualizado > 0 si devuelve conteo
                flash(f'Proveedor "{nombre}" actualizado con éxito.', 'success')
                return redirect(url_for('pollo_vivo.listar_proveedores'))
            else:
                flash('No se pudo actualizar el proveedor o no hubo cambios.', 'info') # 'info' si no hubo cambios, 'error' si falló
        except Exception as e:
            flash(f'Error excepcional al actualizar el proveedor: {e}', 'error')
        
        # Si llegamos aquí, algo falló, volvemos a renderizar el form con los datos del POST
        # y el ID para la URL del action del form.
        return render_template('editar_proveedor.html', title=f"Editar Proveedor: {proveedor_actual.get('nombre')}", proveedor=request.form, id_proveedor=id_proveedor)

    # Para peticiones GET, pasamos el proveedor_actual obtenido de la BD
    return render_template('editar_proveedor.html', title=f"Editar Proveedor: {proveedor_actual.get('nombre')}", proveedor=proveedor_actual, id_proveedor=id_proveedor)

@bp_pollo_vivo.route('/proveedores/eliminar/<int:id_proveedor>', methods=['POST']) # Solo POST para seguridad
def eliminar_proveedor(id_proveedor):
    """Elimina un proveedor."""
    # Es buena práctica verificar si existe antes de intentar eliminar,
    # aunque la BD podría manejarlo (ej. no hacer nada si no existe).
    try:
        proveedor = proveedor_model.get_proveedor_by_id(id_proveedor)
        if not proveedor:
            flash(f'Proveedor con ID {id_proveedor} no encontrado. No se pudo eliminar.', 'warning')
            return redirect(url_for('pollo_vivo.listar_proveedores'))

        # Asumimos que delete_proveedor devuelve True/False o el número de filas eliminadas
        eliminado = proveedor_model.delete_proveedor(id_proveedor)
        if eliminado: # O if eliminado > 0
            flash(f'Proveedor "{proveedor.get("nombre", id_proveedor)}" eliminado con éxito.', 'success')
        else:
            flash(f'No se pudo eliminar el proveedor "{proveedor.get("nombre", id_proveedor)}".', 'error')
    except Exception as e:
        flash(f'Error excepcional al eliminar el proveedor: {e}', 'error')
    
    return redirect(url_for('pollo_vivo.listar_proveedores'))