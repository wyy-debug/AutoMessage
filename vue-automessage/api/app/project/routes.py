from flask import request
from app import db
from app.project import project_bp
from app.project.models import Project
from app.project.schema import ProjectSchema
from app.utils.responses import response_with
from app.utils import responses as resp
from flask_jwt_extended import jwt_required

# 创建项目
@project_bp.route('/',methods=['POST'])
def create_project():
    try:
        data = request.get_json()
        project_schema = ProjectSchema()
        project = project_schema.load(data)
        result = project_schema.dump(project.create())
        return response_with(resp.SUCCESS_201,value={"project":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

# 查询所有项目
@project_bp.route('/', methods=['GET'])
def get_project_list():
  fetched = Project.query.all()
  project_schema = ProjectSchema(many=True, only=['project_name', 'id'])
  projects = project_schema.dump(fetched)
  return response_with(resp.SUCCESS_200, value={"projects": projects})

# 按照ID查询单个项目
@project_bp.route('/<int:project_id>', methods=['GET'])
def get_project_from_id(project_id):
  fetched = Project.query.get_or_404(project_id)
  project_schema = ProjectSchema()
  project = project_schema.dump(fetched)
  return response_with(resp.SUCCESS_200, value={"project":project})

# 更新项目参数
@project_bp.route('/<int:id>', methods=['PATCH'])
def modify_project_detail(id):
  data = request.get_json()
  get_project = Project.query.get(id)
  if data.get('project_name'):
    get_project.project_name = data['project_name']
  db.session.add(get_project)
  db.session.commit()
  project_schema = ProjectSchema()
  project = project_schema.dump(get_project)
  return response_with(resp.SUCCESS_200, value={'project':project})

# 删除项目
@project_bp.route('/<int:id>', methods=['DELETE'])
def delete_project(id):
  get_project = Project.query.get_or_404(id)
  db.session.delete(get_project)
  db.session.commit()
  return response_with(resp.SUCCESS_204)
