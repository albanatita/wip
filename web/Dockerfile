FROM python:3.6.3
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST "redis"
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
RUN python manage.py migrate

FROM python:3.4
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST "redis"
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
RUN python manage.py migrate