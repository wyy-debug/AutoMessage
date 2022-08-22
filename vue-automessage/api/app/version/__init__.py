from flask import Blueprint
version_bp = Blueprint('version_bp',__name__)
from app.version import routes
