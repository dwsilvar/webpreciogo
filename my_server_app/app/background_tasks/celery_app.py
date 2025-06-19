# This file configures the Celery application for background tasks.

from celery import Celery

# Basic Celery app configuration
# Replace with your actual broker URL (e.g., Redis or RabbitMQ)
celery_app = Celery(
    "my_background_tasks",
    broker="redis://localhost:6379/0",  # Example Redis broker URL
    backend="redis://localhost:6379/0" # Example Redis backend URL
)

# Optional: Configure Celery to automatically discover tasks in specific modules
# celery_app.autodiscover_tasks(['my_server_app.app.background_tasks'])