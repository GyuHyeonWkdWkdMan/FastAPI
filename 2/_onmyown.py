from fastapi import FastAPI
from typing import Optional

app = FastAPI()
def Error(error): print(error)
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):    #http://127.0.0.1:8000/items/?skip=0&limit=3 값 입력한 만큼 반복, items까지만 입력했을 시 default: skip=0 limit=10
    Error('works!')
    return fake_items_db[skip : skip + limit]

#@app.get("/items/{item_id}")
#async def read_item(item_id: str, q: Optional[str] = None):
#    if q:
#        return {"item_id": item_id, "q": q}
#    
#    print("\nitem_id is ",{item_id},"\n")      #값 넘어오는지 확인만
#    Error('Works! rea')
#    return {"item_id": item_id}

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        Error('q is present!')
        item.update({"q": q})
    if not short:
        Error('short is false!')
        item.update(
            {"description": "This is an amazing item that has a long description"}    
        )
    return item

#@app.get("/item/{item_id}")
#async def read_user_item(item_id: str, needy: str):
#    item = {"item_id": item_id, "needy": needy}
#    return item