from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read():
    return "Hello world"

@app.get('/name/{firstname}')
def read(firstname: str, lastname: str = ''):
    return f'Hello {firstname} {lastname}'

