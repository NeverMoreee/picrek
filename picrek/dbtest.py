import pymysql as mdb
import sys

try:
    con = mdb.connect(host='127.0.0.1', port='3366', user='root', passwd='yi')
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS geltest')
    cur.execute("CREATE TABLE geltest(pid INT PRIMARY KEY, \
                                      rating CHAR(1), \
                                      score TINYINT UNSIGNED, \
                                      tags TEXT, \
                                      file_height TINYINT UNSIGNED, \
                                      file_width TINYINT UNSIGNED, \
                                      sample_url TINYTEXT, \
                                      file_url TINYTEXT)")

except mdb.Error as e:
    if con:
        con.rollback()
    print('Error %d: %s' % (e.args[0], e.args[1]))
    sys.exit(1)

finally:
    if con:
        con.close()
