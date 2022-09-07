import json

from flask import request
from app import db
from app.device import device_bp
from app.device.models import Device
from app.device.schema import DeviceSchema
from app.utils.responses import response_with
from app.utils import responses as resp
import app.utils.gol as gol
from app.devicerelationnumber.models import DeviceRelationNumber
from app.utils.poco_device import Poco
from flask_jwt_extended import jwt_required

# 增加手机设备
@device_bp.route('/',methods=['POST'])
def add_device():
    try:
        data = request.data.decode('UTF-8')
        device_data = json.loads(data)
        device_schema = DeviceSchema()
        device = device_schema.load(device_data)
        result = device_schema.dump(device.create())
        return response_with(resp.SUCCESS_201,value={"device":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


# 获取手机列表
@device_bp.route('/',methods=['GET'])
def get_device():
  fetched = Device.query.all()
  device_schema = DeviceSchema(many=True, only=['id', 'device_name', 'device_number'])
  devices = device_schema.dump(fetched)
  return response_with(resp.SUCCESS_200, value={"devices": devices})

# 更新手机信息
@device_bp.route('/<int:id>',methods=['PUT'])
def update_device():
  data = request.get_json()
  get_device = Device.query.get_or_404(id)
  get_device.device_name = data['device_name']
  get_device.device_number = data['device_number']
  db.session.add(get_device)
  db.session.commit()
  device_schema = DeviceSchema()
  device = device_schema.dump(get_device)
  return response_with(resp.SUCCESS_200, value={"device": device})

# 删除手机
@device_bp.route('/<int:id>',methods=['DELETE'])
def delete_device(id):
  get_device = Device.query.get_or_404(id)
  db.session.delete(get_device)
  db.session.commit()
  DeviceRelationNumber.delete_number_id(id)
  return response_with(resp.SUCCESS_204)

# 切卡
@device_bp.route('/changedevices/',methods=['POST'])
def change_devices():
  try:
    data = request.data.decode('UTF-8')
    device_data = json.loads(data)
    device_number = device_data['device_number']
    phone_part = device_data['number_parition']
    phone_sim = device_data['number_semicolon']
    poco_device = Poco(device_number)
    if(poco_device.change_call(phone_part, phone_sim)):
      return response_with(resp.SUCCESS_200,value={"mes": "succss"})
    else:
      return response_with(resp.SUCCESS_200, value={"mes": "fail"})
  except Exception as e:
    gol.set_value("phone_state", "free")
