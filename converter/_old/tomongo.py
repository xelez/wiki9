from mysql import sql_cursor
from phpickle import unserialize

#from utils.db import db
#from pymongo import ASCENDING, DESCENDING
#from datetime import datetime, time

#needs rewrite, see below
"""
def content_table():
    '''Converts table Content from MySQL to MongoDB'''
    
    data = []

    sql_cursor.execute("SELECT id,name,service,class,settings,parent,path FROM content ORDER BY precedence");
    table = sql_cursor.fetchall();
    
    for row in table:
        info = {
                'id'       : int(row[0]),
                'name'     : row[1],
                'service'  : row[2],
                'class'    : row[3],
                'settings' : None,
                'parent'   : int(row[5]),
                'path'     : row[6],
        }
        
        if row[4] is not None:
            opt = {};
	    for a,b in unserialize(row[4]):
                opt[a] = b;
            info['settings'] = opt;
	
        data += [info]
    
    db['content'].insert(data);

    return data
"""

def articles():
    '''Convert all content that have dataset set to 2 from MySQK to MongoDB'''

    data = [];
    for content in db['content'].find({'settings.dataset': '2'}):
        data += [content['path']];
        table = content['settings'].get('table', None);
        if table is None: continue;
        sql_cursor.execute("SELECT full FROM " + table)
        full = sql_cursor.fetchone()['full'];

        update = {
                "$set" : {"data_html": full},
                 }
       
        db['content'].update({"_id": content["_id"]}, update);
#            sql_cursor.execute("DROP TABLE " + table + ";");
 #       except:
  #          pass

    return data;

#Commented out because needs some rewrite when dealing with info dict
#Now sql returns dict, not list
"""
def news():
    '''Convert all content that have dataset set to 3 (NEWS) from MySQK to MongoDB'''

    debug = [];

    for news in db['content'].find( {'settings.dataset': '3', 'data' : {'$exists': False}} ):
        table = news['settings']['table'];
        name = 'news_' + str(news['path']);
        
        debug += [table];
        
        sql_cursor.execute("SELECT date, header, short, full FROM " + table)
        data = [];

        for tmp in sql_cursor.fetchall():
            info = {
                    "date"   : datetime.combine(tmp[0], time()),
                    "header" : tmp[1],
                    "short"  : tmp[2],
                    "full"   : tmp[3],
                    }
            data += [info]

        db[name].insert(data);
        db['content'].update({'_id': news['_id']}, {"$set" : {"data" : name, "type" : article} } )
        
    return debug;
"""

def graduates(table_years, table, cid):
    '''Convert graduates database'''
    sql_cursor.execute("SELECT * FROM " + table_years)
    years= []
    yearbyid = {}
    
    for row in sql_cursor.fetchall():
        y = int(row['year'])
        yearbyid[row['id']] = y
        years += [y]

    sql_cursor.execute("SELECT * FROM " + table)
    graduates = sql_cursor.fetchall()

    for student in graduates:
        student['year'] = yearbyid[student['parent']]
        del student['parent']
        del student['precedence']

    db['content'].update({'id':cid}, {"$set" : {"data_years" : years} })
    db['graduates'].insert(graduates);
    return graduates

def photos(table):
    '''Convert table with info about photos to MongoDB'''
    sql_cursor.execute("SELECT * FROM " + table)
    db['photos'].insert( sql_cursor.fetchall() )

def photogalleries(table):
    '''Convert table with info about photogalleries to MongoDB'''
    sql_cursor.execute("SELECT * FROM " + table)
    db['photogalleries'].insert( sql_cursor.fetchall() )


