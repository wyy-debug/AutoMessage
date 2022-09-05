import datetime

from flask import request
from app import db
from app.message import message_bp
from app.message.models import Message
from app.message.schema import MessageSchema
from app.utils.responses import response_with
from app.utils import responses as resp
import app.utils.gol as gol
from flask_jwt_extended import jwt_required

# 创建短信
@message_bp.route('/',methods=['POST'])
def create_message():
    try:
        data = request.get_json()
        data["recv_from_number"] = gol.get_value("phone_number")
        data["recv_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message_schema = MessageSchema()
        message = message_schema.load(data)
        result = message_schema.dump(message.create())
        return response_with(resp.SUCCESS_201,value={"message":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

# 获取短信列表
@message_bp.route('/',methods=['GET'])
def get_messages():
  fetched = Message.query.order_by(Message.recv_time.desc()).limit(50)
  message_schema = MessageSchema(many=True, only=['id', 'recv_from_number', 'message_text'])
  messages = message_schema.dump(fetched)
  return response_with(resp.SUCCESS_200, value={"messages": messages})
