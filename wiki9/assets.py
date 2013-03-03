# -*- coding: utf-8 -*-

from flask.ext.assets import Bundle

site_css = Bundle(
    'css/normalize.css',
    'css/app.css',
    'css/content.css',
    output = 'gen/site.css'
)

head_js = Bundle(
    'js/vendor/custom.modernizr.js',
    output = 'gen/head.js',
)

vendor_js = Bundle(
    'js/vendor/jquery.js',
    'js/vendor/jquery.cookie.js',
)

foundation_js = Bundle(
    'js/foundation/foundation.js',
    'js/foundation/foundation.orbit.js',
    'js/foundation/foundation.placeholder.js',
    'js/foundation/foundation.alerts.js',
    'js/foundation/foundation.reveal.js',
    'js/foundation/foundation.tooltips.js',
    'js/foundation/foundation.topbar.js',
    'js/foundation/foundation.cookie.js',
    'js/foundation/foundation.section.js',
    'js/foundation/foundation.joyride.js',
    'js/foundation/foundation.forms.js',
    'js/foundation/foundation.dropdown.js',
    'js/foundation/foundation.clearing.js',
    'js/foundation/foundation.magellan.js',
)

all_js = Bundle(
    vendor_js,
    foundation_js,
    output = 'gen/all.js'
)

