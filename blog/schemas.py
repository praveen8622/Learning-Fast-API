from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title: str
    body: str

class User(BaseModel):
    name : str
    email : str 
    password : str 
class Showuser(BaseModel):
    name : str
    email : str 
    blogs : List [Blog]

class Showblog(BaseModel):
    title: str
    body: str
    creator : Showuser

class Config:
    orm_mode = True