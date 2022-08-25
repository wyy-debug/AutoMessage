from flask import request
from app import db
from app.message import message_bp
from app.message.models import Message
from app.message.schema import MessageSchema
from app.utils.responses import response_with
from app.utils import responses as resp
from flask_jwt_extended import jwt_required

# 创建短信
@message_bp.route('/',methods=['POST'])
def create_message():
    try:
        data = request.get_json()
        message_schema = MessageSchema()
        message = message_schema.load(data)
        result = message_schema.dump(message.create())
        return response_with(resp.SUCCESS_201,value={"message":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

