#!/usr/bin/env python
# coding = utf-8

from flask import Flask,render_template
from furl import furl
from flask import redirect
from flask import request
import requests
import json
from flask import jsonify

app = Flask(__name__)
app.config.update({
    'DEBUG':True,
    'TEMPLATES_AUTO_RELOAD' : True
})

@app.route('/')
def index():
    return  render_template('index.html')

client_id = 'your id'
client_secret = 'your secret'

@app.route('/redirect_github/', methods = ['GET', 'POST'])
def redirect_github():
    url = 'https://github.com/login/oauth/authorize' # 这是官网给定的地址,且必须使用 get 方法
    params = {
        'client_id': client_id, # 必填
        'scope' : 'user'
    }
    url = furl(url).set(params)
    return redirect(url, 302)

@app.route('/oauth2/callback')
def oauth2_callback():
    # 获取code
    code = request.args.get('code')
    print(code)
    # 根据code 获取 token
    access_token_url = 'https://github.com/login/oauth/access_token'
    # 可用参数
    payload = {
        'client_id':client_id,
        'client_secret':client_secret,
        'code':code
    }
    # 发送 post
    r = requests.post(access_token_url, json=payload, headers={'Accept':'application/json'})
    print('------',json.loads(r.text))
    # 获取token
    access_toke = json.loads(r.text).get('access_token')
    print('access_token:', access_toke)

    # 获取到token后,访问资源服务器
    access_user_url = 'https://api.github.com/user'
    # 注意下方 token 后有一个空格
    rr = requests.get(access_user_url, headers={'Authorization':'token ' + access_toke})
    # 返回获取到的
    return jsonify({
        'status': 'sucess',
        'data': json.loads(rr.text)
    })


if __name__ == '__main__':
    app.run(port=8080)