#  Create FastAPI application in Docker with all requests (GET, RETRIEVE, UPDATE - PUT\PATCH, POST, DELETE)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(
    title='First API Project'
)


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str
    is_admin: bool


db_users: Dict[int, User] = {
    1: User(id=1, name="Petr", age=23, email="petr@gmail.com", is_admin=True),
    2: User(id=2, name="Nata", age=23, email="Nata@hmail.vom", is_admin=False)
}

# GET ALL users
@app.get("/users/", response_model=Dict[int, User])
def read_user():
    return db_users

# Get request users ID
@app.get("/users/{users_id}", response_model=User)
def read_user(user_id: int):
    user = db_users.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# POST request create user
@app.post("/users/", response_model=User)
def create_user(user: User):
    db_users[user.id] = user
    return user


# PUT request for update user
@app.put("/user/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    if user_id not in db_users:
        raise HTTPException(status_code=404, detail="User not found")
    db_users[user_id] = user


# DELETE request
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in db_users:
        raise HTTPException(status_code=404, detail="User not found")
    del db_users[user_id]
    return {'message': 'User delete successful'}
