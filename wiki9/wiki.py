# -*- coding: utf-8 -*-

import markdown
import time
#from bs4 import BeautifulSoup

from wiki9 import mongo

md = markdown.Markdown(
        extensions = ['extra', 'meta', 'toc'], 
        safe_mode = False,
        output_format='html5'
)

def markdown_to_html(text):
    return md.convert(text)

def get_breadcrumbs(path):
    breadcrumbs = []
    current = ''
    for p in path.split('/')[:-1]:
        current += p + '/'
        breadcrumbs.append(
            mongo.db['pages'].find_one({'path': current[:-1]}, {'path' : 1, 'title' : 1} ) )
    return breadcrumbs

def save_page(path, title, text):
    html = md.convert(text)
    meta = md.Meta if hasattr(md, 'Meta') else {};
    
    breadcrumbs = get_breadcrumbs(path)
    breadcrumbs.append({'path': path, 'title': title})

    page = {
        'path'        : path,
        'title'       : title,
        'content'     : text,
        'html'        : html,
        'breadcrumbs' : breadcrumbs,
        'cache_ts'    : time.time(),
    }

    redirect = meta.get('redirect')
    if redirect:
        page['redirect'] = redirect[0]
    
    mongo.db['pages'].update({'path': page['path']}, page, upsert=True)
    return page

def delete_page(path):
    mongo.db['pages'].remove({'path': path})

def get_page(path):
    page = mongo.db['pages'].find_one({'path': path})
    if not page: return None

    if not page.has_key('cache_ts'):
        page = save_page(page['path'], page['title'], page['content'])
    
    return page
