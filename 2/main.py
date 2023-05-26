from fastapi import FastAPI
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):    #http://127.0.0.1:8000/items/?skip=0&limit=3 값 입력한 만큼 반복, items까지만 입력했을 시 default: skip=0 limit=10
    return fake_items_db[skip : skip + limit]