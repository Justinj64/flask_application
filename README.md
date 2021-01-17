# Flask Application with SqlAchemy | Sqlite3, Celery + RabbitMQ

## Tested on:
   Windows 10 | Ubuntu 18.04
   Python 3.8
   Celery 5.0.5
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
3) Make credential and other respective changes in **.env** file present at root.

4) Create Virtual Environment.

    ```
     python3 -m venv env

     .\env\Scripts\activate
     ```
5) Install requirements.txt file from activated virtual environment.

     ```
     pip install -r requirements.txt
6) Ensure rabbitMQ is working and start celery worker.
   ```
    celery -A app.celery worker --loglevel=info -P gevent   (Windows)

    celery -A app.celery worker --loglevel=info             (Ubuntu)
   ```
    As I initially tested on Windows I had to pass the gevent argument as celery(4.0+) is not supported on windows
    (https://docs.celeryproject.org/en/stable/faq.html#windows) and it 
    leads to conflict at times.

7) Once celery is up and running , on a new console , execute:
   ``` 
    python app.py
   ```

## Usage
1) Import the Postman collection as it  contains all the necessary API endpoints.
2) Make sure variables are set in the .env file
3) Configuration for Exchange and queues are set in **queues.py**.
## Notes
Schema for the table and its attributes is handled in the code itself. Once the initialization request is hit (refer postman collection), a file 'data.db' will be created, which will act as a SQLite engine.