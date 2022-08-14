from flask import request
from app.autosms import autosms_bp
from app.utils.responses import response_with
from app.utils import responses as resp

@autosms_bp.route('/',methods=['POST'])
def create_author():
    try:
        data = request.get_json()
        print(data)
        return response_with(resp.SUCCESS_201,value={"code":"success"})
    except Exception as e:
        #print(e)
        return response_with(resp.INVALID_INPUT_422)
