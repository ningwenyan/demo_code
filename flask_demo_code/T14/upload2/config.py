import os
from flask_uploads import IMAGES,DOCUMENTS

DEBUG=True
TEMPLATES_AUTO_RELOAD = True

DIR = os.path.dirname(os.path.abspath(__file__))
UPLOADED_PHOTO_DEST= DIR + '/upload/'

UPLOADED_PHOTO_ALLOW = (IMAGES+DOCUMENTS)