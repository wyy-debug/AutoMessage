import json
from flask import request
from app import db
from app.number import number_bp
from app.number.models import Number
from app.number.schema import NumberSchema
from app.utils.responses import response_with
from app.utils import responses as resp
from app.devicerelationnumber.models import DeviceRelationNumber
from app.devicerelationnumber.schema import DeviceRelationNumberSchema
from flask_jwt_extended import jwt_required

# 创建手机
@number_bp.route('/<int:device_id>',methods=['POST'])
def add_number(device_id):
    try:
        data = request.data.decode('UTF-8')
        number_data = json.loads(data)
        number_schema = NumberSchema()
        number = number_schema.load(number_data)
        result = number_schema.dump(number.create())
        DeviceRelationNumber.add_relation(device_id, result["id"])
        return response_with(resp.SUCCESS_201,value={"result":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

@number_bp.route('/<int:device_id>',methods=['GET'])
def get_numbers(device_id):
  numbers_id_list = []
  numbers_id = DeviceRelationNumber.get_numbers_id(device_id)
  for i in numbers_id:
    numbers_id_list.append(i.number_id)
  fetched = Number.query.filter(Number.id.in_(numbers_id_list,)).all()
  numbers_schema = NumberSchema(many=True,only=['id','number_parition','number_semicolon','number_phone'])
  numbers = numbers_schema.dump(fetched)
  return response_with(resp.SUCCESS_200, value={"numbers": numbers})
