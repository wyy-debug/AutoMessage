from flask import Blueprint
partition_bp = Blueprint('partition_bp',__name__)
from app.partition import routes
