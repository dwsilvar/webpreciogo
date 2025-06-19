from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ... import crud, schemas
from ..dependencies import get_db

router = APIRouter(
    tags=["historical_prices"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.HistoricalPrice)
def create_historical_price(
    historical_price: schemas.HistoricalPriceCreate,
    db: Session = Depends(get_db)
):
    return crud.create_historical_price(db=db, historical_price=historical_price)

@router.get("/{historical_price_id}", response_model=schemas.HistoricalPrice)
def read_historical_price(
    historical_price_id: int,
    db: Session = Depends(get_db)
):
    db_historical_price = crud.get_historical_price(db, historical_price_id=historical_price_id)
    if db_historical_price is None:
        raise HTTPException(status_code=404, detail="Historical Price not found")
    return db_historical_price

@router.get("/", response_model=list[schemas.HistoricalPrice])
def read_historical_prices(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    historical_prices = crud.get_historical_prices(db, skip=skip, limit=limit)
    return historical_prices

@router.put("/{historical_price_id}", response_model=schemas.HistoricalPrice)
def update_historical_price(
    historical_price_id: int,
    historical_price: schemas.HistoricalPriceUpdate,
    db: Session = Depends(get_db)
):
    db_historical_price = crud.update_historical_price(db, historical_price_id=historical_price_id, historical_price=historical_price)
    if db_historical_price is None:
        raise HTTPException(status_code=404, detail="Historical Price not found")
    return db_historical_price

@router.delete("/{historical_price_id}", response_model=schemas.HistoricalPrice)
def delete_historical_price(
    historical_price_id: int,
    db: Session = Depends(get_db)
):
    db_historical_price = crud.delete_historical_price(db, historical_price_id=historical_price_id)
    if db_historical_price is None:
        raise HTTPException(status_code=404, detail="Historical Price not found")
    return db_historical_price