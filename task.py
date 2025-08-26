from sqlmodel import Field, SQLModel
from typing import Optional

class TaskBase(SQLModel):
    title: str
    description: str
    priority: int
    status: str | None=Field(default = "pending")

class TaskCreate(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class TaskRead(TaskBase):
    id: int | None = Field(default=None, primary_key=True)