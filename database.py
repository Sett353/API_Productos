import sqlite3

DATABASE = "productos.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def crear_tabla():
    conn = get_connection()
    
    conn.execute("""
    CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    referencia TEXT NOT NULL,
    nombre TEXT NOT NULL,
    precio_cop REAL,
    precio_usd REAL,
    estado BOOLEAN
    )
    """)
    
    conn.commit()
    conn.close()

