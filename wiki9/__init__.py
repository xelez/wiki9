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
assets_loader = PythonAssetsLoader(assets)
for name, bundle in assets_loader.load_bundles().iteritems():
    assets_env.register(name, bundle)

mongo = PyMongo()
mongo.init_app(app)

import wiki9.views
