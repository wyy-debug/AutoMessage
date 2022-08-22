from flask import request
from app import db
from app.version import version_bp
from app.version.models import Version
from app.version.schema import VersionSchema
from app.utils.responses import response_with
from app.utils import responses as resp
from app.questions.schema import QuestionSchema
from flask_jwt_extended import jwt_required

# 创建版本
@version_bp.route('/',methods=['POST'])
def create_version():
    try:
        data = request.get_json()
        version_schema = VersionSchema()
        version = version_schema.load(data)
        result = version_schema.dump(version.create())
        try:
          data = {"question_msg":"1","question_author":"1","question_type": "初始", "version_id": version.id}
          question_schema = QuestionSchema()
          question = question_schema.load(data)
          question_result = question_schema.dump(question.create())
        except Exception as e:
          return response_with(resp.INVALID_INPUT_422)
        return response_with(resp.SUCCESS_201,value={"version":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

# 按照项目ID查询版本
@version_bp.route('/one/<int:project_id>', methods=['GET'])
def get_version_from_project_id(project_id):
  fetched = Version.query.filter(Version.project_id==project_id).all()
  version_schema = VersionSchema(many=True, only=['name', 'id'])
  versions = version_schema.dump(fetched)
  return response_with(resp.SUCCESS_200, value={"versions":versions})
