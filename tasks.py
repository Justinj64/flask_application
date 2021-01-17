from app import app, celery
from models.item import ItemModel
from db import db

## celery task for updating status
@celery.task(name='tasks.update_row')
def update_row(data):
    db.init_app(app)
    with app.app_context():
        item = ItemModel.find(data['id'], data['item'])
        if item:
            item.status = "completed"
        try:
            item.save_to_db()
        except Exception as e:
            return {"message": "An error occurred celery task"}, 500
        return item.json()
