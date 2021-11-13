'''
Author: iiHancock
Time: 2021/11/6 10:43

'''
from flask import Flask

from app.ext import init_ext
from app.settings import envs
from app.views import init_blue


def create_app(env):
    app = Flask(__name__)

    # 初始化配置
    app.config.from_object(envs.get(env))

    # 初始化第三方
    init_ext(app)

    # 初始化路由
    init_blue(app)

    return app
