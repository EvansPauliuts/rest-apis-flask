from marshmallow import fields

from .plain import PlainStoreSchema, PlainTagSchema, PlainItemSchema


class StoreSchema(PlainStoreSchema):
    items = fields.List(
        fields.Nested(PlainItemSchema()),
        dump_only=True,
    )
    tags = fields.List(
        fields.Nested(PlainTagSchema()),
        dump_only=True,
    )
