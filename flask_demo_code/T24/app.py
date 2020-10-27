from flask import Flask, render_template
from bpModel import users
import config
from exts import db, mail, csrf



app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)
csrf.init_app(app)

@app.route('/')
def index():
    return  'index page'


# 注册blueprint
app.register_blueprint(users.bp)


if __name__ == '__main__':
    app.run()