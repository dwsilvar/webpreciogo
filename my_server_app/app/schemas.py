from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime

# Pydantic models for User
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Pydantic models for Location
class LocationBase(BaseModel):
    district: Optional[str] = None
    department: Optional[str] = None
    city: Optional[str] = None
    country: str

class LocationCreate(LocationBase):
    pass

class LocationUpdate(LocationBase):
    district: Optional[str] = None
    department: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None


class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True

# Pydantic models for Company
class CompanyBase(BaseModel):
    name: str

class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(CompanyBase):
    name: Optional[str] = None

class Company(CompanyBase):
    id: int

    class Config:
        orm_mode = True

# Pydantic models for StoreCounter
class StoreCounterBase(BaseModel):
    mode: str

class StoreCounterCreate(StoreCounterBase):
    pass

class StoreCounterUpdate(StoreCounterBase):
    mode: Optional[str] = None

class StoreCounter(StoreCounterBase):
    id: int

    class Config:
        orm_mode = True

# Pydantic models for Product
class ProductBase(BaseModel):
    name: str
    brand: Optional[str] = None
    model: Optional[str] = None
    presentation: Optional[str] = None
    category: Optional[str] = None
    date_release: Optional[date] = None
    image: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    presentation: Optional[str] = None
    category: Optional[str] = None
    date_release: Optional[date] = None
    image: Optional[str] = None

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

# Pydantic models for Store
class StoreBase(BaseModel):
    address: Optional[str] = None
    name: str
    id_location: int
    id_company: int
    url: Optional[str] = None
    ubication_latitud: Optional[float] = None
    ubication_longitud: Optional[float] = None

class StoreCreate(StoreBase):
    pass

class StoreUpdate(StoreBase):
    address: Optional[str] = None
    name: Optional[str] = None
    id_location: Optional[int] = None
    id_company: Optional[int] = None
    url: Optional[str] = None
    ubication_latitud: Optional[float] = None
    ubication_longitud: Optional[float] = None

class Store(StoreBase):
    id: int

    class Config:
        orm_mode = True

# Pydantic models for ProductStore
class ProductStoreBase(BaseModel):
    id_store: Optional[int] = None
    id_product: Optional[int] = None
    id_store_counter: Optional[int] = None
    currency: Optional[str] = None
    value: Optional[float] = None
    discount: Optional[float] = None
    value_discount: Optional[float] = None
    validated_price: Optional[bool] = None

class ProductStoreCreate(ProductStoreBase):
    id_store: int
    id_product: int

class ProductStoreUpdate(ProductStoreBase):
    id_store: Optional[int] = None
    id_product: Optional[int] = None
    id_store_counter: Optional[int] = None
    currency: Optional[str] = None
    value: Optional[float] = None
    discount: Optional[float] = None
    value_discount: Optional[float] = None
    validated_price: Optional[bool] = None

class ProductStore(ProductStoreBase):
    id: int

    class Config:
        orm_mode = True

# Pydantic models for HistoricalPrice
class HistoricalPriceBase(BaseModel):
    id_product_store: int
    currency: Optional[str] = None
    value: Optional[float] = None
    date_init: Optional[datetime] = None

class HistoricalPriceCreate(HistoricalPriceBase):
    pass

class HistoricalPriceUpdate(HistoricalPriceBase):
    id_product_store: Optional[int] = None
    currency: Optional[str] = None
    value: Optional[float] = None
    date_init: Optional[datetime] = None

class HistoricalPrice(HistoricalPriceBase):
    id: int

    class Config:
        orm_mode = True