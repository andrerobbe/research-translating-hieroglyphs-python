from project import app
import os

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CURRENT_FOLDER = os.path.dirname(os.path.realpath(__file__))
app.config['CURRENT_FOLDER'] = CURRENT_FOLDER