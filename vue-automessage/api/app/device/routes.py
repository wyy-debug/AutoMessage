from flask import request
from app import db
from app.device import device_bp
from app.device.models import Device
from app.device.schema import DeviceSchema
from app.utils.responses import response_with
from app.utils import responses as resp
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
