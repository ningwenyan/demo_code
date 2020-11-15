from flask import Flask
import config
from auth import auth_bp
from common import common_bp
from common.exts import db, login_manager, flask_bcrypt, csrf, mail

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
login_manager.init_app(app)
flask_bcrypt.init_app(app)
csrf.init_app(app)
mail.init_app(app)

# 指定登录的URL
login_manager.login_view = 'auth.login'

@app.route('/')
def hello_world():
    return 'Hello World!'

# 注册蓝图
app.register_blueprint(auth_bp)
app.register_blueprint(common_bp)

if __name__ == '__main__':
    app.run()