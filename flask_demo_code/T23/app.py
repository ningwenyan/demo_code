from flask import Flask
import config
from flask import render_template,views

app = Flask(__name__)
app.config.from_object(config)

# 首页
@app.route('/')
def index():
    return render_template('index.html')

# 注册页
class RegisterView(views.MethodView):
    def get(self):
        return render_template('register.html')
    def post(self):
        pass

# 登录页
class LoginView(views.MethodView):
    def get(self):
        return render_template('login.html')
    def post(self):
        pass

# 个人信息页面
@app.route('/personal/')
def personal():
    return render_template('personal.html')

# 存钱页面
class SaveMoneyView(views.MethodView):
    def get(self):
        return render_template('savemoney.html')
    def post(self):
        pass

# 转账页面
class TransferView(views.MethodView):
    def get(self):
        return render_template('transfer.html')
    def post(self):
        pass

# 退出
@app.route('/logout/')
def logout():
    return render_template('index.html')

# 注册URL
app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/register/',view_func=RegisterView.as_view('register'))
app.add_url_rule('/savemoney/',view_func=SaveMoneyView.as_view('savemoney'))
app.add_url_rule('/transfer/',view_func=TransferView.as_view('transfer'))

if __name__ == '__main__':
    app.run()