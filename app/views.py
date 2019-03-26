from app import app
from flask import url_for, redirect, render_template
from scipy import misc, ndimage
import re

from os import listdir
# from os.path import isfile, join
import os


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/images')
def images():
    url_for('static', filename='img/')
    images_path = [f for f in listdir(os.path.join(app.root_path, 'static', 'img'))]
    images_path = [path for path in images_path if re.search('.(jpg|png)$', path)]
    print(os.path.join(app.root_path, 'static', 'img'))
    print(images_path)
    return render_template('liste-images.html', images_path=images_path)


@app.route('/image/<nom>')
def view_image(nom):
    treatment_image(nom)
    return render_template('image.html', image=nom)


def treatment_image(name_file):
    img_path = os.path.join(app.root_path, 'static', 'img', name_file)
    img_array = ndimage.imread(img_path)
    img_resize = misc.imresize(img_array, 50)
    misc.imsave(os.path.join(app.root_path, 'static', 'img','train', 'resize_'+name_file), img_resize)
