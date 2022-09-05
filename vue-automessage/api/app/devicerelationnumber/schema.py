from marshmallow import fields
import app
from app.devicerelationnumber.models import DeviceRelationNumber
from app import db



class DeviceRelationNumberSchema(app.marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = DeviceRelationNumber
        sqla_session = db.session
        load_instance = True

    id = fields.Number(dump_only=True)
    device_id = fields.Integer(required=True)
    number_id = fields.Integer(required=True)
