from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ... import crud, schemas
from ..dependencies import get_db # Assuming you have a dependency to get the DB session

router = APIRouter(
    tags=["product_stores"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.ProductStore)
def create_product_store_association(
    product_store: schemas.ProductStoreCreate,
    db: Session = Depends(get_db)
):
    # You might want to add checks here, e.g., if product_id and store_id exist
    return crud.create_product_store(db=db, product_store=product_store)

@router.get("/{product_store_id}", response_model=schemas.ProductStore)
def read_product_store_association(
    product_store_id: int,
    db: Session = Depends(get_db)
):
    db_product_store = crud.get_product_store(db=db, product_store_id=product_store_id)
    if db_product_store is None:
        raise HTTPException(status_code=404, detail="ProductStore association not found")
    return db_product_store

@router.get("/", response_model=List[schemas.ProductStore])
def read_product_stores_associations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    product_stores = crud.get_product_stores(db=db, skip=skip, limit=limit)
    return product_stores

@router.put("/{product_store_id}", response_model=schemas.ProductStore)
def update_product_store_association(
    product_store_id: int,
    product_store: schemas.ProductStoreUpdate,
    db: Session = Depends(get_db)
):
    db_product_store = crud.update_product_store(db=db, product_store_id=product_store_id, product_store=product_store)
    if db_product_store is None:
        raise HTTPException(status_code=404, detail="ProductStore association not found")
    return db_product_store

@router.delete("/{product_store_id}", response_model=schemas.ProductStore)
def delete_product_store_association(
    product_store_id: int,
    db: Session = Depends(get_db)
):
    db_product_store = crud.delete_product_store(db=db, product_store_id=product_store_id)
    if db_product_store is None:
        raise HTTPException(status_code=404, detail="ProductStore association not found")
    return db_product_store