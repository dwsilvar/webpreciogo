# main.py
# Archivo principal de la aplicación FastAPI.
# Aquí se crea la instancia de la aplicación y se incluyen los routers de los diferentes módulos.

# /my_server_app/app/main.py
# Main entry point for the FastAPI application.
# This file creates the FastAPI instance and includes routers from different modules.

from fastapi import FastAPI

# Importar routers de los módulos
# from app.api import api_router

app = FastAPI(
    description="Aplicativo servidor standalone",
    version="0.1.0",
)

# Incluir routers
# app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    """Punto de entrada principal."""
    return {"message": "Welcome to My Server App!"}

# Otros endpoints o configuraciones globales pueden ir aquí.