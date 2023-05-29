from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def rood():
    return{"message": "This is the last program of Chapter 1"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}