#!/usr/bin/env python
# coding=utf-8
import os

DEBUG = True
TEMPLATES_AUTO_RELOAD = True

# CSRF SECRET_KEY
SECRET_KEY = os.urandom(12)

# 设置数据库的基本信息
# 数据库连接
DB_URI = 'mysql+pymysql://root:2008.Cn123@192.168.0.101:3306/flask_login_demo1' # 确保数据库存在
# 指定数据库连接
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 设置邮箱
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USERNAME = '25@qq.com'
MAIL_PASSWORD = "imkzffddijc"
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_DEFAULT_SENDER = '25@qq.com'