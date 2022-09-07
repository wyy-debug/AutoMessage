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
    gol.set_value("phone_state", "busy")
    data = request.get_json()
    # 处理data
    # part = '1区'
    # sim = '1'
    # phone_number = '1xxxxxxxx'
    # phone_poco = gol.get_value("phone_poco")
    #
    # if(phone_poco.change_call(part='1区',sim='1')):
    #   gol.set_value("phone_part", part)
    #   gol.set_value("phone_sim", sim)
    #   gol.set_value("phone_number", phone_number)
    #
    # gol.set_value("phone_state", "free")
    return response_with(resp.SUCCESS_200)
  except Exception as e:
    gol.set_value("phone_state", "free")
