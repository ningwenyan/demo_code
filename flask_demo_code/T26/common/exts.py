#!/usr/bin/env python
# coding=utf-8

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail


db = SQLAlchemy()
login_manager = LoginManager()
flask_bcrypt = Bcrypt()
csrf = CSRFProtect()
mail = Mail()