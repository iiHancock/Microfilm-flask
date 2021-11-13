'''
Author: iiHancock
Time: 2021/11/6 11:14

'''
from flask import Blueprint

blue = Blueprint('blue', __name__)


def init_blue(app):
    app.register_blueprint(blue)


@blue.route("/")
def index():
    return "Index"
