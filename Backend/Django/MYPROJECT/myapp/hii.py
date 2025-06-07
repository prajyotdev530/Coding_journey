from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def posts():
    return {"data": "here is your data"}

@app.post("/createposts")
def create_posts():
    return {
        "message": "Your post has been created",

    }