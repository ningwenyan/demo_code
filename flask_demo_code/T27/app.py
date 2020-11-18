from flask import Flask
import config
from exts import bootstrap, csrf, db
from flask import flash, render_template, redirect, url_for, request
from flask_bootstrap import Markup
from formModel import GetForm, GetFormField
from sqlModel import User

app = Flask(__name__)
app.config.from_object(config)
bootstrap.init_app(app=app)
csrf.init_app(app=app)
db.init_app(app=app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_flash_messages/', methods=['GET', 'POST'])
def get_flash_messages():
    flash('A simple default alert—check it out!')
    flash('A simple primary alert—check it out!', 'primary')
    flash('A simple secondary alert—check it out!', 'secondary')
    flash('A simple success alert—check it out!', 'success')
    flash('A simple danger alert—check it out!', 'danger')
    flash('A simple warning alert—check it out!', 'warning')
    flash('A simple info alert—check it out!', 'info')
    flash('A simple light alert—check it out!', 'light')
    flash('A simple dark alert—check it out!', 'dark')
    flash(Markup(
        'A simple success alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.'),
          'success')
    return render_template('get_flash_messages.html')

@app.route('/get_form/', methods=['GET', 'POST'])
def get_form():
    form = GetForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('get_form.html', form=form)

@app.route('/get_form_filed/', methods=['GET', 'POST'])
def get_form_field():
    form = GetFormField()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('get_form_field.html', form=form)

@app.route('/get_pager/', methods=['GET', 'POST'])
def get_pager():
    db.drop_all()
    db.create_all()
    for i in range(100):
        user = User(name='{}'.format(str(i)), password='h{}'.format(str(i)))
        db.session.add(user)
    db.session.commit()
    page = request.args.get('page', 1, type=int)
    pagination = User.query.paginate(page, 10)
    messages = pagination.items
    return render_template('get_pager.html', pagination=pagination, messages=messages)


# @app.before_first_request
# def func():
#     db.drop_all()
#     db.create_all()
#     for i in range(20):
#         user = User(name='{}'.format(str(i)), password='h{}'.format(str(i)))
#         db.session.add(user)
#     db.session.commit()
#

if __name__ == '__main__':
    app.run(host='192.168.0.110', port=8080)
