FROM python:3.10

# Выбор папки, в которой будет вестись работа
WORKDIR /code

# Установка зависимостей проекта
COPY ./requirements.txt /code/
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Перенос проекта в образ
COPY ./app /code/app

# Копирование файлов alembic

COPY ./alembic.ini /code/alembic.ini


#RUN chmod +x /code/entrypoint.sh

EXPOSE 8000

#CMD ["/bin/sh", "-c", \alembic upgrade head && \ uvicornvmain:app --host 0.0.0.0 --port 80"]


#ENTRYPOINT ["/code/entrypoint.sh"]
