import getpic
import db
import parser
import log

logger = log.get_logger('main')


def main():

    logger.info('--------------')
    logger.info('picrek started')
    logger.info('--------------')
    mdb = db.Mysql()
    mdb.crate()
    while True:
        try:
            yan_data = getpic.yan(page=1, limit=100)
            pics = parser.yan(yan_data)
            # mdb.insert(pics)
        except Exception as e:
            logger.info(str(e))


if __name__ == '__main__':
    main()
