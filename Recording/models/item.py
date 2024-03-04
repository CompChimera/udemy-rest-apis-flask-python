from db import db

class ItemModel(db.Model):
    # mapping from row in table to python obj
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float(2), unique=False, nullable=False )
    name = db.Column(db.String(80), nullable=False )
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"),  unique=False, nullable=False)
    # when we have a keythat's connected to the stores table, we can map to that table
    # Because the StoreModel says it's connected to the stores table
    #  back_populates means that store.py will have an items relationship
    store = db.relationship("StoreModel", back_populates="items")
    tags = db.relationship("TagModel", back_populates="items", secondary="items_tags")