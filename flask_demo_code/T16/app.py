from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
# Flask_wtf 导入约束域
from flask_wtf.file import FileAllowed,FileField,FileRequired
from flask_uploads import IMAGES,UploadSet,configure_uploads,patch_request_class
from wtforms import StringField
from wtforms.validators import Length
from flask import redirect, url_for
import config



app = Flask(__name__)
app.config.from_object(config)


# 实例化
images = UploadSet('IMAGES')
# 限制大小
patch_request_class(app, 32*1024*1024)
# 注册到app
configure_uploads(app, images)


class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(images), FileRequired('no files')])
    description = StringField(validators=[Length(1, 100)])


@app.route('/')
def index():
    return 'hello world'

@app.route('/upload/', methods = ['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        # 拿到上传的文件
        f = form.photo.data
        filename = images.save(f)
        return redirect(url_for('show', filename=filename))
    else:
        return render_template('upload.html', info='filed')

    return render_template('upload.html')

@app.route('/upload/<filename>')
def show(filename):
    url = images.url(filename)
    return render_template('show.html', url=url, name=filename)

if __name__ == '__main__':
    app.run()