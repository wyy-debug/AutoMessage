from marshmallow import fields

import app
from app.users.models import User
from app import db

class UserSchema(app.marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True

    id = fields.Number(dump_only=True)
    username = fields.String(required=True)
