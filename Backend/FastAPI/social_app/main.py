from typing import Optional

from django.http import HttpResponse
from fastapi import FastAPI, Response, HTTPException,status
from fastapi.params import Body
from pydantic import BaseModel

import random as rd

app = FastAPI()

my_posts=[]
class Post(BaseModel):
    title:str
    content:str
    published:bool=True
    likes: Optional[int] =None




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(new_post:Post):
    print(new_post.title)
    new_post_dict=new_post.dict()
    new_post_dict["id"]=len(my_posts)+1
    my_posts.append(new_post_dict)
    print(f"your post had been published {new_post.published}")
    return {
        "message": "Your post has been created",
        "post contents":new_post.dict(),
        "id": new_post_dict["id"]
    }

@app.get("/posts")
def get_all_posts():
    return {"data":my_posts}

@app.get("/posts/latest")
def get_latest_post():
    latest_post = my_posts[len(my_posts)-1]
    return {"Latest post is": latest_post}

@app.get("/posts/{id}")
def get_post(id: int,response: Response):
    for post in my_posts:
        if post["id"] == id:
            return {"post details you requersted is ": post}
    #response.status_code=404
    raise HTTPException(status_code=404, detail="post not found")
    return {"message": "post not found"}

@app.delete("/posts/{id}")
def delete_post(id: int):
    for post in my_posts:
        if post["id"] == id:
            my_posts.remove(post)
            raise HTTPException(status_code=204)  #no return or delete message with ctatus code 204
    raise HTTPException(status_code=404, detail="post not found")


def find_index(id):
    for i,p in enumerate(my_posts):
        if p["id"] == id:
            return i
@app.put('/posts/{id}')
def update_post(id:int,post:Post):
   post_dict=post.dict()
   post_dict["id"]=id
   index=find_index(id)
   my_posts[index]=post_dict
   print(f"updated post had been {post_dict}")
   return {"message":f"post with id {id} was updated, and its index in my posts is {index}"}




