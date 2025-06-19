# This file contains functions for Create, Read, Update, and Delete (CRUD) operations
# on the database models.

# from sqlalchemy.orm import Session
# from . import models
# from .connection import SessionLocal

from sqlalchemy.orm import Session
from . import models
from ..schemas import (
    UserCreate, UserUpdate,
    LocationCreate, LocationUpdate,
    CompanyCreate, CompanyUpdate,
    StoreCounterCreate, StoreCounterUpdate,
    ProductCreate, ProductUpdate,
    StoreCreate, StoreUpdate,
    ProductStoreCreate, ProductStoreUpdate,
    HistoricalPriceCreate, HistoricalPriceUpdate # Added HistoricalPrice schemas
)

def get_user(db: Session, user_id: int):
 return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
 return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
 return db.query(models.User).offset(skip).limit(limit).all()

# Assuming UserCreate is a Pydantic model with necessary fields
# def create_user(db: Session, user: UserCreate):
# fake_hashed_password = user.password + "notreallyhashed" # Replace with actual password hashing
# db_user = models.User(email=user.email, username=user.username, hashed_password=fake_hashed_password)
# db.add(db_user)
# db.commit()
# db.refresh(db_user)
# return db_user

def delete_user(db: Session, user_id: int):
 db_user = db.query(models.User).filter(models.User.id == user_id).first()
 if db_user:
    db.delete(db_user)
    db.commit()
 return db_user

# CRUD functions for Location model

def get_location(db: Session, location_id: int):
    return db.query(models.Location).filter(models.Location.id == location_id).first()

def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()

def create_location(db: Session, location: LocationCreate):
    db_location = models.Location(**location.model_dump())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

def update_location(db: Session, location_id: int, location: LocationUpdate):
    db_location = db.query(models.Location).filter(models.Location.id == location_id).first()
    if db_location:
        for key, value in location.model_dump(exclude_unset=True).items():
            setattr(db_location, key, value)
        db.commit()
        db.refresh(db_location)
    return db_location

def delete_location(db: Session, location_id: int):
    db_location = db.query(models.Location).filter(models.Location.id == location_id).first()
    if db_location:
        db.delete(db_location)
        db.commit()
    return db_location

# CRUD functions for Company model

def get_company(db: Session, company_id: int):
    return db.query(models.Company).filter(models.Company.id == company_id).first()

def get_companies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Company).offset(skip).limit(limit).all()

def create_company(db: Session, company: CompanyCreate):
    db_company = models.Company(**company.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

def update_company(db: Session, company_id: int, company: CompanyUpdate):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_company:
        for key, value in company.model_dump(exclude_unset=True).items():
            setattr(db_company, key, value)
        db.commit()
        db.refresh(db_company)
    return db_company

def delete_company(db: Session, company_id: int):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_company:
        db.delete(db_company)
        db.commit()
    return db_company

# CRUD functions for StoreCounter model

def get_store_counter(db: Session, store_counter_id: int):
    return db.query(models.StoreCounter).filter(models.StoreCounter.id == store_counter_id).first()

def get_store_counters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.StoreCounter).offset(skip).limit(limit).all()

def create_store_counter(db: Session, store_counter: StoreCounterCreate):
    db_store_counter = models.StoreCounter(**store_counter.model_dump())
    db.add(db_store_counter)
    db.commit()
    db.refresh(db_store_counter)
    return db_store_counter

def update_store_counter(db: Session, store_counter_id: int, store_counter: StoreCounterUpdate):
    db_store_counter = db.query(models.StoreCounter).filter(models.StoreCounter.id == store_counter_id).first()
    if db_store_counter:
        for key, value in store_counter.model_dump(exclude_unset=True).items():
            setattr(db_store_counter, key, value)
        db.commit()
        db.refresh(db_store_counter)
    return db_store_counter

def delete_store_counter(db: Session, store_counter_id: int):
    db_store_counter = db.query(models.StoreCounter).filter(models.StoreCounter.id == store_counter_id).first()
    if db_store_counter:
        db.delete(db_store_counter)
        db.commit()
    return db_store_counter

# CRUD functions for Store model

def get_store(db: Session, store_id: int):
    return db.query(models.Store).filter(models.Store.id == store_id).first()

def get_stores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Store).offset(skip).limit(limit).all()

def create_store(db: Session, store: StoreCreate):
    db_store = models.Store(**store.model_dump())
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

def update_store(db: Session, store_id: int, store: StoreUpdate):
    db_store = db.query(models.Store).filter(models.Store.id == store_id).first()
    if db_store:
        for key, value in store.model_dump(exclude_unset=True).items():
            setattr(db_store, key, value)
        db.commit()
        db.refresh(db_store)
    return db_store

def delete_store(db: Session, store_id: int):
    db_store = db.query(models.Store).filter(models.Store.id == store_id).first()
    if db_store:
        db.delete(db_store)
        db.commit()
    return db_store

# CRUD functions for ProductStore model

def get_product_store(db: Session, product_store_id: int):
    return db.query(models.ProductStore).filter(models.ProductStore.id == product_store_id).first()

def get_product_stores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProductStore).offset(skip).limit(limit).all()

def create_product_store(db: Session, product_store: ProductStoreCreate):
    db_product_store = models.ProductStore(**product_store.model_dump())
    db.add(db_product_store)
    db.commit()
    db.refresh(db_product_store)
    return db_product_store

def update_product_store(db: Session, product_store_id: int, product_store: ProductStoreUpdate):
    db_product_store = db.query(models.ProductStore).filter(models.ProductStore.id == product_store_id).first()
    if db_product_store:
        for key, value in product_store.model_dump(exclude_unset=True).items():
            setattr(db_product_store, key, value)
        db.commit()
        db.refresh(db_product_store)
    return db_product_store

def delete_product_store(db: Session, product_store_id: int):
    db_product_store = db.query(models.ProductStore).filter(models.ProductStore.id == product_store_id).first()
    if db_product_store:
        db.delete(db_product_store)
        db.commit()
    return db_product_store

# CRUD functions for HistoricalPrice model

def get_historical_price(db: Session, historical_price_id: int):
    return db.query(models.HistoricalPrice).filter(models.HistoricalPrice.id == historical_price_id).first()

def get_historical_prices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.HistoricalPrice).offset(skip).limit(limit).all()

def create_historical_price(db: Session, historical_price: HistoricalPriceCreate):
    db_historical_price = models.HistoricalPrice(**historical_price.model_dump())
    db.add(db_historical_price)
    db.commit()
    db.refresh(db_historical_price)
    return db_historical_price

def update_historical_price(db: Session, historical_price_id: int, historical_price: HistoricalPriceUpdate):
    db_historical_price = db.query(models.HistoricalPrice).filter(models.HistoricalPrice.id == historical_price_id).first()
    if db_historical_price:
        for key, value in historical_price.model_dump(exclude_unset=True).items():
            setattr(db_historical_price, key, value)
        db.commit()
        db.refresh(db_historical_price)
    return db_historical_price

def delete_historical_price(db: Session, historical_price_id: int):
    db_historical_price = db.query(models.HistoricalPrice).filter(models.HistoricalPrice.id == historical_price_id).first()
    if db_historical_price:
        db.delete(db_historical_price)
        db.commit()
    return db_historical_price