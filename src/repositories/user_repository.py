from sqlalchemy.orm import Session
from models import User

def create_user(db: Session, user_data):
    db_user = User(**user_data.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()
