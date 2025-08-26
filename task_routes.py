from fastapi import Depends, HTTPException, APIRouter
from database import get_session
from task import TaskBase, TaskRead, TaskCreate
from sqlmodel import Session, select

router = APIRouter()

@router.post("/task")
def create_task(payload: TaskBase, session: Session = Depends(get_session)):
    task = TaskCreate(**payload.model_dump())
    session.add(task)
    session.commit()
    session.refresh(task)
    return {"message": f"Task is created"}
    
@router.get("/tasks/{id}", response_model=TaskRead)
def get_task(id: int, session: Session = Depends(get_session)): 
    found_task = session.get(TaskCreate, id)
    if not found_task:
        raise HTTPException(status_code=404, detail="Task does not exist")
    return found_task

@router.get("/tasks", response_model=list[TaskRead])
def get_all_tasks(session: Session = Depends(get_session)): 
    found_tasks = session.exec(select(TaskCreate)).all()
    if not found_tasks:
        raise HTTPException(status_code=404, detail="No available tasks")
    return found_tasks

@router.patch("/tasks/{id}")
def update_task(id: int, payload: TaskBase, session: Session = Depends(get_session)): 
    found_task = session.get(TaskCreate, id)
    if not found_task:
        raise HTTPException(status_code=406, detail="Task does not exist")
    task = TaskCreate(**payload.model_dump())
    task_data = task.model_dump(exclude_unset=True)
    found_task.sqlmodel_update(task_data)
    session.add(found_task)
    session.commit()
    session.refresh(found_task)
    return {"message": f"Task {id} is updated"}

@router.delete("/tasks/{id}")
def delete_task(id: int, session: Session = Depends(get_session)): 
    found_task = session.get(TaskCreate, id)
    if not found_task:
        raise HTTPException(status_code=406, detail="Task does not exist")
    session.delete(found_task)
    session.commit()
    return {"message": f"Task {id} deleted"}