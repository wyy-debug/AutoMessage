from marshmallow import fields
import app
from app.project.models import Project
from app.version.schema import VersionSchema
from app import db



class ProjectSchema(app.marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Project
        sqla_session = db.session
        load_instance = True

    id = fields.Number(dump_only=True)
    project_name = fields.String(required=True)
    versions = fields.Nested(VersionSchema, many=True, only=['id', 'name', 'bulletin_boards'])
