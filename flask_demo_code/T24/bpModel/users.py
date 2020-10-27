from flask import  Blueprint, render_template, redirect, url_for, flash, current_app
from formModel import RegisterForm
from sqlModel import Users
from exts import db
from mailModel import sendMail


bp = Blueprint('users', __name__, url_prefix='/users')

# 设置路由
@bp.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # 如果表单验证成功
        # 添加到数据库中
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = Users(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        # 生成激活校验的token
        token = user.generate_active_token()
        print(token)
        # 发送激活邮件到注册邮箱
        sendMail(user.email, '账户激活', 'activate', username=user.username, token=token)
        flash('注册成功,请到你邮箱中点击激活!!!')
        return redirect(url_for('users.verification', name=username))
    else:
        print(form.errors)
        return  render_template('register.html')


@bp.route('/login/', methods=['GET', 'POST'])
def login():
    return  render_template('login.html')

@bp.route('/verification/')
def verification():
    return  render_template('verification.html')

@bp.route('/activate/<token>/')
def activate(token):
    if Users.check_activate_token(token):
        flash('激活成功')
        return redirect(url_for('users.login'))
    else:
        flash('激活失败')
        return redirect(url_for('users.register'))