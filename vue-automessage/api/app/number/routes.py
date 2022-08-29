from flask import request
from app import db
from app.number import number_bp
from app.number.schema import NumberSchema
from app.utils.responses import response_with
from app.utils import responses as resp
from flask_jwt_extended import jwt_required

# 创建手机
@number_bp.route('/',methods=['POST'])
def create_number():
    try:
        data = request.get_json()
        number_schema = NumberSchema()
        number = number_schema.load(data)
        result = number_schema.dump(number.create())
        return response_with(resp.SUCCESS_201,value={"number":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
