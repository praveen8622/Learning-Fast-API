from sqlalchemy import Column, Integer, String, ForeignKey
from . database import Base 
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    blogs = relationship('Blog', back_populates='creator')  # Correct relationship definition

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship('User', back_populates='blogs')  # Correct relationship definition