from fastapi import APIRouter, Depends,Response,status ,HTTPException
from typing import List
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session



router = APIRouter(
    prefix='/blog',
    tags= ['Blogs']
)

@router.get('/', response_model=List [schemas.Showblog])
def getdata(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.get('/{id}',status_code=200, response_model=schemas.Showblog)
def allblogs(id, db: Session=Depends(get_db)):
    blogs= db.query(models.Blog).filter(models.Blog.id== id).first()
    if not blogs :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{'detail':f'blog with id {id} is not available'}
    return blogs

@router.post('/', response_model=schemas.Blog,status_code=201)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_user = models.Blog(title=request.title, body=request.body, user_id = 1)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(id, db:Session = Depends(get_db)):
    blog= db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'blog has been deleted.'

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request:schemas.Blog,db:Session = Depends(get_db)):
    blog= db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} is not available')
    blog.update(request.model_dump())
    db.commit()
    return 'blog has been updated.'
