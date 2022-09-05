import os
import logging
from logging.handlers import RotatingFileHandler
import datetime
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate
from config import Config,log_dir
from app.utils.log import DayRotatingHandler
from app.utils import responses as resp
from app.utils.responses import response_with
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
import app.utils.gol as gol
from app.utils.poco_device import poco_device

db = SQLAlchemy()
jwt = JWTManager()
cors = CORS()
migrate = Migrate()
marshmallow = Marshmallow()



def register_plugins(app):
    cors.init_app(app, supports_credentials=True)
    db.init_app(app)
    jwt.init_app(app)
    marshmallow.init_app(app)
    migrate.init_app(app,db)



def register_blueprints(app):


    from app.users import users_bp
    app.register_blueprint(users_bp, url_prefix='/api/users')

    from app.device import device_bp
    app.register_blueprint(device_bp, url_prefix='/api/device')

    from app.message import message_bp
    app.register_blueprint(message_bp, url_prefix='/api/message')

    from app.number import number_bp
    app.register_blueprint(number_bp, url_prefix='/api/number')

    from app.partition import partition_bp
    app.register_blueprint(partition_bp, url_prefix='/api/partition')

    swaggerui_blueprint = get_swaggerui_blueprint('/api/docs', '/api/spec', config={'app_name': 'Flask API Docs'})
    app.register_blueprint(swaggerui_blueprint, url_prefix='/api/docs')


def register_logging(app):
    app.logger.name = 'flask_api'
    log_level = app.config.get('LOG_LEVEL', logging.INFO)
    cls_handler = logging.StreamHandler()
    log_file = os.path.join(log_dir, datetime.date.today().strftime("%Y-%m-%d.log"))
    file_handler = DayRotatingHandler(log_file, mode="a", encoding="utf-8")

    logging.basicConfig(level=log_level,
                        format="%(asctime)s %(name)s"
                               "(5fileaname)s[%(lineno)d] %(funcName)s() %(levelname)s: %(message)s",
                        datefmt="%Y/%m/%d %H:%M:%S",
                        handlers=[cls_handler, file_handler])

    if not app.debug and not app.testing:
        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                os.mkdir('logs')
            file_handler = RotatingFileHandler(os.path.join(log_dir, 'flask_api.log'),maxBytes=1024 * 1024 * 50,backupCount=5,encoding='utf-8')
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(name)s %(levelname)s: %(message)s'
                '[in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)


def register_errors(app):

    @app.after_request
    def add_header(response):
        return response

    @app.errorhandler(404)
    def not_found(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_404)

    @app.errorhandler(500)
    def not_found(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_500)

    @app.errorhandler(400)
    def not_found(e):
        logging.error(e)
        return response_with(resp.BAD_REQUEST_400)



def create_app(config_class=Config):
    app = Flask(__name__,static_folder="../../dist",template_folder="../../dist",static_url_path="/")
    app.config.from_object(config_class)
    app.secret_key = b"\x0bq{\xc2j'M\xa3\xd5\xe7+\xbe\xabb]'"
    # 注册插件
    register_plugins(app)

    # 注册蓝图
    register_blueprints(app)

    # 注册日志处理器
    register_logging(app)

    # 注册错误处理函数
    register_errors(app)

    # 全局变量管理
    gol._init()
    gol.set_value("phone_state", "free")
    gol.set_value("phone_part", "null")
    gol.set_value("phone_sim", "null")
    gol.set_value("phone_number", 13313331333)
    gol.set_value("phone_poco", poco_device())

    app.logger.info('Flask Rest Api startup')

    return app
