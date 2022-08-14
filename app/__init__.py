import os
import logging
from logging.handlers import RotatingFileHandler
import datetime
from flask import Flask, jsonify
from config import Config, log_dir
from app.utils.log import DayRotatingHandler
from app.utils import responses as resp
from app.utils.responses import response_with



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 注册蓝图
    register_blueprints(app)

    # 注册日志处理器
    # register_logging(app)

    # 注册错误处理函数
    register_errors(app)

    app.logger.info('Flask Rest Api startup')
    return app

def register_logging(app):
    app.logger.name = 'flask_api'
    log_level = app.config.get("LOG_LEVEL", logging.INFO)
    cls_handler = logging.StreamHandler()
    log_file = os.path.join(log_dir, datetime.date.today().strftime("%Y-%m-%d.log"))
    file_handler = DayRotatingHandler(log_file, mode="a", encoding="utf-8")

    logging.basicConfig(level=log_level,
                        format="%(asctime)s %(name)s "
                               "%(filename)s[%(lineno)d] %(funcName)s() %(levelname)s: %(message)s",
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
            file_handler = RotatingFileHandler(os.path.join(log_dir, 'flask_api.log'),maxBytes=1024 * 1024 * 50, backupCount=5, encoding='utf-8')
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(name)s %(levelname)s: %(message)s '
                '[in %(pathname)s:%(lineno)d]'))

            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)




def register_blueprints(app):

    from app.autosms import autosms_bp
    app.register_blueprint(autosms_bp,url_prefix='/api/sms')



def register_errors(app):

    @app.after_request
    def add_header(response):
        return response

    @app.errorhandler(404)
    def not_found(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_404)

    @app.errorhandler(500)
    def server_error(e):
        logging.error(e)
        return response_with(resp.SERVER_ERROR_500)

    @app.errorhandler(400)
    def bad_request(e):
        logging.error(e)
        return response_with(resp.BAD_REQUEST_400)