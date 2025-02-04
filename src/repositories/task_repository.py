from sqlalchemy.orm import Session
from models import Task

def create_task(db: Session, task_data, user_id: int):
    db_task = Task(**task_data.dict(), user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks_by_user(db: Session, user_id: int):
    return db.query(Task).filter(Task.user_id == user_id).all()
