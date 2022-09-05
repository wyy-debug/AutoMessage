from flask import request
from app import db
from app.number import number_bp
from app.number.models import Number
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

# 查询手机
# 获取手机列表
@number_bp.route('/<int:number>',methods=['GET'])
def get_devices(number):
  fetched = Number.query.get_or_404(number)
  number_schema = NumberSchema()
  number = number_schema.dump(fetched)
  return response_with(resp.SUCCESS_200, value={"author": number})
