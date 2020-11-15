#!/usr/bin/env python
# coding=utf-8

from . import common_bp
from flask import render_template

# 设计401, 403, 404, 500错误
@common_bp.app_errorhandler(401) # 未授权错误
def unauthorized(e):
    return render_template('401.html'), 401

@common_bp.app_errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@common_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@common_bp.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500