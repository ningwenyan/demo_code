#!/usr/bin/env python
# coding=utf-8

from . import auth_bp
from flask import render_template, redirect, url_for, request, flash
from .auth_form import LoginForm, RegisterForm, ChangePasswordForm, ResetPasswordRequestForm, ResetPasswordForm, ChangeEmailForm
from common.exts import db
from common.sqlModel import User
from flask_login import login_user, login_required, current_user
from datetime import timedelta
from common.mailModel import sendMail

@auth_bp.route('/')
def index():
    return render_template('auth/index.html')

# 设计注册,登录页面

@auth_bp.route('/register/', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        """注册账户"""
        email = form.email.data.lower()
        username = form.username.data
        password = form.password.data
        user = User(email, username, password)
        db.session.add(user)
        db.session.commit()

        # 生成发送邮件token
        token = user.generate_confirmation_token()
        # 将token发送到用户邮箱中,我们希望用户的激活形式为 http://xx.com/auth/confirm/<token>
        sendMail(user.email, '激活账户', 'confirm', user=user, token=token)
        flash("请通过注册邮箱激活账户!")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@auth_bp.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        """登录用户"""
        email = form.email.data.lower()
        password = form.password.data
        confirmed  = form.confirmed.data
        user = User.query.filter_by(email=email).first()
        # 数据库中有账户,并且能够验证密码
        if user is not None and user.check_password(password):
            # print(confirmed)
            if confirmed:
                login_user(user, remember=True, duration=timedelta(days=30))
            else:
                login_user(user)
            # 判断 next
            next = request.args.get('next')
            if next is None or not next.startswitch('/'):
                # next = redirect(url_for('auth.index'))
                next = 'auth.login'
            return redirect(url_for('auth.personal' or next))
        else:
            flash('无效的邮箱或密码.')
    return render_template('auth/login.html')

# 限制登录用户访问 login_required
@auth_bp.route('/personal/')
@login_required
def personal():
    return render_template('auth/personal.html', user = current_user)


# 设置激活邮件的路由
@auth_bp.route('/confirm/<token>')
@login_required
def confirm(token):
    # flask_login可以通过 current_user 代理访问用户
    # 激活的账户直接跳转到 index 页面
    if current_user.confirmed:
        return redirect(url_for('auth.index'))
    # 验证序列化token
    if current_user.check_confirmation_token(token):
        # 设置数据库标志位为 True
        db.session.commit()
        flash('您的账户已激活,请登录!')
    else:
        flash('激活链接不正确或已过期!')
    return redirect(url_for('auth.index'))

# 如果激活过期,再次发送激活邮件
@auth_bp.route('/confirm/')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    sendMail(current_user.email, '激活账户', 'confirm', user=current_user, token=token)
    flash("一个新的激活连接已通过邮箱发送给您,请点击激活!")
    return redirect(url_for('auth.index'))


# 修改密码
@auth_bp.route('/change_password/', methods = ['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        old_password = form.old_password.data
        new_password = form.new_password.data
        if current_user.check_password(old_password):
            # 解密验证旧密码
            current_user.password = new_password
            db.session.add(current_user)
            db.session.commit()
            flash("您的密码已修改.")
            return redirect(url_for('auth.login'))
        else:
            flash("请输入正确的原密码.")
    return render_template('auth/change_password.html')

# 设置忘记密码
@auth_bp.route('/reset_password/', methods= ['GET', 'POST'])
def reset_password_request():
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        email = form.email.data.lower()
        user = User.query.filter(User.email == email).first()
        if user is not None:
            # 如果数据库中存在user,就发送重置密码的邮件
            # 在数据库中重新创建一个 generate_reset_password_token 用于生成密码token
            token = user.generate_reset_password_token()
            # 发送邮件
            sendMail(user.email, '重置密码', 'password_reset', user=user, token=token)
        flash("请检查您的邮箱重置密码.")
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html')

# 忘记密码,带token
@auth_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    form = ResetPasswordForm()
    if form.validate_on_submit():
        new_password = form.password.data
        # 使用类方法验证token
        if User.check_reset_password(token, new_password):
            db.session.commit()
            flash("您的密码已更新!")
            return redirect(url_for('auth.login'))
        else:
            flash("您的账户不存在,请注册!")
            return redirect(url_for('auth.register'))
    return render_template('auth/main/reset_password.html')

# 修改邮箱
@auth_bp.route('/change_email/', methods = ['GET', 'POST'])
@login_required
def change_email_request():
    form = ChangeEmailForm()
    if form.validate_on_submit():
        # 表单验证成功,并在数据库中不存在邮箱
        password = form.password.data
        new_email = form.new_email.data.lower()
        if current_user.check_password(password):
            token = current_user.generate_change_email_token(new_email)
            sendMail(new_email, '更换新邮箱', 'change_email', user= current_user, token=token)
            flash('您的邮箱已更换,请在新邮箱中激活账户.')
            return redirect(url_for('auth.login'))
        else:
            flash('无效的邮箱或密码')
    return render_template('auth/change_email.html')


@auth_bp.route('/change_email/<token>')
@login_required
def change_email(token):
    if current_user.check_change_email_token(token):
        db.session.commit()
        flash('您的邮箱已修改.')
    else:
        flash("链接已过期,请重新修改邮箱.")
    return redirect(url_for('auth.login'))

@auth_bp.route('/logout/')
@login_required
def logout():
    return redirect(url_for('auth.index'))