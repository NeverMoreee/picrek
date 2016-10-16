import getpic
import db
import parser
import logging

config_url = '/home/nemos/code/picrekrepo/picrek'


def main():
    while True:
        cur_page = 1
        yan_data = getpic.yan(page=cur_page)
        cur_page += 1
        pics = parser.yan(yan_data)
        mdb = db.Mysql()
        mdb.crate()
        mdb.insert(pics)


if __name__ == '__main__':
    main()
