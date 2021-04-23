# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt


RUN mkdir /app
COPY ./Inurse_backend /app
WORKDIR /app
