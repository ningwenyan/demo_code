# -*- coding: utf-8 -*-

from flask import Blueprint, make_response
from utils.captcha import Captcha
from io import BytesIO
import json

bp = Blueprint('common', __name__, url_prefix='/common/')

@bp.route('/')
def index():
    return 'hello'


@bp.route('/graph_capture/')
def graph_capture():
    text, image = Captcha.gene_graph_captcha()
    temp = json.dumps(''.join(text).lower())
    with open('temp.json', 'w') as f:
        f.write(temp)
    #  验证码图片以二进制形式写入内存，防止图片都放在文件夹中，占用磁盘空间
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'   
    return resp