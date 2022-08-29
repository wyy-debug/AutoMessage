from flask import request
from app import db
from app.device import device_bp
from app.device.models import Device
from app.device.schema import DeviceSchema
from app.utils.responses import response_with
from app.utils import responses as resp
from app.partition.models import Partition
from app.partition.schema import PartitionSchema
from flask_jwt_extended import jwt_required

# 创建手机
@device_bp.route('/',methods=['POST'])
def create_device():
    try:
        data = request.get_json()
        device_schema = DeviceSchema()
        device = device_schema.load(data)
        result = device_schema.dump(device.create())
        return response_with(resp.SUCCESS_201,value={"device":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


# 获取手机列表
@device_bp.route('/',methods=['GET'])
def get_devices():
  options = []
  fetched = Device.query.all()
  for i in fetched:
    options.append({"value":i.devices_name, "label":i.devices_name, "children":[]})
    for j in i.partition:
      options[-1]["children"].append({"value":j.partition, "label":j.partition, "children":[]})
      for z in j.number:
        options[-1]["children"][-1]["children"].append({"value":z.number_type, "label":z.number_type, "children":[{"value":z.number, "label":z.number}]})

  device_schema = DeviceSchema(many=True, only=['id', 'devices_name'])
  devices = device_schema.dump(fetched)
  return response_with(resp.SUCCESS_200, value={"options": options})

# 切号
@device_bp.route('/changedevices/',methods=['POST'])
def change_devices():
  try:
    data = request.get_json()
    print(data)
    return response_with(resp.SUCCESS_200)
  except Exception as e:
    print(e)
    pass