from flask import Flask
import config
from usermodel import userbp


app = Flask(__name__)
app.config.from_object(config)



@app.route('/')
def index():
    return 'hello world'

# 注册蓝图
app.register_blueprint(userbp.bp)     

if __name__ == '__main__':
    app.run()