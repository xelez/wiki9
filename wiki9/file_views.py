# -*- coding: utf-8 -*-
from wiki9 import app

from flask import send_from_directory
from os import path
## temp; server files from storage

@app.route('/files/<path:filename>')
def send_files(filename):
    directory = path.join(app.config['FILE_DIRECTORY'], 'files')
    return send_from_directory(directory, filename)

@app.route('/storages/<path:filename>')
def send_storages(filename):
    directory = path.join(app.config['FILE_DIRECTORY'], 'storages')
    return send_from_directory(directory, filename)

@app.route('/pics/<path:filename>')
def send_pics(filename):
    directory = path.join(app.config['FILE_DIRECTORY'], 'pics')
    return send_from_directory(directory, filename)

