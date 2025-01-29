from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId
from database.models import get_item, get_all_items, create_item, update_item, delete_item, serialize_doc
from database.schemas import ItemSchema, UpdateItemSchema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Only allow requests from React frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

# CRUD Endpoints with Schemas
@app.post("/items/", response_model=dict)
async def create_item_endpoint(item: ItemSchema):
    result = create_item(item.dict())
    return {"id": str(result.inserted_id)}

@app.get("/items/", response_model=list)
async def read_items():
    return get_all_items()

@app.get("/items/{item_id}", response_model=dict)
async def read_item(item_id: str):
    item = get_item(item_id)
    if item:
        return serialize_doc(item)
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=dict)
async def update_item_endpoint(item_id: str, updated_item: UpdateItemSchema):
    result = update_item(item_id, updated_item.dict(exclude_unset=True))
    if result.modified_count:
        return {"message": "Item updated"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", response_model=dict)
async def delete_item_endpoint(item_id: str):
    result = delete_item(item_id)
    if result.deleted_count:
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
