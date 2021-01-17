from flask_restful import Resource, reqparse
from flask import request
from models.item import ItemModel
from config import Config

class Initialize(Resource):
    def get(self):
        return "Welcome to Flask App"

## class for handling GET, PUT and DELETE
class Item(Resource):
    parser = reqparse.RequestParser()
    def get(self, id):
        item = ItemModel.find_by_id(id)
        if item:
            return item.json()
        return {"message":"Item not found"},404

    def put(self, id):
        data = request.get_json(force=True)
        item = ItemModel.find_by_id(id)
        if item:
            item.item = data['item']
        else:
            item = ItemModel(**data)
        item.save_to_db()
        return item.json()

    def delete(self, id):
        item = ItemModel.find_by_id(id)
        if item:
            item.del_from_db()
            return {'message': 'Item deleted.'}
        return {'message': 'Item not found.'}, 404

## class for Handling POST
class ItemInsert(Resource):
    def post(self):
        from tasks import update_row        ## Import to avoid cyclic import        
        data = request.get_json(force=True)
        item = ItemModel(**data)
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500
        ## call to celery task
        file_task = update_row.apply_async((item.json(),), exchange=Config.ENCHANGE_NAME, routing_key=Config.ITEM_ROUTING_KEY)
        return item.json(), 202

## class to retrieve all items
class ItemList(Resource):
    def get(self):
        return {"items":list(map(lambda x : x.json(),ItemModel.query.all()))}




