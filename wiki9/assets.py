# -*- coding: utf-8 -*-

from flask.ext.assets import Bundle

site_css = Bundle(
    'vendor/bootstrap/css/bootstrap.css',
    'css/app.css',
    'css/content.css',
    output = 'gen/site.css'
)

vendor_js = Bundle(
    'vendor/jquery/jquery-1.9.1.js',
    'vendor/bootstrap/js/bootstrap.js',
)

all_js = Bundle(
    vendor_js,
    output = 'gen/all.js'
)

