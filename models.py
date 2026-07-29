from pydantic import BaseModel

class Producto(BaseModel):
    referencia: str
    nombre: str
    precio_cop: float
    estado: bool
