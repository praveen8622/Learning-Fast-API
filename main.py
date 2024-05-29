from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI(
    title="Blog API",
    description="API for managing blog posts",
    version="1.0.0",
    docs_url="/cus-docs",
    redoc_url="/custom-redoc",
    openapi_url="/custom-openapi.json"
)

@app.get('/blog')
def index(limit: int = 10, published: bool = True):
    if published:
        return {'data': f'{limit} published blog list from db'}
    else:
        return {'data': f'{limit} blog list from db'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blog'}

@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'data': ['1', '2']}  # Using a list instead of a set for consistent JSON response

class Blog(BaseModel):
    name: str
    age: int
    body: str


@app.post('/blog')
def createblog(blog:Blog):
    return {'data': f'Blog is created with title as {blog.name}'}
