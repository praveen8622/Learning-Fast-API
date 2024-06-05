from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, token   
from ..database import get_db
from .. hashing import Hash

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credentials')
    # Simply return the user details (or a subset of them)

    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid password')
    
    access_token = token.create_access_token(
        data={"sub": user.email})
    return schemas.Token(access_token=access_token, token_type="bearer")