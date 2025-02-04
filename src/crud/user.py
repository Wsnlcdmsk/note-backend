from sqlalchemy.orm import Session
from src.models import User 
from src.schemas.users import UserCreate

def create_user(db: Session, user_data: UserCreate):
    db_user = User(username=user_data.username, email=user_data.email, hashed_password=user_data.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user
