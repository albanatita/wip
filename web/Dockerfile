FROM python:3.6.3
ENV PYTHONUNBUFFERED 1
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
