from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    # dump_only is something we only ever return in the API
    #  not used for validation
    id = fields.Str(dump_only=True)
    # because we accept name through the JSON payload, add req  if req
    # required also means it's required in both incoming and outgoing calls
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


