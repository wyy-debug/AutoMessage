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
    number_parition = fields.String(required=True)
    number_semicolon = fields.String(required=True)
    number_phone = fields.Integer(required=True)
