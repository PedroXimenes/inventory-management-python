from fastapi import FastAPI, Depends, HTTPException
from app.schemas.warehouse import WarehouseBase, WarehouseCreate, WarehouseResponse
from app.models.warehouse import Warehouse
from sqlalchemy.orm import Session
from app.db.database import get_db

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/warehouses", response_model=list[WarehouseResponse])
async def read_warehouses(db: Session = Depends(get_db)):
    warehouse = db.query(Warehouse).all()
    print(warehouse)
    return warehouse

@app.get("/warehouses/{id}")
async def read_warehouse(id: int, db: Session = Depends(get_db)):
    warehouse = db.query(Warehouse).filter(Warehouse.id == id).first()
    if warehouse is None:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return warehouse

@app.post("/warehouses")
async def create_warehouse(warehouse: WarehouseCreate, db: Session = Depends(get_db)):
    db_item = Warehouse(name=warehouse.name, location=warehouse.location)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item