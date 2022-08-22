from flask import request
from app import db
from app.questions import questions_bp
from app.questions.models import Question
from app.questions.schema import QuestionSchema
from app.utils.responses import response_with
from app.utils import responses as resp

# 创建问题
@questions_bp.route('/',methods=['POST'])
def create_question():
    try:
        data = request.get_json()
        question_schema = QuestionSchema()
        question = question_schema.load(data)
        result = question_schema.dump(question.create())
        return response_with(resp.SUCCESS_201,value={"question":result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

# 按照看板ID查询问题
@questions_bp.route('/one/', methods=['GET'])
def get_question_from_version_id():
  version_id = request.args.get('version_id')
  fetched = Question.query.filter(Question.version_id == version_id).all()
  qu_schema = QuestionSchema(many=True)
  question = qu_schema.dump(fetched)
  return response_with(resp.SUCCESS_200, value={"question": question})

