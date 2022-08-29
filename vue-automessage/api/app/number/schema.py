from marshmallow import fields
import app
from app.number.models import Number
from app.message.schema import Message
from app import db



class NumberSchema(app.marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Number
        sqla_session = db.session
        load_instance = True

    id = fields.Number(dump_only=True)
    number = fields.Integer(required=True)
    partition_id = fields.Integer(dump_only=True)
    messages = fields.Nested(Message, many=True, only=['id', 'recv_from_number', 'message_text', 'recv_time', 'devices_id'])
