import getpic
import db
import parser
import log

logger = log.get_logger('main')


def main():
    while True:
        logger.info('picrek started')
        # try:
        #     cur_page = 1
        #     yan_data = getpic.yan(page=1, limit=1)
        #     cur_page += 1
        #     pics = parser.yan(yan_data)
        #     mdb = db.Mysql()
        #     mdb.crate()
        #     mdb.insert(pics)
        # except Exception as e:
        #     logger.info(str(e))
        # finally:
        #     exit()
        cur_page = 1
        yan_data = getpic.yan(page=1, limit=1)
        cur_page += 1
        pics = parser.yan(yan_data)
        mdb = db.Mysql()
        mdb.crate()
        mdb.insert(pics)


if __name__ == '__main__':
    main()
