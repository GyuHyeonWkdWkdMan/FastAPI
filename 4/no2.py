from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")

async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):    #query's default value: None

    results = {"items": [{"item_id": "Foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
        return results