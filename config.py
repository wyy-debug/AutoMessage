import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))

# load env

# log dir
log_dir = os.path.join(basedir, os.getenv('LOG_DIR', 'logs'))

class Config(object):
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    LOG_LEVEL = logging.INFO