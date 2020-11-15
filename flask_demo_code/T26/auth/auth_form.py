#!/usr/bin/env python
# coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, ValidationError
from wtforms.validators import Length, EqualTo, Regexp, Required, DataRequired, Email
from common.sqlModel import User

class LoginForm(FlaskForm):
    email = StringField(validators=[Email(), DataRequired(), Length(1, 64)])
    password = PasswordField(validators=[Length(1, 24)])
    confirmed = BooleanField(validators=[])

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[Email(), Length(1, 64), DataRequired()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Username must have only letters, numbers, dots or '
               'underscores')
    ])
    password = PasswordField('Password', validators=[Length(1, 24), Required()])
    con_password = PasswordField('Confirm Password', validators=[EqualTo('password')])

    # 自定义Field,验证邮箱和用户
    def validate_email(self, field):
        if User.query.filter_by(email = field.data.lower()).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, filed):
        if User.query.filter_by(username = filed.data).first():
            raise  ValidationError('Username already in use.')

# 修改密码表单
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(validators=[Length(1, 24)])
    new_password = PasswordField(validators=[Length(1, 24)])
    rep_password = PasswordField(validators=[EqualTo('new_password')])

# 忘记密码表单1
class ResetPasswordRequestForm(FlaskForm):
    email = StringField(validators=[Email()])

# 忘记密码表单2
class ResetPasswordForm(FlaskForm):
    email = StringField(validators=[Email()])
    password = PasswordField('Password', validators=[Length(1, 24)])
    con_password = PasswordField('Confirm Password', validators=[EqualTo('password')])

# 修改邮箱
class ChangeEmailForm(FlaskForm):
    password = PasswordField('Password', validators=[Length(1, 24)])
    new_email = StringField('New Email', validators=[Email()])

    def validate_new_email(self, field):
        if User.query.filter_by(email = field.data.lower()).first():
            print('11111111')
            raise ValidationError('邮箱已经存在!')