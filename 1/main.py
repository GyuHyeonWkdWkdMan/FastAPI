from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}


#####################################################
#path operaion의 순서
#기능이 겹친다면 등록한 순서에 따라 우선순위 결정
#예시: localhost:8000/users/me 접속시 두 번째 함수 실행 안되고 
#첫 번째 함수로만 실행될 것임
@app.get("/users/me")
async def read_user_me():
    return{"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
#####################################################

