#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint

common_bp = Blueprint('common', __name__, url_prefix='/common')

from . import errors
from . import exts
from . import sqlModel
from . import mailModel