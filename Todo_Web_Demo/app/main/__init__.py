#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint

main_bp = Blueprint('main',__name__, url_prefix='/')

from . import views
from . import forms