# -*- coding: utf-8 -*-

from wiki9 import app
from flask import request, session, url_for, redirect, abort
from functools import wraps

def valid_login(username, password):
    if (username == app.config['ROOT_USERNAME']):
        return password == app.config['ROOT_PASSWORD']

def login_user(username, password):
    if valid_login(username, password):
        session["username"] = username
        return True
    return False

def logout_user():
    session.pop("username", None)

def is_root():
    return session.get("username", None) == app.config['ROOT_USERNAME']

def root_required(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if not is_root():
            return redirect(url_for('login', next=request.url))
        return func(*args, **kwargs)
    return wrapped

@app.context_processor
def inject_is_root():
    return dict(is_root=is_root)

