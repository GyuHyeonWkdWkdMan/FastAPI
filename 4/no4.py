from typing import List, Optional
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[List[str]] = Query(None)):
#async def read_items(q: List[str] = Query(["foo", "bar"])):
#async def read_items(q: list = Query([])):
    query_items = {"q": q}
    return query_items

