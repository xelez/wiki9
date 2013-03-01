# -*- coding: utf-8 -*-

from wiki9 import app, mongo

def setup_db():
    #TODO: add indexies to database and optimizations for some queries
    pass

with app.app_context():
    setup_db()
