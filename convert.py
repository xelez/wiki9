from converter.db import sql_cursor
from converter.phpickle import unserialize

def get_table(table):
    sql_cursor.execute("SELECT * FROM " + table)
    return sql_cursor.fetchall()

def delete_table(table):
    sql_cursor.execute("DROP TABLE " + table)
    sql_cursor.commit()
    

def get_content_index():
    data = get_table('content')
    for row in data:
        if row['settings'] is not None:
            row.update(dict(unserialize(row['settings'])))
        del row['precedence']
        del row['settings']
        del row['class']
        row.pop(u'restable', None)
    return data

by_id = {}

def make_url(row):
    global by_id
    if ('url' in row):
        return row['url']
    if row['parent'] == -1:
        row['url'] = row['path']
    else:
        row['url'] = make_url(by_id[row['parent']]) + '/' + row['path'] 
    return row['url']

def get_by_id():
    global by_id

    for row in get_content_index():
        by_id[row['id']] = row
    
    for val  in by_id.values():
        make_url(val)

    return by_id

from pprint import pprint

import pymongo
conn = pymongo.Connection()
db = conn['wiki9']
pages = db['pages']


from bs4 import BeautifulSoup

def update_page(row, content):
    if content is None:
        print "what the fuck: %s" % row['url']
        content = '<body></body>'
    soup = BeautifulSoup(content, "lxml")
    html = soup.body.prettify()
    page = { 'path'    : row['url'],
             'title'   : row['name'],
             'content' : html,
             'html'    : html,
    }
    
    pages.update( {'path' : page['path']}, page, upsert = True)

def add_2_to_mongo():
    for row in get_by_id().values():
        if row.get(u'dataset') == '2':
            pprint(row['url'])
            html = get_table(row['table'])[0].get('full')
            update_page(row, html)

def list_all_other():
    for row in get_by_id().values():
        if row.get(u'dataset') != '2':
            pprint(row['url'])

add_2_to_mongo()    
#list_all_other()
