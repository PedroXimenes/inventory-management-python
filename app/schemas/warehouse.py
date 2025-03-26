from pydantic import BaseModel

class WarehouseBase(BaseModel):
    name: str | None = None
    location: str | None = None

class WarehouseCreate(WarehouseBase):
    pass # No additional Fields

class WarehouseUpdate(WarehouseBase):
    name: str | None = None
    location: str | None = None

class WarehouseResponse(WarehouseBase):
    id: int

    class Config:
        from_attributes = True