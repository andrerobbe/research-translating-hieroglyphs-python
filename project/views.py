from project import app
import os

from flask import Flask, render_template, redirect, request, url_for, flash



@app.route('/')
@app.route('/home')
def index():
	return render_template('home.html')

@app.route('/text')
def text():
	return render_template('text.html')

@app.route('/album')
def album():
	return render_template('album.html')



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


@app.route('/translated')
def translated():
	lang = '123'
	return render_template('translated.html', lang=lang)