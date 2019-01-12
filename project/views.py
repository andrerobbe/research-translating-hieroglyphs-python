from project import app
import os
from flask import Flask, render_template, redirect, request, url_for, flash



@app.route('/home')
@app.route('/')
def index(msg=None):
	return render_template('home.html')


@app.route('/upload', methods=['POST'])
def upload_file():
	file = request.files['image']
	extensions = ['.jpg', '.png']
	file_extension = file.filename[-4:]

	if file_extension in extensions:
		f = os.path.join(app.config['CURRENT_FOLDER'], app.config['UPLOAD_FOLDER'], file.filename)
		file.save(f)
	else:
		flash('Bestand is geen ' + str(extensions))


	return redirect(url_for('index'))

