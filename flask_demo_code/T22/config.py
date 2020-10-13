import os
from redisModel import redis

DEBUG = True
TEMPLATES_AUTO_RELOAD = True

# 显式关闭CSRF
WTF_CSRF_ENABLED = False

# 指定Session保存类型
SESSION_TYPE = 'redis'
SESSION_PERMANENT = False
SESSION_USE_SIGNER = True # 加密
SECRET_KEY = os.urandom(24) # 设定加密
SESSION_KEY_PREFIX= 'session'
SESSION_REDIS = redis