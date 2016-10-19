import pymysql as mdb
import log

logger = log.get_logger('db')


class Mysql(object):
    def __init__(self):
        try:
            self.connect = mdb.connect(
                host='127.0.0.1', port='3366', user='root', passwd='yi')
            self.cursor = self.connect.cursor()
        except mdb.Error as e:
            logger.error('Error %d: %s' % (e.args[0], e.args[1]))
        else:
            logger.info('database created')

    def crate(self):
        sql_create = """CREATE TABLE geltest(pid INT PRIMARY KEY,
                                              rating CHAR(1),
                                              score TYNYINT UNSIGNED,
                                              tags TEXT,
                                              file_url TINYTEXT,
                                              file_height SMALLINT UNSIGNED,
                                              file_width SMALLINT UNSIGNED,
                                              sample_url TINYTEXT,
                                              sample_height SMALLINT UNSIGNED,
                                              sample_width SMALLINT UNSIGNED,
                                              preview_url TINYTEXT,
                                              preview_height SMALLINT UNSIGNED,
                                              preview_width SMALLINT UNSIGNED,
                                              )"""
        try:
            self.cursor.execute('DROP TABLE IF EXISTS geltest')
            self.cursor.execute(sql_create)
            self.connect.commit()
        except mdb.Error as e:
            if self.connect:
                self.connect.rollback()
            logger.error('Error %d: %s' % (e.args[0], e.args[1]))

    def insert(self, pics):
        inserted = ''
        for pic in pics:
            inserted += str(pic.pid)
            sql_insert = """INSERT INTO geltest(pid, rating, score, tags
                         file_url, file_height, file_width,
                         sample_url, sample_height, sample_width,
                         preview_url, preview_height, preview_width)
                         Value('%d', '%s', '%d', '%s',
                               '%s', '%d', '%d'
                               '%s', '%d', '%d'
                               '%s', '%d', '%d')
                         """ % (pic.pid, pic.rating, pic.score, pic.tags,
                                pic.file['file_url'],
                                pic.file['file_height'],
                                pic.file['file_width'],
                                pic.sample['sample_url'],
                                pic.sample['sample_height'],
                                pic.sample['sample_width'],
                                pic.preview['preview_url'],
                                pic.preview['preview_height'],
                                pic.preview['preview_width'])
            try:
                self.cursor.execute(sql_insert)
                self.connect.commit()
            except mdb.Error as e:
                logger.error('Error %d: %s' % (e.args[0], e.args[1]))
                self.connect.rollback()
            else:
                logger.info('pic inserted' + inserted)

    def select(self):
        sql_select = """SELECT * FROM geltest"""
        try:
            self.cursor.execute(sql_select)
            rows = self.cursor.fetchall()
        except mdb.Error as e:
            logger.error('Error %d: %s' % (e.args[0], e.args[1]))
        for row in rows:
            logger.error(row)
