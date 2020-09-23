from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import Length,Email, EqualTo, NumberRange, Regexp


class Register_Form(FlaskForm):
    username = StringField(validators=[Length(min=3,max=10,message='用户名不正确')])
    password= PasswordField(validators=[Length(min=6,max=10,message='密码长度不够')])
    repeat_password = PasswordField(validators=[EqualTo('password',message='密码不匹配')])
    phone = StringField(validators=[Regexp(r'1[3578]\d{9}',message='输入正确的手机号')])
    email=StringField(validators=[Email(message='输入正确的邮箱地址')])
    age = IntegerField(validators=[NumberRange(min=18,max=100,message='不接受未成年人')])