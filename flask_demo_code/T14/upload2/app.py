from flask import Flask,request,redirect,url_for,render_template,abort
import config
from flask_uploads import patch_request_class,UploadSet,configure_uploads


app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return 'Hello World!'

# 约束大小
patch_request_class(app, 32*1024*1024)

# 约束位置
photos = UploadSet('PHOTO')
# 注册
configure_uploads(app, photos)

@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files.get('photo'))
        return redirect(url_for('show', name=filename))
    return render_template('upload.html')

@app.route('/upload/<name>')
def show(name):
    if name is None:
        return abort(404)
    # 通过photos.url 获取地址
    url = photos.url(name)
    return render_template('show.html', url=url, name=name)


if __name__ == '__main__':
    app.run() 