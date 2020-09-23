import os
from flask_uploads import IMAGES

DEBUG = True
TEMPLATES_AUTO_RELOAD = True
# 显式关闭CSRF
WTF_CSRF_ENABLED = False
DIR = os.path.dirname(os.path.abspath(__file__))
UPLOADED_IMAGES_DEST= DIR + '/upload/'
UPLOADED_IMAGES_ALLOW = IMAGES