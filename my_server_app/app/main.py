# /my_server_app/app/main.py
# Main entry point for the FastAPI application.
# This file creates the FastAPI instance and includes routers from different modules.

from fastapi import FastAPI

# Importar routers de los módulos
from app.api.v1 import api_router as api_v1_router

app = FastAPI(
    description="Aplicativo servidor standalone",
    version="0.1.0",
)

# Include routers
app.include_router(api_v1_router, prefix="/api/v1")

@app.get("/")
def read_root():
    """Punto de entrada principal."""
    return {"message": "Welcome to My Server App!"}

# Otros endpoints o configuraciones globales pueden ir aquí.