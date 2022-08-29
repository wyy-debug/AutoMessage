from marshmallow import fields
import app
from app.partition.models import Partition
from app.number.schema import Number
from app import db



class PartitionSchema(app.marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Partition
        sqla_session = db.session
        load_instance = True

    id = fields.Number(dump_only=True)
    partition = fields.String(required=True)
    devices_id = fields.Integer(dump_only=True)
    number = fields.Nested(Number, many=True, only=['id', 'number', 'partition_id', 'messages'])
