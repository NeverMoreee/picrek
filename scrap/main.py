import getpic
import db
import parser
import log
import config
import err

logger = log.get_logger('main')


class Main(object):
    def __init__(self):
        logger.info('|--------------------------|')
        logger.info('|---picrek-scrap started---|')
        logger.info('|--------------------------|')
        self.conf = config.Config()
        self.mdb = db.Mysql()

    def gel(self):
        logger.info('start scraping gelbooru')
        self.mdb.gel_create()
        page = self.get_page(get=getpic.gel, par=parser.count,
                             cur_id=self.conf.data['gelbooru']['cur_pid'])
        while True:
            try:
                xml = getpic.gel(page=page, limit=100)
                pics = parser.gel(xml)
                self.mdb.gel_insert(pics)
            except err.ConnectException:
                page -= 1
                continue
            except err.ParserException:
                continue

    def yan(self):
        logger.info('start scraping yandere')
        self.mdb.yan_create()
        page = self.get_page(get=getpic.yan, par=parser.count,
                             cur_id=self.conf.data['yandere']['cur_pid'])
        while True:
            try:
                xml = getpic.yan(page=page, limit=100)
                pics = parser.yan(xml)
                self.mdb.yan_insert(pics)
                page -= 1
            except err.ConnectException:
                page -= 1
                continue
            except err.ParserException:
                continue

    def get_page(self, get=None, par=None, cur_id=None):
        xml = get(limit=1)
        count = par(xml)
        return (count - cur_id) // 100


if __name__ == '__main__':
    main = Main()
    main.yan()
