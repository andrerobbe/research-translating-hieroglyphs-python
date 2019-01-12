from project import app
import os

from flask import Flask, render_template, redirect, request, url_for, flash



@app.route('/home')
@app.route('/')
def index():
	return render_template('home.html')

@app.route('/images')
def img():
	return render_template('img.html')

@app.route('/text')
def text():
	return render_template('text.html')

@app.route('/translated')
def translated():
	return render_template('translated.html')


@app.route('/upload', methods=['POST'])
def upload():
	file = request.files['image']
	extensions = ['.jpg', '.png']
	file_extension = file.filename[-4:]

	if file_extension in extensions:
		f = os.path.join(app.config['CURRENT_FOLDER'], app.config['UPLOAD_FOLDER'], 'hieroglyphs.jpg')
		file.save(f)
		render = 'img.html'
	else:
		flash('Bestand is geen ' + str(extensions))
		render = 'home.html'
		
	return render_template(render)