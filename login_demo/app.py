from flask import Flask
import config
from flask import render_template, request, redirect, url_for
from common.bp_captcha import bp
from exts import db
from models import Demo_Login_Users
import json
from furl import furl

import requests
from flask import jsonify


app = Flask(__name__)
app.config.from_object(config)

# db绑定app
db.init_app(app)


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = request.form.get('username')
        passwd = request.form.get('passwd')
        code = request.form.get('code')
        #try:
        q1 = db.session.query(Demo_Login_Users).filter(db.and_(Demo_Login_Users.name == user, Demo_Login_Users.password == passwd)).first()
        with open('temp.json', 'r') as f:
            temp = f.read()
        #print(type(q1))
        #print(q1 != None)
        if q1 != None and code.lower() == json.loads(temp):
            return 'success'
        else:
            return redirect(url_for('login'))
        #except Exception as e:
        #    return  redirect(url_for('login'))


@app.route('/register/', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        user = request.form.get('username')
        passwd = request.form.get('passwd')
        phone = request.form.get('phone')
        User = Demo_Login_Users(name=user, phone=phone, password= passwd)
        db.session.add(User)
        db.session.commit()
        return redirect(url_for('success'))

@app.route('/success/')
def login_success():
    return render_template('loginSuccess.html')

# 两把钥匙
# 此处填写自己申请的id secret
client_id = 'ac1a836072*****'
client_secret = '5985ef31f96d7*****'


# github登录路由
@app.route('/redirect_github/')
def redirect_github():
    url = 'https://github.com/login/oauth/authorize'
    params = {
        'client_id' : client_id,
        'scope': 'read:user',
        'allow_signup': 'true'
    }
    url = furl(url).set(params)
    return redirect(url, 302)

@app.route('/oauth2/<service>/callback')
def oauth2_callback(service):
    print(service)

    code = request.args.get('code')
    # 根据code 获取 access token
    access_token_url = 'https://github.com/login/oauth/access_token'
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code' : code
    }
    r = requests.post(access_token_url, json=payload, headers={'Accept': 'application/json'})
    access_token = json.loads(r.text).get('access_token')

    access_user_url = 'https://api.github.com/user'
    r = requests.get(access_user_url, headers={'Authorization': 'token ' + access_token})
    return jsonify({
        'status': 'success',
        'data': json.loads(r.text)
    })

# 注册 Blueprint
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run()