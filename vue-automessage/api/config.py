import os
import logging
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


#load env
load_dotenv(os.path.join(basedir,'.flaskenv'))

#log dir
log_dir = os.path.join(basedir, os.getenv('LOGDIR','logs'))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///books.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    LOG_LEVEL = logging.INFO
