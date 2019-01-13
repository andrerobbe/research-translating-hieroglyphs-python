from flask import Flask
import os

app = Flask(__name__)
app.secret_key = 'An231;02ncm/`m 213m ads09!31k?'

#avoid caching the img
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

app.config['UPLOAD_FOLDER'] = '/static/uploads/'
app.config['CURRENT_FOLDER'] = os.path.dirname(os.path.realpath(__file__)) 


import project.views