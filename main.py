from fastapi import FastAPI, HTTPException
from models import Producto

app = FastAPI(title="API de Productos")

# "Base de datos" temporal en memoria
productos_db = []
siguiente_id = 1


@app.get("/")
def inicio():
    return {"mensaje": "API de Productos funcionando"}


@app.post("/productos", status_code=201)
def crear_producto(producto: Producto):
    global siguiente_id
    nuevo_producto = producto.model_dump()
    nuevo_producto["id"] = siguiente_id
    productos_db.append(nuevo_producto)
    siguiente_id += 1
    return nuevo_producto


@app.get("/productos")
def listar_productos():
    return productos_db


@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    for p in productos_db:
        if p["id"] == producto_id:
            return p
    raise HTTPException(status_code=404, detail="Producto no encontrado")


@app.put("/productos/{producto_id}")
def actualizar_producto(producto_id: int, producto: Producto):
    for p in productos_db:
        if p["id"] == producto_id:
            p["nombre"] = producto.nombre
            p["precio"] = producto.precio
            p["stock"] = producto.stock
            return p
    raise HTTPException(status_code=404, detail="Producto no encontrado")


@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int):
    for p in productos_db:
        if p["id"] == producto_id:
            productos_db.remove(p)
            return {"mensaje": f"Producto {producto_id} eliminado"}
    raise HTTPException(status_code=404, detail="Producto no encontrado")