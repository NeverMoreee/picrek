import getpic
import db
import parser
import log
import config

logger = log.get_logger('main')


def main():

    logger.info('|--------------------------|')
    logger.info('|---picrek-scrap started---|')
    logger.info('|--------------------------|')
    data = config.init()
    mdb = db.Mysql()

    # test
    yan(data=data['yandere'], mdb=mdb)
    # end


def gel(data=None, mdb=None):
    logger.info('start scraping gelbooru')
    mdb.gel_create()
    page = get_page(get=getpic.gel, par=parser.count, cur_id=data['cur_id'])
    while True:
        try:
            xml = getpic.gel(page=page, limit=100)
            pics = parser.gel(xml)
            mdb.gel_insert(pics)
        except Exception as e:
            logger.info(str(e))


def yan(data=None, mdb=None):
    logger.info('start scraping yandere')
    mdb.yan_create()
    page = get_page(get=getpic.yan, par=parser.count, cur_id=data['cur_id'])
    while True:
        try:
            xml = getpic.yan(page=page, limit=100)
            pics = parser.yan(xml)
            mdb.yan_insert(pics)
        except Exception as e:
            logger.info(str(e))


def get_page(get=None, par=None, cur_id=None):
    xml = get(limit=1)
    count = par(xml)
    return (count - cur_id) // 100


if __name__ == '__main__':
    main()
