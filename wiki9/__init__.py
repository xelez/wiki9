# -*- coding: utf-8 -*-

import os.path

from flask import Flask
from flask.ext.pymongo import PyMongo

from flask.ext.assets import Environment as AssetsEnvironment
from webassets.loaders import PythonLoader as PythonAssetsLoader

from flask.ext.admin import Admin

import config
app = Flask(__name__)
app.config.from_object(config)
app.config.from_envvar('WIKI9_SETTINGS', silent=True)

import assets
assets_env = AssetsEnvironment(app)
assets_loader = PythonAssetsLoader(assets)
for name, bundle in assets_loader.load_bundles().iteritems():
    assets_env.register(name, bundle)

mongo = PyMongo()
mongo.init_app(app)

from wiki9.manage import MyFileAdmin, PagesAdmin
admin = Admin(app, name='Wiki9 Manage', url='/manage');
admin.add_view(PagesAdmin(name='Pages', endpoint='pages'))
admin.add_view(MyFileAdmin(app.config['FILE_DIRECTORY'], '/', endpoint='files', name='Files'))

import wiki9.views
import wiki9.file_views
