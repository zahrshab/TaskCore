from fastapi import Depends, HTTPException, APIRouter
from database import get_session
from task import Task
from sqlmodel import Session, select

router = APIRouter()

@router.post("/task")
def create_task(task: Task, session: Session = Depends(get_session)):
    if get_task(task.id, session): 
        raise HTTPException(status_code=406, detail="Task already exists")
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
    
@router.get("/tasks/{id}", response_model=Task)
def get_task(id: int, session: Session = Depends(get_session)): 
    found_task = session.get(Task, id)
    if not found_task:
        raise HTTPException(status_code=404, detail="Task does not exist")
    return found_task

@router.get("/tasks", response_model=list[Task])
def get_all_tasks(session: Session = Depends(get_session)): 
    found_tasks = session.exec(select(Task)).all()
    if not found_tasks:
        raise HTTPException(status_code=404, detail="No available tasks")
    return found_tasks

@router.delete("/tasks/{id}")
def delete_task(id: int, session: Session = Depends(get_session)): 
    found_task = session.get(Task, id)
    if not found_task:
        raise HTTPException(status_code=406, detail="Task does not exist")
    session.delete(found_task)
    session.commit()
    return {"message": f"Item {id} deleted"}