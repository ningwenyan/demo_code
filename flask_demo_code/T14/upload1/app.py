from flask import Flask
import config
from flask import request, render_template,send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config.from_object(config)


ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg','gif'])

# 判断文件夹后缀
def allow_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        file = request.files.get('file')
        if file and allow_file(file.filename):
            print('success')
            # 安全考虑,使用 security filename
            filename = secure_filename(file.filename)
            print(app.config['UPLOAD_FOLDER'])
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('upload.html')

@app.route('/upload/<filename>')           
def upload_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == "__main__":
    app.run()