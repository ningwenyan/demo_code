#!/usr/bin/env python
# coding=utf-8
import os

DEBUG = True
TEMPLATES_AUTO_RELOAD = True
SECRET_KEY = os.urandom(12)

# 设置数据库的基本信息
# 数据库连接
DB_URI = 'mysql+pymysql://root:2008.Cn123@192.168.0.101:3306/flask_bootstrap_demo' # 确保数据库存在
# 指定数据库连接
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False