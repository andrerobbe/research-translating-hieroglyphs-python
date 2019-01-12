from flask import Flask
import os

app = Flask(__name__)
app.secret_key = 'An231;02ncm/`m 213m ads09!31k?'

import project.config
import project.views