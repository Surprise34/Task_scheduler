# task_scheduler
Grid-Cloud spring 2018
https://imgur.com/a/uNvkgrE

# How to start work with app:
Was using PostgreSQL as db, so u have to install it to work with application.

-postgres=# CREATE DATABASE task_scheduler;

-postgres=# CREATE USER admin WITH password 'admin';

-postgres=# GRANT ALL privileges ON DATABASE task_scheduler TO admin;

$ git clone https://github.com/Surprise34/task_scheduler.git

$ cd task_scheduler

$ source myvenv/bin/activate

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py runserver


