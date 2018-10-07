from flask import Blueprint
routes = Blueprint('handlers', __name__)

from .index import *
