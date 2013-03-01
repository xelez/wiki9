from utils.db import db
from pymongo import ASCENDING, DESCENDING
from datetime import datetime, time

def gen_navigation():
    level0 = db['content'].find({'parent': -1}, ('id', 'name', 'parent', 'path'))
    level0 = list(level0)

    i=1;
    for el in level0:
        el['url'] = '/'+el['path']+'/'
        el['order'] = i
        i += 1
    
    nav = list(level0)

    for el in level0:
        level1 = list( db['content'].find({'parent': el['id']}, ('id', 'name', 'parent', 'path')) )
        
        i=1
        for t in level1:
            t['url'] = '/'+el['path']+'/'+t['path']+'/'
            t['order'] = i
            i += 1
        
        nav += level1

    for el in nav:
        del el['path']

    db['nav'].drop()
    db['nav'].insert(nav)
