FROM python:3.11
WORKDIR /motekatuApp

COPY . .
RUN pip install django
RUN pip install mysqlclient
RUN pip install Pillow
RUN pip install boto3
RUN pip install django-storages
RUN pip install django-environ

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
