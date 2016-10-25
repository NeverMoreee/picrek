import getpic
import db
import parser
import log
import config

logger = log.get_logger('main')


def main():

    logger.info('--------------------')
    logger.info('picrek-scrap started')
    logger.info('--------------------')
    data = config.init()
    mdb = db.Mysql()
    mdb.yan_crate()
    while True:
        try:
            yan_data = getpic.yan(page=1, limit=1)
            pics = parser.yan(yan_data)
            mdb.yan_insert(pics)
        except Exception as e:
            logger.info(str(e))


if __name__ == '__main__':
    main()
