from exts import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(45))
    password = db.Column(db.String(45))
    remember = db.Column(db.Boolean)