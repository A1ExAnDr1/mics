from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID

from app.schem.base_schem import Base
from app.models.task import TaskStatuses


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    status = Column(Enum(TaskStatuses), nullable=False)
    taskuser_id = Column(UUID(as_uuid=True), nullable=True)
