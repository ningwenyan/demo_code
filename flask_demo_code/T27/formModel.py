#!/usr/bin/env python
# coding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length

class GetForm(FlaskForm):
    username = StringField('用户名', validators=[Length(4, 9, '请输入正确长度的用户名')], render_kw={'placeholder':'username'})
    password = PasswordField('密码', validators=[Length(4, 9, '请输入正确长度的密码')], render_kw={'placeholder':'password'})
    submit  = SubmitField('登录')


class GetFormField(FlaskForm):
    username = StringField('用户名', validators=[Length(4, 9, '请输入正确长度的用户名')], render_kw={'placeholder': 'username'})
    password = PasswordField('密码', validators=[Length(4, 9, '请输入正确长度的密码')], render_kw={'placeholder': 'password'})
    submit = SubmitField('登录')
