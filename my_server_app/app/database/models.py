# Purpose: Define database models using SQLAlchemy.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import ForeignKey, Float, DateTime, Boolean

# Define the base class for declarative models
Base = declarative_base()

# Example model (replace with your actual models)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # Add any other columns your user model requires


# SQLAlchemy model for the 'Location' table
class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    district = Column(String, nullable=True) # Assuming district can be null
    department = Column(String, nullable=True) # Assuming department can be null
    city = Column(String, nullable=True) # Assuming city can be null
    country = Column(String)

# SQLAlchemy model for the 'Company' table
class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# SQLAlchemy model for the 'StoreCounter' table
class StoreCounter(Base):
    __tablename__ = "store_counters"

    id = Column(Integer, primary_key=True, index=True)
    # The 'mode' column is expected to have values like 'App', 'Online', 'En tienda', 'App móvil', 'En tienda con tarjeta'
    mode = Column(String)

# SQLAlchemy model for the 'Product' table
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    brand = Column(String, nullable=True)
    model = Column(String, nullable=True)
    presentation = Column(String, nullable=True)
    category = Column(String, nullable=True)
    date_release = Column(Date, nullable=True)
    image = Column(String, nullable=True)

# SQLAlchemy model for the 'Store' table
class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=True)
    name = Column(String, index=True)
    id_location = Column(Integer, ForeignKey("locations.id"))
    id_company = Column(Integer, ForeignKey("companies.id"))
    url = Column(String, nullable=True)
    ubication_latitud = Column(Float, nullable=True)
    ubication_longitud = Column(Float, nullable=True)

 
# SQLAlchemy model for the 'ProductStore' table
class ProductStore(Base):
    __tablename__ = "product_stores"
 
    id = Column(Integer, primary_key=True, index=True)
    id_store = Column(Integer, ForeignKey("stores.id"))
    id_product = Column(Integer, ForeignKey("products.id"))
    id_store_counter = Column(Integer, ForeignKey("store_counters.id"), nullable=True)
    currency = Column(String, nullable=True)
    value = Column(Float, nullable=True)
    discount = Column(Float, nullable=True)
    value_discount = Column(Float, nullable=True)
    validated_price = Column(Boolean, nullable=True)
 

# SQLAlchemy model for the 'HistoricalPrice' table
class HistoricalPrice(Base):
    __tablename__ = "historical_prices"

    id = Column(Integer, primary_key=True, index=True)
    id_product_store = Column(Integer, ForeignKey("product_stores.id"))
    currency = Column(String, nullable=True)
    value = Column(Float, nullable=True)
    date_init = Column(DateTime, nullable=True)



