from typing import Optional

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(
    *,

    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),

    q: Optional[str] = None,

    item: Optional[Item] = None,

):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results