from db import db

class StoreModel(db.Model):
    # mapping from row in table to python obj
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False )
    # tells alchemy there's two ends of a relationship because of these lines in both files
    # Dynamic means they won't be fetched from DB until we tell it to
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
