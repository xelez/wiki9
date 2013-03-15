# -*- coding: utf-8 -*-

import os.path

from flask import Flask
from flask.ext.pymongo import PyMongo

from flask.ext.assets import Environment as AssetsEnvironment
from webassets.loaders import PythonLoader as PythonAssetsLoader

from flask.ext.admin import Admin
from flask.ext.admin.contrib.fileadmin import FileAdmin

import config
app = Flask(__name__)
app.config.from_object(config)
app.config.from_envvar('WIKI9_SETTINGS', silent=True)

import assets
assets_env = AssetsEnvironment(app)
assets_loader = PythonAssetsLoader(assets)
for name, bundle in assets_loader.load_bundles().iteritems():
    assets_env.register(name, bundle)

admin = Admin(app);
admin.add_view(FileAdmin(app.static_folder, '/static/', name='Static Files'))

mongo = PyMongo()
mongo.init_app(app)

import wiki9.views
