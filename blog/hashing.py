from passlib.context import CryptContext

pwd_cntxt = CryptContext(schemes=['bcrypt'], deprecated ='auto')

class Hash():
    def bcrypt(password:str):
        return pwd_cntxt.hash(password)
    
    def verify_password(plain_password, hashed_password):
        return pwd_cntxt.verify(plain_password, hashed_password)
