from marshmallow import fields
import app
from app.device.models import Device
from app.message.schema import Message
from app import db



class DeviceSchema(app.marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Device
        sqla_session = db.session
        load_instance = True

    id = fields.Number(dump_only=True)
    devices_id = fields.String(required=True)
    phone_number = fields.Integer(required=True)
    messages = fields.Nested(Message, many=True, only=['id', 'recv_from_number', 'message_text', 'recv_time', 'devices_id'])
