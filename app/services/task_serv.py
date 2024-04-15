from uuid import UUID
from datetime import datetime
from app.models.task import Task, TaskStatuses
from app.reps.task_repo import TaskRepo
from app.reps.user_repo import UsersRepo

class TaskServise():
    task_r:TaskRepo
    user_r:UsersRepo

    def __init__(self) -> None:
        self.task_r = TaskRepo()
        self.user_r = UsersRepo()

    def get_tasks(self) -> list[Task]:
        return self.task_r.get_tasks()

    def create_task(self, task_id: UUID, date: datetime, name: str) -> Task:
        task = Task(id=task_id, date=date,name=name,status=TaskStatuses.CREATED)
        return self.task_r.create_task(task)

    def activate_task(self, id:UUID) -> Task:
        task = self.task_r.get_task_by_id(id)
        if task.status !=TaskStatuses.CREATED:
            raise ValueError
        task.status = TaskStatuses.ACTIVATED
        return self.task_r.set_status(task)

    def set_user(self, task_id, user_id) -> Task:
        task = self.task_r.get_task_by_id(task_id)
        try:
            user = self.user_r.get_user_by_id(user_id)
        except KeyError:
            raise ValueError
        if task.status != TaskStatuses.ACTIVATED:
            raise ValueError
        task.user = user
        return self.task_r.set_user(user)

    def get_users(self):
        return self.user_r.get_users()
   # def get_user_by_id(self):
