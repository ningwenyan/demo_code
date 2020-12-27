#!/usr/bin/env python
# coding=utf-8


from flask import Flask
import config
from .auth import auth_bp
from .main import main_bp
from .commons.exts import bootstrap


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # 初始化插件
    bootstrap.init_app(app)

    # 注册蓝图
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app