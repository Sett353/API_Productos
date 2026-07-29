from fastapi import FastAPI
from database import crear_tabla, get_connection
from models import Producto

app = FastAPI()

crear_tabla()

tasa_usd=3205.87

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}

@app.post("/productos")
def crear_producto(producto: Producto):
    precio_usd= producto.precio_cop/tasa_usd
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos"\
        "(referencia, nombre, precio_cop, precio_usd, estado) VALUES (?, ?, ?, ?, ?)", 
        (producto.referencia, producto.nombre, producto.precio_cop, precio_usd, producto.estado))
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

@app.get ("/productos/{id}")
def buscar (id: int):
    conn = get_connection()
    producto= conn.execute(
        "SELECT * FROM productos WHERE id = ?",
        (id,)
    ).fetchone()
    conn.close()
    if producto:
        return dict(producto)
    return {"mensaje": "No existe"}

@app.put("/productos/{id}")
def actualizar (id:int, producto:Producto):
    precio_usd= producto.precio_cop/tasa_usd
    conn = get_connection()
    conn.execute(
        "UPDATE productos SET referencia=?,nombre=?,precio_cop=?,precio_usd=?,estado=? WHERE id=?",
        (producto.referencia,producto.nombre,producto.precio_cop,precio_usd,producto.estado,id)
    )
    conn.commit()
    conn.close()
    return {"mensaje": "Actualizado correctamente"}

@app.delete("/productos/{id}")
def eliminar(id: int):

    conn = get_connection()
    conn.execute(
    "DELETE FROM productos WHERE id=?",
    (id,)
    )
    conn.commit()
    conn.close()
    return {"mensaje": "Eliminado"}