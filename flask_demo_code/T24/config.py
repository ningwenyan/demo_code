import os

DEBUG = True
TEMPLATES_AUTO_RELOAD = True

# 加密
# secret key
SECRET_KEY = os.urandom(24)

# mysql
# 数据库支持
msg = "mysql+pymysql://root:2008.Cn123@192.168.0.101:3306/flask_mail_demo"
SQLALCHEMY_DATABASE_URI = msg
SQLALCHEMY_TRACK_MODIFICATIONS = False # 关闭追

# 配置Mail
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USERNAME = '257@qq.com'
MAIL_PASSWORD = "imkzc"
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_DEFAULT_SENDER = '257@qq.com'