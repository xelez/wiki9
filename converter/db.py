# -*- coding: utf-8 -*-

import config

# MySQL part
import sys;

import MySQLdb
import MySQLdb.cursors

try:
    conn = MySQLdb.connect (host = config.mysql_host,
                            user = config.mysql_user,
                            passwd = config.mysql_password,
                            db = config.mysql_db,
			    cursorclass=MySQLdb.cursors.DictCursor,
                            use_unicode = True,
			    charset = 'utf8'
			    )
    sql_cursor = conn.cursor()
except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit (1)


