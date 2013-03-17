# -*- coding: utf-8 -*-

from wiki9 import mongo
from wiki9 import auth
from wiki9 import wiki

from flask.ext.admin import BaseView, expose
from flask.ext.admin.contrib.fileadmin import FileAdmin
from flask.ext import wtf

from flask import flash, redirect, url_for

class EditPageForm(wtf.Form):
    path    = wtf.TextField(u"Адрес", [wtf.validators.Required()])
    title   = wtf.TextField(u"Название", [wtf.validators.Required()])
    content = wtf.TextAreaField(u"Содержание")

class MyBaseView(BaseView):
    def is_accessible(self):
        return auth.is_root()

class MyFileAdmin(FileAdmin):
    editable_extensions = ('md', 'html', 'txt')

    def is_accessible(self):
        return auth.is_root()

class PagesAdmin(MyBaseView):
    @expose('/')
    def list(self):
        pages = mongo.db['pages'].find({}).sort('path')
        return self.render('manage/list_pages.html', pages=pages)

    @expose('/edit/<path:path>/', methods=['GET', 'POST'])
    def edit(self, path):
        page = mongo.db['pages'].find_one({'path': path})
        if page is None:
            page = {'path': path, 'title': '', 'content': ''}

        form = EditPageForm(**page)
        if form.validate_on_submit():
            wiki.save_page(form.path.data, form.title.data, form.content.data)
            flash(u"Изменения сохранены", "success")
            return redirect(url_for('show_page', path = page['path']))

        return self.render('manage/edit_page.html', form=form)

    @expose('/delete/<path:path>')
    def delete(self, path):
        wiki.delete_page(path)
        flash(u"Страница удалена", "success")
        return redirect(url_for('.list'))
     
