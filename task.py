from sqlmodel import Field, SQLModel

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    priority: int
    status: str | None=Field(default = "pending")
