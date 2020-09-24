from flask import Flask
import config
from flask import session,escape,request,redirect,url_for

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as {}. <a href="/logout/">Logout</a>'.format(escape(session.get('username')))
    return 'You are not log in <a href="/login/">Login<a>'

@app.route('/login/', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    login_html = """
        <form action="" method="POST">
           <p><input type=text name=username></p>
           <p><input type=submit value=Login></p>
         </form>
    """
    return login_html

@app.route('/logout/')
def logout():
    '''删除session'''
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()