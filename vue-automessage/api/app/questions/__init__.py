from flask import Blueprint
questions_bp = Blueprint('questions_bp',__name__)
from app.questions import routes
