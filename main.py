from fastapi import FastAPI
from database import crear_tabla, get_connection
from models import Producto

app = FastAPI()

crear_tabla()

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}

@app.post("/productos")
def crear_producto(producto: Producto):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos"\
        "(referencia, nombre, precio_cop, precio_usd, estado) VALUES (?, ?, ?, ?, ?)", 
        (producto.referencia, producto.nombre, producto.precio_cop, producto.precio_usd, producto.estado))
    conn.commit()
    conn.close()
    return {"mensaje": "Producto creado exitosamente"}

@app.get("/productos")
def listar_productos():
    conn = get_connection()
    productos = conn.execute(
        "SELECT * FROM productos"
    ).fetchall()
    conn.close()
    return [dict(x) for x in productos]