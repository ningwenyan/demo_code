from exts import db
import os

DEBUG = True
TEMPLATES_AUTO_RELOAD  =  True
# 设置数据库信息
dbmsg = 'mysql+pymysql://root:2008.Cn123@192.168.0.101:3306/flask_session_demo2'
SQLALCHEMY_DATABASE_URI = dbmsg
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 使用Flask_WTF 暂时关闭 CSRF
# 显式关闭CSRF
WTF_CSRF_ENABLED = False
# 指定Flask-Session的存储
SESSION_TYPE = 'sqlalchemy' # 指定数据库类型
SESSION_SQLALCHEMY = db     # 指定数据库
SESSION_SQLALCHEMY_TABLE = 'session'  # 指定保存到的表
SESSION_PERMANENT = False  # 指定永久性保存
SESSION_USE_SIGNER = True # 设定加密
SECRET_KEY = os.urandom(24) # 设定加密秘钥
SESSION_KEY_PREFIX = 'session' # 设置保存的前缀