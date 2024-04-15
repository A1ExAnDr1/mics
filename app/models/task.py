import enum
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.models.user import User
class TaskStatuses(enum.Enum):
    CREATED = 'created'
    ACTIVATED = 'activated'
    DONE = 'done'
    CANCELED = 'canceled'

class Task(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str
    date: datetime
    status: TaskStatuses
    taskuser: User | None = None

class CreateTaskRequest(BaseModel):
    order_id:UUID
    address:str
    date:str
