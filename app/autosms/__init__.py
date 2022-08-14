from flask import Blueprint
autosms_bp = Blueprint('autosms_bp',__name__)
from app.autosms import routes