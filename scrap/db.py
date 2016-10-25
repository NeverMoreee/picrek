import pymysql as mdb
import log

logger = log.get_logger('db')


class Mysql(object):
    def __init__(self):
        # connect to Mysql
        try:
            self.connect = mdb.connect(
                host='127.0.0.1', port=3306, user='root', passwd='yi')
            self.cursor = self.connect.cursor()
        except mdb.Error as e:
            logger.error('Error %d: %s' % (e.args[0], e.args[1]))
        else:
            logger.info('Mysql connected')
        # create picrek database
        try:
            self.cursor.execute('CREATE DATABASE IF NOT EXISTS picrek')
            self.cursor.execute('USE picrek')
        except mdb.error as e:
            logger.info(str(e))
        else:
            logger.info('entered database picrek')

    def select(self):
        sql_select = """SELECT * FROM geltest"""
        try:
            self.cursor.execute(sql_select)
            rows = self.cursor.fetchall()
        except mdb.Error as e:
            logger.error(str(e))
        for row in rows:
            logger.error(row)

    def gel_insert(self, pics):
        inserted = ''
        try:
            for pic in pics:
                inserted += (str(pic.pid) + ', ')
                sql_insert = """INSERT INTO gelbooru(pid, rating, score, tags,
                           file_url, file_height, file_width,
                           sample_url, sample_height, sample_width,
                           preview_url, preview_height, preview_width)
                           VALUES(%d, "%s", %d, "%s",
                                 "%s", %d, %d,
                                 "%s", %d, %d,
                                 "%s", %d, %d)
                           """ % (int(pic.pid), pic.rating,
                                  int(pic.score), pic.tags,
                                  pic.file['file_url'],
                                  int(pic.file['file_height']),
                                  int(pic.file['file_width']),
                                  pic.sample['sample_url'],
                                  int(pic.sample['sample_height']),
                                  int(pic.sample['sample_width']),
                                  pic.preview['preview_url'],
                                  int(pic.preview['preview_height']),
                                  int(pic.preview['preview_width']))
                self.cursor.execute(sql_insert)
                self.connect.commit()
        except mdb.Error as e:
            logger.error(str(e))
            if self.connect:
                self.connect.rollback()
        else:
            logger.info('gelbooru inserted:' + inserted)

    def yan_insert(self, pics):
        inserted = ''
        try:
            for pic in pics:
                inserted += (str(pic.pid) + ', ')
                sql_insert = """INSERT INTO yandere(pid, rating, score, tags,
                           file_url, file_height, file_width,
                           sample_url, sample_height, sample_width,
                           preview_url, preview_height, preview_width,
                           jpeg_url, jpeg_height, jpeg_width)
                           VALUES(%d, "%s", %d, "%s",
                                 "%s", %d, %d,
                                 "%s", %d, %d,
                                 "%s", %d, %d,
                                 "%s", %d, %d)
                           """ % (int(pic.pid), pic.rating,
                                  int(pic.score), pic.tags,
                                  pic.file['file_url'],
                                  int(pic.file['file_height']),
                                  int(pic.file['file_width']),
                                  pic.sample['sample_url'],
                                  int(pic.sample['sample_height']),
                                  int(pic.sample['sample_width']),
                                  pic.preview['preview_url'],
                                  int(pic.preview['preview_height']),
                                  int(pic.preview['preview_width']),
                                  pic.jpeg['jpeg_url'],
                                  int(pic.jpeg['jpeg_height']),
                                  int(pic.jpeg['jpeg_width'])
                                  )
                self.cursor.execute(sql_insert)
                self.connect.commit()
        except mdb.Error as e:
            logger.error(e.args[0])
            logger.error(e.args[1])
            if self.connect:
                self.connect.rollback()
        else:
            logger.info('yandere inserted:' + inserted)

    def gel_crate(self):
        sql_create = """CREATE TABLE IF NOT EXISTS gelbooru(
        pid INT PRIMARY KEY,
        rating CHAR(1),
        score SMALLINT UNSIGNED,
        tags TEXT,
        file_url TINYTEXT,
        file_height SMALLINT UNSIGNED,
        file_width SMALLINT UNSIGNED,
        sample_url TINYTEXT,
        sample_height SMALLINT UNSIGNED,
        sample_width SMALLINT UNSIGNED,
        preview_url TINYTEXT,
        preview_height SMALLINT UNSIGNED,
        preview_width SMALLINT UNSIGNED
        )
        """
        try:
            self.cursor.execute(sql_create)
            self.connect.commit()
        except mdb.Error as e:
            logger.error(str(e))
        else:
            logger.info('table gelbooru created')

    def yan_crate(self):
        sql_create = """CREATE TABLE IF NOT EXISTS yandere(
        pid INT PRIMARY KEY,
        rating CHAR(1),
        score SMALLINT UNSIGNED,
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
        jpeg_url TINYTEXT,
        jpeg_height SMALLINT UNSIGNED,
        jpeg_width SMALLINT UNSIGNED
        )
        """
        try:
            self.cursor.execute(sql_create)
            self.connect.commit()
        except mdb.Error as e:
            logger.error(str(e))
        else:
            logger.info('table yandere created')