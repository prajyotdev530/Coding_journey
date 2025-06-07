from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
users=[]

class User(BaseModel):
    name: str
    username: str
    password: str
    blood_group: str
@app.get("/users")
async def get_users():
    return users
@app.post('/new_user')
def new_user(user: User):
    user_dict=user.dict()
    user_dict['id']=len(users)+1
    users.append(user_dict)
    return {"message": "New user created"}

