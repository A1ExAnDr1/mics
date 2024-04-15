from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Body

from app.services.task_serv import TaskServise
from app.models.task import Task
from app.reps.user_repo import users

task_rout = APIRouter(prefix='/task', tags=['Task']) #prefix='/task', tags=['Task']
@task_rout.get("/tasks/")
def get_tasks(task_serv: TaskServise = Depends(TaskServise)) -> list[Task]:
    return task_serv.get_tasks()

@task_rout.get("/users/")
def get_users():
    return users
@task_rout.post('/{id}/appoint')
def set_taskuser(id: UUID,user_id: UUID = Body(embed=True),task_serv: TaskServise = Depends(TaskServise)) -> Task:
    try:
        task = task_serv.set_user(id, user_id)
        return task.dict()
    except KeyError:
        raise HTTPException(404, f'Task with id={id} not found')
    except ValueError:
        raise HTTPException(400)
@task_rout.post('/{id}/activate')
def activate_task(id: UUID, task_serv: TaskServise = Depends(TaskServise)) -> Task:
    try:
        task = task_serv.active_task(id)
        return task.dict
    except KeyError:
        raise HTTPException(404, f'Task with id={id} not found')
    except ValueError:
        raise HTTPException(400, f'Task with id={id} can\'t be activated')

@task_rout.post('/{id}/finish')
def finish_delivery(id: UUID, task_serv: TaskServise = Depends(TaskServise)) -> Task:
    try:
        task = task_serv.finish_task(id)
        return task.dict()
    except KeyError:
        raise HTTPException(404, f'TasK with id={id} not found')
    except ValueError:
        raise HTTPException(400, f'Task with id={id} can\'t be finished')

@task_rout.post('/{id}/cancel')
def cancel_delivery(id: UUID, task_serv: TaskServise = Depends(TaskServise)) -> Task:
    try:
        task = task_serv.cancel_task(id)
        return task.dict()
    except KeyError:
        raise HTTPException(404, f'Task with id={id} not found')
    except ValueError:
        raise HTTPException(400, f'Task with id={id} can\'t be canceled')
