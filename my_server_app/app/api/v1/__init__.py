# app/api/v1/__init__.py
# Archivo de inicialización para el módulo v1 de la API

from fastapi import APIRouter

# Import all routers from the .endpoints subdirectory
from .endpoints import (
 companies,
 stores,
 locations,
 store_counters,
 products,
 product_stores,
 historical_prices,
 items,
 users,
)

# Create a main router for API version 1
api_router = APIRouter()

# Include individual routers. Adjust prefix if necessary, but endpoints should ideally define their own prefixes.
api_router.include_router(companies.router, prefix="/companies", tags=["companies"])
api_router.include_router(stores.router, prefix="/stores", tags=["stores"])
api_router.include_router(locations.router, prefix="/locations", tags=["locations"])
api_router.include_router(store_counters.router, prefix="/store_counters", tags=["store_counters"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(product_stores.router, prefix="/product_stores", tags=["product_stores"])
api_router.include_router(historical_prices.router, prefix="/historical_prices", tags=["historical_prices"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(users.router, prefix="/users", tags=["users"])