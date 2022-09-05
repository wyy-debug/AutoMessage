from marshmallow import fields
import app
from app.device.models import Device
from app import db



class DeviceSchema(app.marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Device
        sqla_session = db.session
        load_instance = True

    id = fields.Number(dump_only=True)
    device_name = fields.String(required=True)
    device_number = fields.String(required=True)
