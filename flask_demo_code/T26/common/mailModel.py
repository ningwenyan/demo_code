#!/usr/bin/env python
# coding=utf-8

from flask_mail import Message

from flask import render_template, current_app
from threading import Thread
from common.exts import mail

# 异步发送邮件
def async_send_mail(app, msg):
    # 要求在Flask的一次访问中发送邮件,下面代码中新建的线程中并
    # 不包含 上下文结构,手动推送
    with app.app_context():
        mail.send(msg)


def sendMail(to, subject, template, **kwargs):
    try:
        # 创建邮件
        msg = Message(subject, recipients=[to])
        # 回传浏览器
        msg.body = render_template('auth/mail/'+ template + '.txt', **kwargs)
        msg.html = render_template('auth/mail/' + template + '.html', **kwargs)
        print('auth/mail/{}'.format(template) + '.txt')
        print('auth/mail/{}'.format(template) + '.html')
        # 创建一个新线程,发送邮件
        # 根据flask上下文,如果不再同一个 app 中,将无法发送邮件
        app = current_app._get_current_object()
        thread = Thread(target=async_send_mail, args=[app, msg])
        thread.start()
        return thread
    except Exception as e:
        print(e)