#!/usr/bin/env python
# coding=utf-8

from flask_login import UserMixin
from .exts import db, flask_bcrypt, login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    _password_hash = db.Column(db.String(128))   # 隐藏属性值,不能被外部访问
    confirmed = db.Column(db.Boolean, default=False)  # flag, 标识是否注册激活

    # 密码加密
    # 使用_password作为类属性,这是私有属性,不允许访问
    # 映射一个password方法
    def __init__(self, email, username, password, **kwargs):
        self.email = email
        self.username = username
        self.password = password

    @property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, raw_password):
        # 加密密码
        self._password_hash = flask_bcrypt.generate_password_hash(raw_password)

    @password.deleter
    def password(self):
        del self._password_hash

    # 定义解密密码
    def check_password(self, password):
        # 如果原始密码和加密后的密码相同,返回True
        return flask_bcrypt.check_password_hash(self._password_hash, password)

    # 邮件设置,发送邮件token并检测
    # 生成token,使用itsdangerous序列化token,确定唯一用户,并设置超时时间
    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app._get_current_object().config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'confirm':self.id}).decode('utf-8')

    # 接受序列化信息并检测
    def check_confirmation_token(self, token):
        s = Serializer(current_app._get_current_object().config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm') != self.id:
            # 检测唯一id
            return False
        # 所有检测通过,证明唯一用户,设置标志位
        self.confirmed = True
        # 没有执行db.session.commit(), 因为用户这里并不能确定用户点击了激活的超链接
        # 这将会在 views.py 中定义
        db.session.add(self)
        return True

    #  生成 reset password token
    def generate_reset_password_token(self, expiration=3600):
        s = Serializer(current_app._get_current_object().config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'reset':self.id}).decode('utf-8')

    # 序列化消息并验证,这里使用静态方法,对比以上的类的方法
    @staticmethod
    def check_reset_password(token, new_password):
        s = Serializer(current_app._get_current_object().config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        user = User.query.get(data.get('reset'))
        # 不是系统数据库中的用户,返回False
        if user is None:
            return False
        user.password = new_password
        db.session.add(user)
        return True

    # 验证邮箱token的token
    def generate_change_email_token(self,new_email,  expiration=3600):
        s = Serializer(current_app._get_current_object().config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'email':self.id, 'new_email': new_email}).decode('utf-8')

    def check_change_email_token(self, token):
        s = Serializer(current_app._get_current_object().config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        new_email = data.get('new_email')
        if data.get('email') != self.id:
            return False
        if new_email is None:
            return False
        # 判断重复
        if self.query.filter_by(email = new_email).first() is not None:
            return False
        # 修改
        self.email = new_email
        db.session.add(self)
        return True




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))