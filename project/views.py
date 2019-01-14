from project import app
import os
from flask import Flask, render_template, redirect, request, url_for, flash

#used for debugging
from pprint import pprint

#translating
from sightengine.client import SightengineClient
import PIL
import sys, random, argparse 
import numpy as np 
import math 
import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"


#global vars
gscale1 = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~i!lI;:,\"^`". '    #70 levels of gray
gscale2 = '@%#*+=-:. ' 														         #10 levels of gray

client = SightengineClient('407400170', 'PVmF8vE3vnunnu8LQumR')

img = ''
img_path = app.config['CURRENT_FOLDER'] + app.config['UPLOAD_FOLDER']
img_name = 'hieroglyphs'
img_ext = '.jpg'
extensions = ['.jpg', '.png']
filename = os.path.join(img_path + img_name + img_ext) #os.patch.join escapes of \t etc





@app.route('/')
@app.route('/image')
def index(*args):
	return render_template('img.html')

############################################################################################################################
############################################################################################################################

@app.route('/text')
def text():
	return render_template('text.html')

############################################################################################################################
############################################################################################################################

@app.route('/album')
def album():
	return render_template('album.html')

############################################################################################################################
############################################################################################################################

@app.route('/upload', methods=['POST'])
def upload():
	global img, img_ext, filename
	img = request.files['image']
	img_ext = img.filename[-4:]
	#pprint(vars(img)) #print object

	if img_ext in extensions:
		filename = os.path.join(img_path + img_name + img_ext) #overwrite filename in case it's .png
		img.save(filename)

		render = 'upload.html'
	else:
		flash('Bestand is geen ' + str(extensions))
		render = 'img.html'

	return render_template(render, img_name=img_name, img_ext=img_ext)

import base64

############################################################################################################################
############################################################################################################################

@app.route('/translated')
def translated():

	output = client.check('text').set_file(filename) #API call to check for txt
	#print output

	msg = covertImageToAscii() #args = cols, scale, moreLevels
	path = img_path + 'output.txt'
	output = writeToFile(msg, path)

	imgToTxt = tesserImgToTxt(filename)

	return render_template('translated.html', img_name=img_name, img_ext=img_ext, txt=imgToTxt)

############################################################################################################################
############################################################################################################################

def writeToFile(msg, path):
	f = open(os.path.join(path), 'w')

	for row in msg:
		f.write(row + '\n')
	f.close()
	print 'File written to ' + path
	return

############################################################################################################################
############################################################################################################################

#return average brightness for a tile in the grayscale image
def getAverageBrightness(image): 
	im = np.array(image)
	w,h = im.shape
	return np.average(im.reshape(w*h))

############################################################################################################################
############################################################################################################################

#given image and dims (rows, cols), returns an m*n list of Images
def covertImageToAscii(cols=None, scale=None, moreLevels=None): 
	global gscale1, gscale2
	#set arguments
	if scale:
		scale = float(scale)
	else:
		scale = 0.43  #set scale default as 0.43 which suits Courier font
	
	if cols:
		cols = int(cols)
	else:
		cols = 200

    # open as PIL, convert into greyscale and split img into grid
	image = PIL.Image.open(filename).convert('L')

	W, H = image.size[0], image.size[1]
	print("Input image dims: %d x %d" % (W, H)) 
	w = W/cols
	h = w/scale
	rows = int(H/h) 
	print("Cols: %d, Rows: %d" % (cols, rows))
	print("Tile dims: %d x %d" % (w, h))


	#check if image size is too small 
	if cols > W or rows > H: 
		print("Image too small for specified cols!") 
		#exit(0) 


	##########################
	##### GENERATING ASCII ###
	##########################
	aimg = [] 
	
	for j in range(rows): #generate list of dimensions
		y1 = int(j*h) 
		y2 = int((j+1)*h) 
		
		if j == rows-1: #correct last tile
			y2 = H 
			
		aimg.append("")
		
		for i in range(cols): #crop image to tile
			x1 = int(i*w) 
			x2 = int((i+1)*w) 
			
			if i == cols-1: #correct last tile 
				x2 = W 
			
			img_crop = image.crop((x1, y1, x2, y2)) #crop image to extract tile
			
			avg = int(getAverageBrightness(img_crop)) #get average luminance
			
			if moreLevels: #look up ascii char 
				gsval = gscale1[int((avg*69)/255)] 
			else: 
				gsval = gscale2[int((avg*9)/255)] 

			aimg[j] += gsval #append ascii char to string 

	return aimg

############################################################################################################################
############################################################################################################################


def tesserImgToTxt(filename):
	image = PIL.Image.open(filename)
	#image = cv2.resize(image, (0,0), fx=2, fy=2) #double the size so letters convert properly
	#ret,image = cv2.threshold(image,127,255,cv2.THRESH_BINARY) #strip colour out, anything below 127 = black, above 127 is white
	#image = PIL.Image.fromarray(image, 'RGB')
	txt = pytesseract.image_to_string(image)

	return txt
