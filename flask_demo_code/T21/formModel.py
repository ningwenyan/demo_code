from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,IntegerField,PasswordField
from wtforms.validators import Length,EqualTo

class LoginForm(FlaskForm):
    username = StringField(validators=[Length(3, 12)])
    password = PasswordField(validators=[Length(6.12)])
    remember = BooleanField(validators=[])



class RegisterForm(FlaskForm):
    username = StringField(validators=[Length(3, 12)])
    password = PasswordField(validators=[Length(6.12)])
    reppassword = PasswordField(validators=[EqualTo('password')])