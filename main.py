from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    is_admin: bool

@app.get('/')
def read():
    return "Hello world"

@app.get('/name/{firstname}')
def read(firstname: str, lastname: str = ''):
    return f'Hello {firstname} {lastname}'

@app.get('/user')
def update_user():
    return 'user'

@app.get('/user/{user_id}')
def update_user(user_id: int):
    return user_id

@app.put('/user/{user_id}')
def update_user(user_id: int, user: User):
    return {'name': user.name, 'age': user.age, 'is_admin': user.is_admin, 'id': user_id}
