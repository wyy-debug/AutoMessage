from flask import request
from app import db
from app.devicerelationnumber import devicerelationnumber_bp
from app.devicerelationnumber.models import DeviceRelationNumber
from app.devicerelationnumber.schema import DeviceRelationNumberSchema
from app.utils.responses import response_with
from app.utils import responses as resp
import app.utils.gol as gol
from flask_jwt_extended import jwt_required

# 创建手机
@devicerelationnumber_bp.route('/',methods=['POST'])
def create_device():
    try:
        data = request.get_json()
        device_schema = DeviceRelationNumberSchema()
        device = device_schema.load(data)
        result = device_schema.dump(device.create())
        return response_with(resp.SUCCESS_201,value={"device":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

