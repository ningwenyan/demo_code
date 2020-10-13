from flask import Flask
import config
from flask_session import Session as Fsession
from flask import session,redirect,url_for,render_template,escape
from formModel import LoginForm
from datetime import timedelta

app = Flask(__name__)
app.config.from_object(config)
Fsession(app)

@app.route('/')
def index():
    if 'username' in session:
        # escape 用来替换html中的16进制特殊符号
        return 'Logged in as {}.<a href="/logout/">Logout</a>'.format(escape(session.get('username')))
    return 'You are not log in <a href="/login/">Login<a>'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #  假设数据库验证通过, 添加 session
        user = form.username.data
        remember = form.remember.data
        session['username'] = user
        print(remember)
        if remember:
            session.permanent = True
            app.config.update({'SESSION_COOKIE_LIFETIME': timedelta(days=30) })
        else:
            session.permanent = False
        return 'success'
    return render_template('login.html')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()