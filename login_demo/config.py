# /usr/bin/env python 
# -*- coding: utf-8 -*-

DEBUG = True
TEMPLATES_AUTO_RELOAD = True
# 此处填写自己的mysql服务器地址和数据库
DB_URI = 'mysql+pymysql://root:2008.Cn123@192.168.0.101:3306/sqlalchemy' # 确保数据库存在
# 指定数据库连接
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False