# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.pymongo import PyMongo

import config

app = Flask(__name__)
app.config.from_object(config)
app.config.from_envvar('WIKI9_SETTINGS', silent=True)

mongo = PyMongo()
mongo.init_app(app)

import wiki9.views
