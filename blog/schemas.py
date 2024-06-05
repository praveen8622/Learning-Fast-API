from pydantic import BaseModel
from typing import List, Optional

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

class Login(BaseModel):
    username: str
    password: str 

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None