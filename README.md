# Proof of concept: Can I translate hieroglyphs images through python?


## Inhoud
- [Installation?](#installation)
- [Gevolgede Stappen](#gevolgde-stappen)
   - [Site met Python en Flask](#site-met-python-en-flask)
   - [Image Uploaden](#image-uploaden)
   - [Research naar Hiërogliefen](#research-naar-hiërogliefen)
   - [Rechtstreekse Vertaling](#rechtstreekse-vertaling)
   - [Text detection op Images](#text-detection-op-images)
   - [Hiërogliefen omzetten via Ascii Art](#hiërogliefen-omzetten-via-Ascii-Art)
   - [Images omzetten naar text](#images-omzetten-naar-text)
- [Resources](#resources)



## Installation

```cmd
pip install pil
 ```

```cmd
pip install numpy
 ```

```cmd
pip install pytesseract
 ```
```cmd
pip install opencv-python
 ```
- install tesseract https://github.com/tesseract-ocr/tesseract/wiki



## Gevolgede Stappen
- Site met python maken in flask
- Image uploaden
- Research naar Hiërogliefen
- Rechtstreekse Vertaling
- Text detection op Images
- Hiërogliefen omzetten via Ascii Art
- Images omzetten naar text



### Site met Python en Flask
Dit was redelijk makkelijk doordat we met web-concepten dit ook al eens gedaan hebben. Dit is gewoon een init py script aanmaken, samen met een routing script die dan de HTML templates rendered via flask. 



### Image Uploaden
Hiervoor heb ik een guide gevolgd, wat ook vrij makkelijk was. Het komt er op neer om in de routing een pagina met een POST method te hebben, waar het formulier van de HTML naar toe wordt gestuurd. In python heb je dan de volgende code:

```python
import os
from flask import Flask, render_template, request

app.config['CURRENT_FOLDER'] = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = '/static/uploads/'

# other routes

@app.route('/upload', methods=['POST'])
def upload_file():
	file = request.files['image']
    f = os.path.join(app.config['CURRENT_FOLDER'], app.config['UPLOAD_FOLDER'], file.filename)
    file.save(f)

    return render_template('index.html')
```

En de HTML:
```HTML
<form action="/upload" method="post" enctype="multipart/form-data" >
	<span class="btn btn-default btn-file">
		Browse <input type="file" name="image">
	</span>

	<input type="submit" value="Upload your image" class="btn btn-primary">
</form>
```



## Research naar Hiërogliefen
Er zijn een paar belangrijke zaken waar je op moet letten bij hiërogliefen.

Ten eerste doet deze vertaler een fonetische vertaling (of beter gezegd 'transliteration'). Hiërogliefen zijn nooit echt een officieel alfabet geweest. Er zijn ongeveer 24 verschillende symbolen die eenvoudige geluiden zijn die erg op ons alfabet lijken. Dat zijn 'unilaterals'. Er zijn ook hiërogliefen die een combinatie van letters zijn zoals 'nfr'.

<img src="img/nfr.PNG" alt="nfr hyroglyph" style="align-content: center;">

Dat betekend 'mooi', 'perfect' of 'goed'. Dit soort combinaties van letters zijn gewoon niet uit te spreken en is ook moeilijk te vertalen.
In deze vertaler worden letters dus gewoon letterlijk één voor één vervangen door de hiëroglief of andersom.

Iets anders belangrijks, spaties en leestekens bestaan eigenlijk niet in het hiërogliefensysteem, maar worden tegenwoordig wel bij onze vertalers gebruikt om toch een woorden onderscheiding te zien.

Als laatste, meestal werd er van rechts naar links gelezen, maar beide varianten komt voor. De meeste wetenschappers doen het van links naar rechts. Maar symbolen van mensen of dieren moeten altijd naar de kant kijken van waaruit gelezen wordt. Als het dus van links naar rechts is, kijken ze naar links.


## Rechtstreekse Vertaling
Ik ben dus op zoek gegaan naar een hiërogliefen font, en eigenlijk elke karakter gewoon daarin omzetten. Dat heb ik op de volgende manier gedaan:

```HTML
<form>
	<div>
		<h2>Text</h2>
		<textarea placeholder="Text here ..." id="textarea-en" onKeyPress="javascript:changeTxtToHG();"></textarea>
	</div>
	
	<div>
		<h2>Hieroglyphs</h2>
		<textarea placeholder="Hieroglyphs here" id="textarea-hg" onKeyPress="javascript:changeTxtToEN();"></textarea>
	</div>
</form>

<script src="http://code.jquery.com/jquery-latest.js"></script>
```


```Javascript
var areaEN = document.getElementById('textarea-en');
var areaHG = document.getElementById('textarea-hg');

function changeTxtToHG(){ 
	areaHG.value = areaEN.value;
}

function changeTxtToEN(){ 
	areaEN.value = areaHG.value;
}
```


## Text detection op Images
Nadat ik dus ook rechtstreekse vertaling heb wil ik text uit images kunnen halen. Ik heb dat geprobeerd met de API van Sightengine.

```python
#API client and key
client = SightengineClient('407400170', 'PVmF8vE3vnunnu8LQumR')

# Sightengine API call to check for txt on img
output = client.check('text').set_file(filename)
print output
```

<img src="img/sightengine.PNG" alt="sightengine API call">

Helaas verteld deze API alleen of er text in zit of niet, en of deze er al op zat of achteraf op is geplaatst. Verder kan je uit deze API nog dingen halen zoals weapons, hatesigns, face detection, celebrities, etc. Maar de API verteld eigenlijk alleen hoeveel dat op de foto voorkomt en niet echt welke text bijvoorbeeld.



## Hiërogliefen omzetten via Ascii Art





## Image omzetten naar text






## Ascii Art Converter
<img src="img/convert-to-ascii.PNG" alt="convert to ascii art"><br>


## Img To Txt Converter

<img src="img/imgToTxt.PNG" alt="image converted to text"><br>
<img src="img/ImgToTxt2.PNG" alt="image converted to text"><br>
























## Resources

- https://medium.com/@sightengine_/image-upload-and-moderation-with-python-and-flask-e7585f43828a

- https://www.sitepoint.com/manipulating-images-with-the-python-imaging-library/

- https://github.com/ShadyAbuKalam/Hieroglyphics-translator

- https://sightengine.com/detect-artificial-text-watermarks

- https://www.geeksforgeeks.org/converting-image-ascii-image-python/





- https://medium.com/@MicroPyramid/extract-text-with-ocr-for-all-image-types-in-python-using-pytesseract-ec3c53e5fc3a
	- https://www.youtube.com/watch?v=_5ml_Y9hqG8

- https://commons.wikimedia.org/wiki/Category:Hieroglyphs_of_Egypt_(Alphabet)

- https://nl.wikipedia.org/wiki/Egyptische_hi%C3%ABrogliefen