# src/routers/task.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.crud.task import get_tasks, create_task, update_task, delete_task
from src.schemas.task import Task, TaskCreate, TaskUpdate
from src.depends import get_db
from src.auth import get_current_user
from src.models import User

router = APIRouter()

@router.get("/tasks/", response_model=list[Task])
def read_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_tasks(db, user_id=current_user.id)

@router.post("/tasks/", response_model=Task)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_task(db, task=task, user_id=current_user.id)

@router.put("/tasks/{task_id}", response_model=Task)
def update_existing_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_task = update_task(db, task_id=task_id, task=task, user_id=current_user.id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/tasks/{task_id}", response_model=Task)
def delete_existing_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_task = delete_task(db, task_id=task_id, user_id=current_user.id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
