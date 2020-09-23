from flask import Blueprint
from flask import request, render_template
from app_flaskwtf import Register_Form

# 实例化
bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/register/', methods=['GET', 'POST'])
def register():
    form = Register_Form()
    # validate_to_submit 会自动检查POST方法,只有是POST并且验证正确,返回True
    if form.validate_on_submit():
        return render_template('register.html', info='success')
    else:
        message = ""
        for k,v in form.errors.items():
            for i in v:
                message = message + '\r{}'.format(i)
            return render_template('register.html',info=message)
    # 返回 GET 方法请求的html
    return render_template('register.html')