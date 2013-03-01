# -*- coding: utf-8 -*-

from flask.ext.wtf import Form, TextField, TextAreaField, PasswordField, BooleanField, validators
from wiki9.utils import RedirectBackForm

class LoginForm(RedirectBackForm):
    login    = TextField(u"Логин", [validators.Required()])
    password = PasswordField(u"Пароль", [validators.Required()])

class EditPageForm(Form):
    path    = TextField(u"Адрес", [validators.Required()])
    title   = TextField(u"Название", [validators.Required()])
    content = TextAreaField(u"Содержание")


