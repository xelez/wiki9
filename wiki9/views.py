# -*- coding: utf-8 -*-

from wiki9 import app, mongo
from wiki9.auth import root_required, is_root, login_user, logout_user
from wiki9.utils import redirect_back
from wiki9.forms import LoginForm
from wiki9 import wiki

from flask import request, session, url_for, redirect, render_template, jsonify, safe_join, abort, g, flash

@app.route('/')
def index():
    return redirect(url_for('show_page', path='main'))

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if login_user(form.login.data, form.password.data):
            flash(u"Добро пожаловать", 'success')
            return form.redirect_back()
        else:
            flash(u"Неверный логин или пароль", 'alert')
    return render_template('login.html', form=form)

@app.route('/logout')
@root_required
def logout():
    logout_user()
    return redirect_back()

@app.route('/<path:path>/')
def show_page(path='main'):
    page = wiki.get_page(path)
    if not page: abort(404)

    if page.has_key('redirect'):
        return redirect(page['redirect'])
   
    sidenav = mongo.db['pages'].find_one({'path': 'sidenav'})
    if not sidenav: sidenav = {}

    return render_template('show_page.html', sidenav=sidenav, page=page)

@app.route('/ajax/preview', methods=['POST'])
@root_required
def ajax_preview():
    text =  request.form.get('markdown', '');
    return wiki.markdown_to_html(text)


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
