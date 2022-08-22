
from marshmallow import fields
import app
from app.version.models import Version
from app.questions.schema import QuestionSchema
from app import db



class VersionSchema(app.marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Version
        sqla_session = db.session
        load_instance = True

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    project_id = fields.Integer()
    bulletin_boards = fields.Nested(QuestionSchema, many=True, only=['id', 'name', 'questions'])
