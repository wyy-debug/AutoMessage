from flask import Blueprint
number_bp = Blueprint('number_bp',__name__)
from app.number import routes
