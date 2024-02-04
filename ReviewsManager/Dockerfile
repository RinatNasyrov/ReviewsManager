FROM python:3.12.1-alpine3.18
RUN mkdir reviews_docker
WORKDIR reviews_docker
ADD . /reviews_docker/
ADD .env.docker /reviews_docker/.env
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000