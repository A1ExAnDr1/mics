import traceback
from uuid import UUID
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.task import Task
from app.schem.db_tasks import Task as DBTask
from app.reps.user_repo import UsersRepo


class TaskRepo():
    db: Session
    user_repo: UsersRepo

    def __init__(self) -> None:
        self.db = next(get_db())
        self.deliveryman_repo = UsersRepo()

    def _map_to_model(self, task: DBTask) -> Task:
        result = Task.from_orm(task)
        if task.taskuser_id != None:
            result.taskuser = self.user_repo.get_user_by_id(task.taskuser_id)

        return result

    def _map_to_schema(self, task: Task) -> DBTask:
        data = dict(task)
        del data['taskuser']
        data['taskuser_id'] = task.taskuser.id if task.taskuser != None else None
        result = DBTask(**data)

        return result

    def get_tasks(self) -> list[Task]:
        tasks = []
        for d in self.db.query(DBTask).all():
            tasks.append(self._map_to_model(d))
        return tasks

    def get_delivery_by_id(self, id: UUID) -> Task:
        task = self.db \
            .query(DBTask) \
            .filter(DBTask.id == id) \
            .first()

        if task == None:
            raise KeyError
        return self._map_to_model(task)

    def create_delivery(self, task: Task) -> Task:
        try:
            db_task = self._map_to_schema(task)
            self.db.add(db_task)
            self.db.commit()
            return self._map_to_model(db_task)
        except:
            traceback.print_exc()
            raise KeyError

    def set_status(self, task: Task) -> Task:
        db_task = self.db.query(DBTask).filter(
            DBTask.id == task.id).first()
        db_task.status = task.status
        self.db.commit()
        return self._map_to_model(db_task)

    def set_deliveryman(self, task: Task) -> Task:
        db_task = self.db.query(DBTask).filter(
            DBTask.id == task.id).first()
        db_task.taskuser_id = task.taskuser.id
        self.db.commit()
        return self._map_to_model(db_task)
