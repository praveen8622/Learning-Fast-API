from fastapi import APIRouter, Depends,Response,status ,HTTPException
from typing import List
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from .. repository import blog_repo



router = APIRouter(
    prefix='/blog',
    tags= ['Blogs']
)

@router.get('/', response_model=List [schemas.Showblog])
def getdata(db: Session = Depends(get_db)):
    return blog_repo.get_allblog(db)

@router.get('/{id}',status_code=200, response_model=schemas.Showblog)
def allblogs(id, db: Session=Depends(get_db)):
   return blog_repo.show(db,id)


@router.post('/', response_model=schemas.Blog,status_code=201)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog_repo.create(db, request)

    

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(id, db:Session = Depends(get_db)):
   return blog_repo.destroy(db, id )

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, request:schemas.Blog,db:Session = Depends(get_db)):
    return blog_repo.update(db, id, request)
