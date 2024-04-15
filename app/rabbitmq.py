import json
import traceback
from asyncio import AbstractEventLoop
from aio_pika.abc import AbstractRobustConnection
from aio_pika import connect_robust, IncomingMessage

from app.reps.task_repo import TaskRepo
from settings import settings
from app.services.task_serv import TaskServise



async def process_created_order(msg: IncomingMessage):
    try:
        data = json.loads(msg.body.decode())
        TaskServise(TaskRepo()).create_task(data['uuid'],data['datetime'],data['name'])
    except:
        traceback.print_exc()
        await msg.ack()


async def process_paid_order(msg: IncomingMessage):
    try:
        data = json.loads(msg.body.decode())
        TaskServise(TaskRepo()).activate_task(data['id'])
    except:
        await msg.ack()
    pass


async def consume(loop: AbstractEventLoop) -> AbstractRobustConnection:
    connection = await connect_robust(settings.amqp_url, loop=loop)
    channel = await connection.channel()

    order_created_queue = await channel.declare_queue('task_order_created_queue', durable=True)
    order_queue = await channel.declare_queue('task_order_queue', durable=True)

    await order_created_queue.consume(process_created_order)
    await order_queue.consume(process_paid_order)
    print('Started RabbitMQ consuming...')

    return connection
