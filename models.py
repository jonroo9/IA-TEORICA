from pydantic import BaseModel, Field


class Producto(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    precio: float = Field(..., gt=0, description="Debe ser mayor a 0")
    stock: int = Field(..., ge=0, description="No puede ser negativo")