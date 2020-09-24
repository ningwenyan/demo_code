from flask import Blueprint

blogBp = Blueprint('blog', __name__,  subdomain='blog')

@blogBp.route('/')
def index():
    return 'bp blog'