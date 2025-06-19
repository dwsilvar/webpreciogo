# Path: my_server_app/app/api/v1/endpoints/items.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/items/")
async def read_items():
    """
    Retrieve a list of items.
    """
    return [{"item_id": "Foo"}, {"item_id": "Bar"}]

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    Retrieve a specific item by ID.
    """
    return {"item_id": item_id}

# Add more item-related endpoints here (create, update, delete)