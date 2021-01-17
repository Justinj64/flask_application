import sqlite3
from db import db

## itemModel class to bridge sql schema
class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), default="pending")
    item = db.Column(db.String(20))

    def __init__(self,item):
        self.item = item
        
    def json(self):
        return {"id":self.id,"item":self.item,"status":self.status} 

    @classmethod
    def find_by_id(cls,id):
        return cls.query.get(id)

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(item=name).first()

    @classmethod
    def find(cls, id, name):
        return cls.query.filter_by(id=id, item=name).first()        

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def del_from_db(self):
        db.session.delete(self)
        db.session.commit()

     