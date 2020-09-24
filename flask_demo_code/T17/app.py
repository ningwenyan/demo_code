from flask import Flask
import config
from flask import render_template, request, make_response
from formModel import LoginForm
from uuid import uuid4

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    return 'index page'

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 拿到值
        name = form.name.data
        uid = str(uuid4())
        resp = make_response(render_template('user.html', username=name))
        resp.set_cookie(name, uid)
        return resp
    else:
        return render_template('login.html')
    return render_template('login.html')

@app.route('/getcookies/')
def get_cookie():
    name = request.args.get('name')
    cookie1 = request.cookies.get(name)
    return cookie1

if __name__ == '__main__':
    app.run()