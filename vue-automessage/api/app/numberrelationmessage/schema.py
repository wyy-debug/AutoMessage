from marshmallow import fields
import app
from app.numberrelationmessage.models import NumberRelationMessage
from app import db



class NumberRelationMessageSchema(app.marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = NumberRelationMessage
        sqla_session = db.session
        load_instance = True

    id = fields.Number(dump_only=True)
    number_id = fields.Integer(required=True)
    message_id = fields.Integer(required=True)
