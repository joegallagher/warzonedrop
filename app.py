from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
from random import randint
from flask import Flask, render_template

app = Flask(__name__)

def generate_map():
    initialmap = Image.open('static/warzone1.png')
    dotimage = Image.open('static/dot.png')

    randomx = randint(420, 1520)
    randomy = randint(420, 1650)

    newmap = initialmap.copy()
    newmap.paste(dotimage, (randomx, randomy), dotimage.convert('RGBA'))
    newmap.save('static/mapobjective.png', quality=95)

@app.route('/')
def index():
    generate_map()
    return render_template('index.html')

