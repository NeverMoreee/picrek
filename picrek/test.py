import requests
import log

logger = log.get_logger('getpic')


def yan(url='https://yande.re/post.xml',
        limit=100, page=1, tags=None, proxy=None):
    try:
        param = {'page': page, 'limit': limit, 'tags': tags}
        req = requests.get(url, proxies=proxy, params=param)
        logger
        logger.info('yandere:status_code:%d, page:%d, limit:%d' %
                    (req.status_code, page, limit))
    except Exception as e:
        logger.error(str(e))
    return req.text


yan()