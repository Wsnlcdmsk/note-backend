from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from src.models import User
from src.depends import get_db
from src.config import SECRET_KEY, ALGORITHM 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        user_username: str = payload.get("sub")
        if user_username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        
        user = db.query(User).filter(User.username == user_username).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
