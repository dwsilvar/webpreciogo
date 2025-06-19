from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ... import crud, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/store_counters",
    tags=["store_counters"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.StoreCounter)
def create_store_counter(
    store_counter: schemas.StoreCounterCreate, db: Session = Depends(get_db)
):
    # You might want to add some validation here before creating the store counter
    # For example, check if the related store_id exists
    # db_store = crud.get_store(db, store_id=store_counter.store_id)
    # if not db_store:
    #     raise HTTPException(status_code=400, detail="Store not found")

    return crud.create_store_counter(db=db, store_counter=store_counter)

# You would add other endpoints here for GET, PUT, DELETE operations for store counters