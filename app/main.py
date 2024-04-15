import asyncio

from fastapi import FastAPI


import rabbitmq
from app.endpoints.task_rout import task_rout

app = FastAPI(title='Task Serv', prefix='/api')  #title='Task Serv', prefix='/api'

app.include_router(task_rout, prefix='/api') #task_rout, prefix='/api'
@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(rabbitmq.consume(loop))
    app.include_router(task_rout, prefix='/api')
