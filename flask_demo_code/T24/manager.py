from flask_script import Manager
from exts import db
from flask_migrate import MigrateCommand, Migrate
from app import app


# 导入Manager并绑定app
manager = Manager(app)

# 导入flaks_migrate
# Migrate 绑定app,db
Migrate(app, db)
# MigrateCommand 可以使用Alembic的命令
#

manager.add_command('db', MigrateCommand) # db是别名


if __name__  == '__main__':
    manager.run()