DROP TABLE IF EXISTS proveedor;
DROP TABLE IF EXISTS lote_pollo_vivo;

CREATE TABLE proveedor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    contacto_telefono TEXT,
    datos_pago_cuenta TEXT,
    datos_pago_banco TEXT,
    notas_adicionales TEXT,
    activo INTEGER NOT NULL DEFAULT 1, -- 1 para True, 0 para False
    creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE lote_pollo_vivo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_llegada DATE NOT NULL,
    proveedor_id INTEGER NOT NULL,
    marca_pollo TEXT,
    cantidad_piezas INTEGER NOT NULL,
    tamano_promedio_kg REAL NOT NULL, -- Usar REAL para decimales en SQLite
    precio_compra_kg REAL NOT NULL,
    costo_total_calculado REAL, -- Se calculará en la app
    estado_pago TEXT DEFAULT 'Pendiente', -- 'Pendiente', 'Pagado'
    fecha_pago DATE,
    metodo_transporte TEXT, -- 'Proveedor', 'Propio'
    costo_transporte_adicional REAL,
    notas_lote TEXT,
    creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (proveedor_id) REFERENCES proveedor (id)
);