import os

DEBUG = True
TEMPLATES_AUTO_RELOAD = True

# 显式关闭CSRF
WTF_CSRF_ENABLED = False

# 指定Session保存类型
SESSION_TYPE = 'filesystem'
SESSION_FILE_DIR = './flask_session'
SESSION_FILE_THRESHOLD = 10 # 默认是500,大于设定值,会自动删除
SESSION_FILE_MODE = 600 # 默认值,文件模式,读写执行
SESSION_PERMANENT = False
SESSION_USE_SIGNER = True # 加密
SECRET_KEY = os.urandom(24) # 设定加密秘
SESSION_KEY_PREFIX= 'session'