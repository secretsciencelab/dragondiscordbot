from flask import Blueprint
handlers = Blueprint('handlers', __name__)

from .index import *
