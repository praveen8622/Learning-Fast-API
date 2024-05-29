
from ..hashing import Hash
from fastapi import APIRouter, Depends,Response,status ,HTTPException
from typing import List
from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/user',
    tags=['users']
)

@router.post('/',status_code=201, response_model=schemas.Showuser, )
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name= request.name , email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/')
def getdata(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users