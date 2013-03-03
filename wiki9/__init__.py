# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask.ext.pymongo import PyMongo

from flask.ext.assets import Environment as AssetsEnvironment
from webassets.loaders import PythonLoader as PythonAssetsLoader

import config
import assets


app = Flask(__name__)
app.config.from_object(config)
app.config.from_envvar('WIKI9_SETTINGS', silent=True)

assets_env = AssetsEnvironment(app)
assets_env.load_path = [os.path.join(app.root_path, 'design')]

#hack because of stupid Flask-Assets, remove as soon as 0.9 released
assets_env.config['directory'] = assets_env.directory
assets_env.config['url'] = '/static/'

assets_loader = PythonAssetsLoader(assets)
for name, bundle in assets_loader.load_bundles().iteritems():
    assets_env.register(name, bundle)

mongo = PyMongo()
mongo.init_app(app)

import wiki9.views
