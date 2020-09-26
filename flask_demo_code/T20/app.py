from flask import Flask
import config
from exts import db
from flask import render_template,redirect,url_for,session
from formModel import LoginForm,RegisterForm
from dbModel import User
from flask_session import Session as Fsession
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object(config)
# 初始化db
db.init_app(app)
Fsession(app)

@app.route('/')
def index():
    return 'You are not log in <a href="/login/">Login<a>'

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.username.data
        passwd = form.password.data
        remember = form.remember.data
        print(user, passwd, remember, type(remember))
        patt = db.session.query(User.password).filter(User.username == user).first() 
        dpaassword = ""
        for i in patt:
            dpaassword = i
        if patt and dpaassword == passwd:
            # 设置session
            session['username'] = user
            
            if remember:
                session.permanent = True
                app.config.update({
                    'PERMANENT_SESSION_LIFETIME': timedelta(days=30)
                })
                db.session.query(User).filter(User.username == user).update({ User.remember: remember})
                db.session.commit()
            else:
                db.session.query(User).filter(User.username == user).update({ User.remember: remember})
                db.session.commit()   
        return 'success'
    return render_template('login.html')


@app.route('/register/', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit(): # post请求,并验证通过
        user = form.username.data
        passwd = form.password.data
        user1 = User(username=user, password=passwd, remember=1)
        db.session.add(user1)
        db.session.commit()
        return redirect(url_for('login'))
    else:
        print(form.errors)
    
    return render_template('register.html')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()