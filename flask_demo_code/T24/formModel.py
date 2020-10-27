from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Length, Email, EqualTo


class RegisterForm(FlaskForm):
    username = StringField(validators=[Length(6, 20, '长度不够')])
    email = StringField(validators=[Email()])
    password = PasswordField(validators=[Length(6, 20, '长度不够')])
    passwordR = PasswordField(validators=[EqualTo('password')])
    agree = BooleanField(validators=[]) # 验证为空,默认是False, 选择checkbox 变成True

class LoginForm(FlaskForm):
    login_username = StringField(validators=[Length(6, 20)])
    login_password = StringField(validators=[Length(6, 20)])