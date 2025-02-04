from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.auth_service import authenticate_user, create_access_token, get_password_hash
from src.crud import user as user_crud
from src.schemas.users import UserCreate, UserLogin
from src.depends import get_db

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    if user_crud.get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    user.password = get_password_hash(user.password)
    return user_crud.create_user(db, user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token = create_access_token(data={"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}
