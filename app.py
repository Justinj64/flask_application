from flask import Flask
from flask_restful import Api
from celery import Celery
from resources.items import Item, ItemList, ItemInsert, Initialize
from db import db
from config import Config
from queues import task_queues

# app initialization
app = Flask(__name__)

# sqlalchemy params
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

# celery params and initialization
app.config['CELERY_BROKER_URL'] = Config.CELERY_BROKER_URL
app.config['CELERY_RESULT_BACKEND'] = Config.CELERY_RESULT_BACKEND

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'], include=Config.TASK_FILES)
celery.conf.update(
    task_serializer=Config.TASK_SERIALIZER,
    result_serializer=Config.RESULT_SERIALIZER,
    accept_content=Config.ACCEPT_CONTENT,
)
celery.conf.task_queues = task_queues

api = Api(app)

# decorator autocreates tables from models
@app.before_first_request
def create_tables():
    db.create_all()

# adding resource for various Methods
api.add_resource(Initialize, "/")
api.add_resource(ItemList, "/items")
api.add_resource(Item, "/item/<int:id>")
api.add_resource(ItemInsert, "/items")

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True, port=5000)