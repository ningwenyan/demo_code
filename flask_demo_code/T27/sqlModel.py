#!/usr/bin/env python
# coding=utf-8

from exts import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    password = db.Column(db.String(45))