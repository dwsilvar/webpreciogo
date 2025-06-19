from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ... import schemas, crud
from ...database.connection import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Store)
def create_store(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    """
    Registers a new store.
    """
    return crud.create_store(db=db, store=store)