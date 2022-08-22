import app
from app.questions.models import Question
from marshmallow import fields
from app import db

class QuestionSchema(app.marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Question
        sqla_session = db.session
        load_instance = True

    id = fields.Number(dump_only=True)
    question_msg = fields.String(required=True)
    question_type = fields.String(required=True)
    question_author = fields.String(required=True)
    version_id = fields.Integer()
