
from marshmallow import fields
import app
from app.message.models import Message
from app import db



class MessageSchema(app.marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Message
        sqla_session = db.session
        load_instance = True

    id = fields.Number(dump_only=True)
    recv_from_number = fields.Integer(required=True)
    message_text = fields.String(required=True)
    recv_time = fields.DateTime(required=False)
    numbers_id = fields.Integer(dump_only=False)
