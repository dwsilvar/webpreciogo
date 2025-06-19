# Purpose: Define database models using SQLAlchemy.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

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