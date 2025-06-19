# Use an official Python runtime as a base image
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
# Set the working directory in the container
WORKDIR /app

# Copia los archivos de requisitos e instala las dependencias
# Copy the requirements file into the container
COPY requirements.txt .
# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
# Copy the rest of the application code into the container
COPY . .

# Expone el puerto en el que correrá la aplicación FastAPI
# Expose the port the FastAPI application will run on
EXPOSE 80

# Comando para ejecutar la aplicación con Uvicorn
# Command to run the application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]