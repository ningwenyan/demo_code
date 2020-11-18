#!/usr/bin/env python
# coding=utf-8
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
csrf = CSRFProtect()
db = SQLAlchemy()
