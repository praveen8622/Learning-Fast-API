
from fastapi import HTTPException, status

from .. import models, schemas
from sqlalchemy.orm import Session


def get_allblog(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def show(db:Session,id: int):
    blogs= db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blogs :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available')
    return blogs

def create(db: Session,request: schemas.Blog):
    new_user = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def destroy(db: Session, id: int ):
    blog= db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'blog has been deleted.'

def update (db: Session, id: int ,request: schemas.Blog):
    blog= db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available')
    blog.update(request.model_dump())
    db.commit()
    return 'blog has been updated.'