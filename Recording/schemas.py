from marshmallow import Schema, fields

class ItemSchema(Schema):
    # dump_only is something we only ever return in the API
    #  not used for validation
    id = fields.Str(dump_only=True)
    # because we accept name through the JSON payload, add req  if req
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


