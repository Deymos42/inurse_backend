# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-alpine
ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /app
COPY ./inurse /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*


RUN mkdir /var/log/django
RUN touch /var/log/django/myapp.log
RUN adduser -D user
RUN chown -R user:user /app
RUN chmod -R 777 /var/log/django/myapp.log
RUN chmod -R 755 /app/APIapp
RUN rm -rf /app/APIapp/static/APIapp

USER user

CMD ["entrypoint.sh"]