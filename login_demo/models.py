# -*- coding: utf-8 -*-

from exts import db
from datetime import datetime

# 创建Model

class Demo_Login_Users(db.Model):
    __tablename__ = 'demo_login_users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50))
    password = db.Column(db.String(50))
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_time = db.Column(db.DateTime)