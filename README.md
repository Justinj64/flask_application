# Flask Application with SqlAchemy | Sqlite3, Celery + RabbitMQ

## Tested on:
Windows 10

Python 3.8

RabbitMq 3.8.9
## Installation

1) Install RabbitMQ from the link given below

   https://www.rabbitmq.com/download.html

2) Configure RabbitMQ for Celery
   ```
    sudo rabbitmqctl add_user username password

    sudo rabbitmqctl add_vhost sample_host

    sudo rabbitmqctl set_user_tags username administrator
  
    sudo rabbitmqctl set_permissions -p sample_host username ".*" ".*" ".*"
   ```
3) Make credential and other respective changes in .env file present at root.

4) Create Virtual Environment.

   ```
   python3 -m venv env

   .\env\Scripts\activate
    ```
5) Install requirements.txt file from inside virtual enviroment 

   ```pip install -r requirements.txt ```

6) Ensure rabbitMQ is working and start celery worker.
   ```
    celery -A app.celery worker --loglevel=info -P gevent
   ```
    As I was on Windows I had to pass the gevent argument as celery does not support windows 4.0+       
    (https://docs.celeryproject.org/en/stable/faq.html#windows) and it 
    leads to conflict at times.

7) Once celery is up and running , on a new console , execute:
   ``` 
    python app.py
   ```