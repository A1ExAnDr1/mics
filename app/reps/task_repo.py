from uuid import UUID

from app.models.task import Task


tasks: list[Task] = []


class TaskRepo():

    def get_tasks(self) -> list[Task]:
        return tasks

    def get_task_by_id(self, id: UUID) -> Task:
        for d in tasks:
            if d.id == id:
                return d
        raise KeyError

    def create_task(self, task: Task) -> Task:
        if len([d for d in tasks if d.id == task.id]) > 0:
            raise KeyError
        tasks.append(task)
        return task

    def set_status(self, task: Task) -> Task:
        for d in tasks:
            if d.id == task.id:
                d.status = task.status
                break
        return task

    def set_user(self, task: Task) -> Task:
        for d in tasks:
            if d.id == task.id:
                d.tastuser = task.taskuser
                break

        return task
