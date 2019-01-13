from project import app
import os
from flask import Flask, render_template, redirect, request, url_for, flash


img = ''
img_path = app.config['CURRENT_FOLDER'] + app.config['UPLOAD_FOLDER']
img_name = 'hierogyphs'
img_ext = '.jpg'
extensions = ['.jpg', '.png']


@app.route('/')
@app.route('/home')
def index(*args):
	return render_template('home.html')

@app.route('/text')
def text():
	return render_template('text.html')

@app.route('/album')
def album():
	return render_template('album.html')



@app.route('/upload', methods=['POST'])
def upload():
	global img, img_ext
	img = request.files['image']
	img_ext = img.filename[-4:]

	if img_ext in extensions:
		#os.patch.join escapes of \t etc
		f = os.path.join(img_path + img_name + img_ext)
		img.save(f)
		render = 'upload.html'
	else:
		flash('Bestand is geen ' + str(extensions))
		render = 'home.html'

	return render_template(render, img_name=img_name, img_ext=img_ext)

import base64

@app.route('/translated')
def translated():
	"""
	with open('img', "rb") as imageFile:
		f = imageFile.read()
		b = bytearray(f)

	print b[0]
	"""

	msg = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat nonproident, sunt in culpa qui officia deserunt mollit.'

	return render_template('translated.html', img_name=img_name, img_ext=img_ext, msg=msg)



