from flask import request
import json
from app import db
from app.message import message_bp
from app.message.models import Message
from app.message.schema import MessageSchema
from app.numberrelationmessage.models import NumberRelationMessage
from app.utils.responses import response_with
from app.utils import responses as resp
import app.utils.gol as gol
from flask_jwt_extended import jwt_required

# 创建短信
@message_bp.route('/',methods=['POST'])
def add_message():
    try:
        data = request.data.decode('UTF-8')
        message_data = json.loads(data)
        message_text = {}
        message_text["message_text"] = message_data["message_text"]
        message_schema = MessageSchema()
        message = message_schema.load(message_text)
        result = message_schema.dump(message.create())
        device_id = message_data["device_id"]
        NumberRelationMessage.add_relation(device_id,result["id"])
        return response_with(resp.SUCCESS_201,value={"result":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

@message_bp.route('/<int:device_id>',methods=['GET'])
def get_messages(device_id):
  messages_id_list = []
  messages_id = NumberRelationMessage.get_messages_id(device_id)
  for i in messages_id:
    messages_id_list.append(i.message_id)
  fetched = Message.query.filter(Message.id.in_(messages_id_list,)).all()
  message_schema = MessageSchema(many=True, only=['id', 'message_text'])
  messages = message_schema.dump(fetched)
  return response_with(resp.SUCCESS_200, value={"messages": messages})
