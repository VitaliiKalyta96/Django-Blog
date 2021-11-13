FROM python:3.9.7-buster
ENV PYTHONUNBUFFERED 1
WORKDIR /application
COPY requirements.txt /application/requirements.txt
RUN pip install -r requirements.txt

CMD python3 manage.py runserver 0.0.0.0:8000
