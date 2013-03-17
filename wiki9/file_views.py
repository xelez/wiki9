# -*- coding: utf-8 -*-
from wiki9 import app

## temp; server files from storage
from flask import send_from_directory
@app.route('/files/<path:filename>')
def send_storages(filename):
     return send_from_directory('/home/xelez/programming/wiki9/_data/files/', filename)

@app.route('/storages/<path:filename>')
def send_storages(filename):
     return send_from_directory('/home/xelez/programming/wiki9/_data/storages/', filename)

@app.route('/pics/<path:filename>')
def send_pics(filename):
     return send_from_directory('/home/xelez/programming/wiki9/_data/pics/', filename)

