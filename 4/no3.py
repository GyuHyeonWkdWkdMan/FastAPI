from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")

async def read_items(q: Optional[str] = Query("fixedquery", min_length=3, max_length=50)):    #query's default value: "fixedquery"

    p1= "done!"
    if len(q)<3:
        p1="length is too short"

    results = {"items": [{"item_id": "Foo"}, {"item_id": "bar"}, {"status": p1}]}
    if q:
        results.update({"q": q})
        return results
    else:
        return p1