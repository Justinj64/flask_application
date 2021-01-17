import os
from dotenv import load_dotenv
import json

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') 
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
    EXCHANGE_NAME = os.environ.get('EXCHANGE_NAME')
    EXCHANGE_TYPE = os.environ.get('EXCHANGE_TYPE')
    ITEM_ROUTING_KEY = os.environ.get('ITEM_ROUTING_KEY')
    ITEM_QUEUE_NAME = os.environ.get('ITEM_QUEUE_NAME')
    TASK_FILES = json.loads(os.environ.get('TASK_FILES'))
    TASK_SERIALIZER = os.environ.get('TASK_SERIALIZER')
    RESULT_SERIALIZER = os.environ.get('RESULT_SERIALIZER')
    ACCEPT_CONTENT = json.loads(os.environ.get('ACCEPT_CONTENT'))
