import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') 
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
    ENCHANGE_NAME = os.environ.get('ENCHANGE_NAME')
    EXCHANGE_TYPE = os.environ.get('ENCHANGE_TYPE')
    ITEM_ROUTING_KEY = os.environ.get('ITEM_ROUTING_KEY')
    ITEM_QUEUE_NAME = os.environ.get('ITEM_QUEUE_NAME')


