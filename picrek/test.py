import requests
import log

logger = log.get_logger('getpic')

proxy = {
    'http': '47.89.53.92:3128',
}
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0)\
    Gecko/20100101 Firefox/49.0'
}


def yan(url='https://yande.re/post.xml',
        limit=100, page=1, tags=None, proxy=None):
    try:
        param = {'page': page, 'limit': limit, 'tags': tags}
        req = requests.get(url, proxies=proxy, params=param)
    except Exception as e:
        logger.error(str(e))
    else:
        logger.info('yandere:status_code:%d, page:%d, limit:%d' %
                    (req.status_code, page, limit))
        return req.text


yan(page=1, limit=100)
