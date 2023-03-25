# 本番用
FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
COPY nginx/nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080

RUN python manage.py migrate 

CMD ["gunicorn", "--reload", "-b", ":8080", "portfolio.wsgi:application","-w","2","-k","gevent"]