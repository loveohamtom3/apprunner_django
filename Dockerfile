# 本番用
FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

EXPOSE 8002

CMD ["gunicorn", "--reload", "-b", ":8002", "config.wsgi:application","-w","2","-k","gevent"]