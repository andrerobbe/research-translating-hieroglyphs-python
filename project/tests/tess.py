import pyautogui
import pytesseract
import cv2
import numpy as np
import PIL


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"


def tesserImg(image):
	image = cv2.resize(image, (0,0), fx=2, fy=2) #double the size so letters convert properly
	ret,image = cv2.threshold(image,127,255,cv2.THRESH_BINARY) #strip colour out
	image = PIL.Image.fromarray(image, 'RGB')
	txt = pytesseract.image_to_string(image)

	return txt

def screen_grab_as_numpy_array(loc1, loc2, loc3, loc4):
	im = np.array(PIL.ImageGrab.grab(bbox=(loc1,loc2,loc3,loc4)))
	im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
	return im

print(tesserImg(screen_grab_as_numpy_array(1812,0,1860,50)))


print pytesseract.image_to_string(PIL.Image.open('../static/img/alfabet.jpg'))