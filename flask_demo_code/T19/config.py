import os

DEBUG = True
TEMPLATES_AUTO_RELOAD = True
# 显式关闭CSRF
WTF_CSRF_ENABLED = False
# 创建secret key
SECRET_KEY = os.urandom(24)