#!/usr/bin/env python
# coding=utf-8
from flask_script import Manager
from app import app
from exts import db
from flask_migrate import MigrateCommand,Migrate
from dbModel import User


# 绑定Flask app
manager = Manager(app)

# 导入 flask-migrate
# migrate绑定app, db
# MigrateCommand 可以使用Alembic所有的命令
# 导入所需要的 ORM
Migrate(app, db)
# 使用命令行创建数据库
manager.add_command('db', MigrateCommand) # 起一个别名

if __name__ == '__main__':
    manager.run()