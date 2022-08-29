from flask import request
from app import db
from app.partition import partition_bp
from app.partition.schema import PartitionSchema
from app.utils.responses import response_with
from app.utils import responses as resp
from flask_jwt_extended import jwt_required

# 创建手机
@partition_bp.route('/',methods=['POST'])
def create_partition():
    try:
        data = request.get_json()
        partition_schema = PartitionSchema()
        partition = partition_schema.load(data)
        result = partition_schema.dump(partition.create())
        return response_with(resp.SUCCESS_201,value={"partition":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
