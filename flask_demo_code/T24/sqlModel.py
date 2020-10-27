from config import SECRET_KEY
from exts import db
# 一种加密方式
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    verification = db.Column(db.Boolean, default=0) # flag,标识是否注册激活

    # 生成账户激活的token
    def generate_active_token(self, expires_in=3600):
        s = Serializer(current_app._get_current_object().config['SECRET_KEY'], expires_in=expires_in)
        print(s)
        print(current_app._get_current_object().config['SECRET_KEY'])
        return s.dumps({'id':self.id})

    # 账户激活
    @staticmethod
    def check_activate_token(token):
        s = Serializer(current_app._get_current_object().config['SECRET_KEY'])
        print(s)
        print(current_app._get_current_object().config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        # 得到用户
        u = Users.query.get(data['id'])
        if not u:
            # 用户不存在
            return False
        if not u.verification:
            # 用户没有激活
            u.verification = 1
            db.session.add(u)
            db.session.commit()
            return True