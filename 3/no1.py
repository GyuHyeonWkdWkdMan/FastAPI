from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel  # to make request body


class Item(BaseModel):      #making request body
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.post("/items")
async def create_item(item: Item):
    return item