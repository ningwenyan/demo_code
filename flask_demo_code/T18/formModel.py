from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import Length

class LoginForm(FlaskForm):
    name = StringField(validators=[Length(6,12)])
    password = PasswordField(validators=[Length(8, 20)])