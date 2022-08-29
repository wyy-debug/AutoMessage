from marshmallow import fields
import app
from app.device.models import Device
from app.partition.schema import Partition
from app import db



class DeviceSchema(app.marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Device
        sqla_session = db.session
        load_instance = True

    id = fields.Number(dump_only=True)
    devices_name = fields.String(required=True)
    partition = fields.Nested(Partition, many=True, only=['id', 'partition', 'devices_id', 'number'])
