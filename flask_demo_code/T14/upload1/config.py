import os 

DEBUG=True
TEMPLATES_AUTO_RELOAD=True

PAR_DIR = os.path.dirname(__file__) # 会得到当前的目录
UPLOAD_FOLDER=PAR_DIR + '/upload/'
MAX_CONTENT_LENGTH = 16*1024*1024
